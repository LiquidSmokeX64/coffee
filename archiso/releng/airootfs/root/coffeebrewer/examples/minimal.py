import coffeebrewer

# Select a harddrive and a disk password
from coffeebrewer import User

coffeebrewer.log("Minimal only supports:")
coffeebrewer.log(" * Being installed to a single disk")

if coffeebrewer.arguments.get('help', None):
	coffeebrewer.log(" - Optional disk encryption via --!encryption-password=<password>")
	coffeebrewer.log(" - Optional filesystem type via --filesystem=<fs type>")
	coffeebrewer.log(" - Optional systemd network via --network")

coffeebrewer.arguments['harddrive'] = coffeebrewer.select_disk(coffeebrewer.all_blockdevices())


def install_on(mountpoint):
	# We kick off the installer by telling it where the
	with coffeebrewer.Installer(mountpoint) as installation:
		# Strap in the base system, add a boot loader and configure
		# some other minor details as specified by this profile and user.
		if installation.minimal_installation():
			installation.set_hostname('minimal-arch')
			installation.add_bootloader()

			# Optionally enable networking:
			if coffeebrewer.arguments.get('network', None):
				installation.copy_iso_network_config(enable_services=True)

			installation.add_additional_packages(['nano', 'wget', 'git'])
			installation.install_profile('minimal')

			user = User('devel', 'devel', False)
			installation.create_users(user)

	# Once this is done, we output some useful information to the user
	# And the installation is complete.
	coffeebrewer.log("There are two new accounts in your installation after reboot:")
	coffeebrewer.log(" * root (password: airoot)")
	coffeebrewer.log(" * devel (password: devel)")


if coffeebrewer.arguments['harddrive']:
	coffeebrewer.arguments['harddrive'].keep_partitions = False

	print(f" ! Formatting {coffeebrewer.arguments['harddrive']} in ", end='')
	coffeebrewer.do_countdown()

	# First, we configure the basic filesystem layout
	with coffeebrewer.Filesystem(coffeebrewer.arguments['harddrive'], coffeebrewer.GPT) as fs:
		# We use the entire disk instead of setting up partitions on your own
		if coffeebrewer.arguments['harddrive'].keep_partitions is False:
			fs.use_entire_disk(root_filesystem_type=coffeebrewer.arguments.get('filesystem', 'btrfs'))

		boot = fs.find_partition('/boot')
		root = fs.find_partition('/')

		boot.format('fat32')

		# We encrypt the root partition if we got a password to do so with,
		# Otherwise we just skip straight to formatting and installation
		if coffeebrewer.arguments.get('!encryption-password', None):
			root.encrypted = True
			root.encrypt(password=coffeebrewer.arguments.get('!encryption-password', None))

			with coffeebrewer.luks2(root, 'luksloop', coffeebrewer.arguments.get('!encryption-password', None)) as unlocked_root:
				unlocked_root.format(root.filesystem)
				unlocked_root.mount('/mnt')
		else:
			root.format(root.filesystem)
			root.mount('/mnt')

		boot.mount('/mnt/boot')

install_on('/mnt')
