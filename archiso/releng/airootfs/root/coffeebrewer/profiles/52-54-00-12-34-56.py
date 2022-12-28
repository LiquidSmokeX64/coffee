import coffeebrewer

# import json
# import urllib.request

__packages__ = ['nano', 'wget', 'git']

if __name__ == '52-54-00-12-34-56':
	awesome = coffeebrewer.Application(coffeebrewer.storage['installation_session'], 'postgresql')
	awesome.install()

"""
# Unmount and close previous runs (Mainly only used for re-runs, but won't hurt.)
coffeebrewer.sys_command(f'umount -R /mnt', suppress_errors=True)
coffeebrewer.sys_command(f'cryptsetup close /dev/mapper/luksloop', suppress_errors=True)

# Select a harddrive and a disk password
harddrive = coffeebrewer.all_blockdevices()['/dev/sda']
disk_password = '1234'

with coffeebrewer.Filesystem(harddrive) as fs:
	# Use the entire disk instead of setting up partitions on your own
	fs.use_entire_disk('luks2')

	if harddrive.partition[1].size == '512M':
		raise OSError('Trying to encrypt the boot partition for Pete's sake..')
	harddrive.partition[0].format('fat32')

	with coffeebrewer.luks2(harddrive.partition[1], 'luksloop', disk_password) as unlocked_device:
		unlocked_device.format('btrfs')

		with coffeebrewer.Installer(
				unlocked_device,
				boot_partition=harddrive.partition[0],
				hostname="testmachine"
		) as installation:
			if installation.minimal_installation():
				installation.add_bootloader()

				installation.add_additional_packages(__packages__)
				installation.install_profile('awesome')

				user = User('devel', 'devel', False)
				installation.create_users(user)
				installation.user_set_pw('root', 'toor')

				print(f'Submitting {coffeebrewer.__version__}: success')

				conditions = {
					"project": "coffeebrewer",
					"profile": "52-54-00-12-34-56",
					"status": "success",
					"version": coffeebrewer.__version__
				}
				req = urllib.request.Request("https://api.archlinux.life/build/success",
												data=json.dumps(conditions).encode('utf8'),
												headers={'content-type': 'application/json'})
				try:
					urllib.request.urlopen(req, timeout=5)
				except:
					pass
"""
