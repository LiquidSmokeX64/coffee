import logging
import os
import time

import coffeebrewer
from coffeebrewer import ConfigurationOutput, Menu
from coffeebrewer.lib.models.network_configuration import NetworkConfigurationHandler

if coffeebrewer.arguments.get('help'):
	print("See `man coffeebrewer` for help.")
	exit(0)
if os.getuid() != 0:
	print(_("Coffeebrewer requires root privileges to run. See --help for more."))
	exit(1)

# Log various information about hardware before starting the installation. This might assist in troubleshooting
coffeebrewer.log(f"Hardware model detected: {coffeebrewer.sys_vendor()} {coffeebrewer.product_name()}; UEFI mode: {coffeebrewer.has_uefi()}", level=logging.DEBUG)
coffeebrewer.log(f"Processor model detected: {coffeebrewer.cpu_model()}", level=logging.DEBUG)
coffeebrewer.log(f"Memory statistics: {coffeebrewer.mem_available()} available out of {coffeebrewer.mem_total()} total installed", level=logging.DEBUG)
coffeebrewer.log(f"Virtualization detected: {coffeebrewer.virtualization()}; is VM: {coffeebrewer.is_vm()}", level=logging.DEBUG)
coffeebrewer.log(f"Graphics devices detected: {coffeebrewer.graphics_devices().keys()}", level=logging.DEBUG)

# For support reasons, we'll log the disk layout pre installation to match against post-installation layout
coffeebrewer.log(f"Disk states before installing: {coffeebrewer.disk_layouts()}", level=logging.DEBUG)


def ask_user_questions():
	"""
		First, we'll ask the user for a bunch of user input.
		Not until we're satisfied with what we want to install
		will we continue with the actual installation steps.
	"""

	# ref: https://github.com/archlinux/coffeebrewer/pull/831
	# we'll set NTP to true by default since this is also
	# the default value specified in the menu options; in
	# case it will be changed by the user we'll also update
	# the system immediately
	global_menu = coffeebrewer.GlobalMenu(data_store=coffeebrewer.arguments)

	global_menu.enable('coffeebrewer-language')

	global_menu.enable('keyboard-layout')

	# Set which region to download packages from during the installation
	global_menu.enable('mirror-region')

	global_menu.enable('sys-language')
	global_menu.enable('sys-encoding')

	# Ask which harddrives/block-devices we will install to
	# and convert them into coffeebrewer.BlockDevice() objects.
	global_menu.enable('harddrives')

	global_menu.enable('disk_layouts')

	# Specify disk encryption options
	global_menu.enable('disk_encryption')

	# Ask which boot-loader to use (will only ask if we're in UEFI mode, otherwise will default to GRUB)
	global_menu.enable('bootloader')

	global_menu.enable('swap')

	# Get the hostname for the machine
	global_menu.enable('hostname')

	# Ask for a root password (optional, but triggers requirement for super-user if skipped)
	global_menu.enable('!root-password')

	global_menu.enable('!users')

	# Ask for coffeebrewer-specific profiles (such as desktop environments etc)
	global_menu.enable('profile')

	# Ask about audio server selection if one is not already set
	global_menu.enable('audio')

	# Ask for preferred kernel:
	global_menu.enable('kernels')

	global_menu.enable('packages')

	if coffeebrewer.arguments.get('advanced', False):
		# Enable parallel downloads
		global_menu.enable('parallel downloads')

	# Ask or Call the helper function that asks the user to optionally configure a network.
	global_menu.enable('nic')

	global_menu.enable('timezone')

	global_menu.enable('ntp')

	global_menu.enable('additional-repositories')

	global_menu.enable('__separator__')

	global_menu.enable('save_config')
	global_menu.enable('install')
	global_menu.enable('abort')

	global_menu.run()


def perform_filesystem_operations():
	"""
		Issue a final warning before we continue with something un-revertable.
		We mention the drive one last time, and count from 5 to 0.
	"""

	if coffeebrewer.arguments.get('harddrives', None):
		print(_(f" ! Formatting {coffeebrewer.arguments['harddrives']} in "), end='')
		coffeebrewer.do_countdown()

		"""
			Setup the blockdevice, filesystem (and optionally encryption).
			Once that's done, we'll hand over to perform_installation()
		"""
		mode = coffeebrewer.GPT
		if coffeebrewer.has_uefi() is False:
			mode = coffeebrewer.MBR

		for drive in coffeebrewer.arguments.get('harddrives', []):
			if coffeebrewer.arguments.get('disk_layouts', {}).get(drive.path):
				with coffeebrewer.Filesystem(drive, mode) as fs:
					fs.load_layout(coffeebrewer.arguments['disk_layouts'][drive.path])


def perform_installation(mountpoint):
	"""
	Performs the installation steps on a block device.
	Only requirement is that the block devices are
	formatted and setup prior to entering this function.
	"""

	with coffeebrewer.Installer(mountpoint, kernels=coffeebrewer.arguments.get('kernels', ['linux'])) as installation:
		# Mount all the drives to the desired mountpoint
		# This *can* be done outside of the installation, but the installer can deal with it.
		if coffeebrewer.arguments.get('disk_layouts'):
			installation.mount_ordered_layout(coffeebrewer.arguments['disk_layouts'])

		# Placing /boot check during installation because this will catch both re-use and wipe scenarios.
		for partition in installation.partitions:
			if partition.mountpoint == installation.target + '/boot':
				if partition.size < 0.19: # ~200 MiB in GiB
					raise coffeebrewer.DiskError(f"The selected /boot partition in use is not large enough to properly install a boot loader. Please resize it to at least 200MiB and re-run the installation.")

		# if len(mirrors):
		# Certain services might be running that affects the system during installation.
		# Currently, only one such service is "reflector.service" which updates /etc/pacman.d/mirrorlist
		# We need to wait for it before we continue since we opted in to use a custom mirror/region.
		installation.log('Waiting for automatic mirror selection (reflector) to complete.', level=logging.INFO)
		while coffeebrewer.service_state('reflector') not in ('dead', 'failed'):
			time.sleep(1)

		# If we've activated NTP, make sure it's active in the ISO too and
		# make sure at least one time-sync finishes before we continue with the installation
		if coffeebrewer.arguments.get('ntp', False):
			# Activate NTP in the ISO
			coffeebrewer.SysCommand('timedatectl set-ntp true')

			# TODO: This block might be redundant, but this service is not activated unless
			# `timedatectl set-ntp true` is executed.
			logged = False
			while coffeebrewer.service_state('dbus-org.freedesktop.timesync1.service') not in ('running'):
				if not logged:
					installation.log(f"Waiting for dbus-org.freedesktop.timesync1.service to enter running state", level=logging.INFO)
					logged = True
				time.sleep(1)

			logged = False
			while 'Server: n/a' in coffeebrewer.SysCommand('timedatectl timesync-status --no-pager --property=Server --value'):
				if not logged:
					installation.log(f"Waiting for timedatectl timesync-status to report a timesync against a server", level=logging.INFO)
					logged = True
				time.sleep(1)

		# Set mirrors used by pacstrap (outside of installation)
		if coffeebrewer.arguments.get('mirror-region', None):
			coffeebrewer.use_mirrors(coffeebrewer.arguments['mirror-region'])  # Set the mirrors for the live medium

		# Retrieve list of additional repositories and set boolean values appropriately
		if coffeebrewer.arguments.get('additional-repositories', None) is not None:
			enable_testing = 'testing' in coffeebrewer.arguments.get('additional-repositories', None)
			enable_multilib = 'multilib' in coffeebrewer.arguments.get('additional-repositories', None)
		else:
			enable_testing = False
			enable_multilib = True

		if installation.minimal_installation(
				testing=enable_testing, multilib=enable_multilib, hostname=coffeebrewer.arguments['hostname'],
				locales=[f"{coffeebrewer.arguments['sys-language']} {coffeebrewer.arguments['sys-encoding'].upper()}"]):
			if coffeebrewer.arguments.get('mirror-region') is not None:
				if coffeebrewer.arguments.get("mirrors", None) is not None:
					installation.set_mirrors(coffeebrewer.arguments['mirror-region'])  # Set the mirrors in the installation medium
			if coffeebrewer.arguments.get('swap'):
				installation.setup_swap('zram')
			if coffeebrewer.arguments.get("bootloader") == "grub-install" and coffeebrewer.has_uefi():
				installation.add_additional_packages("grub")
			installation.add_bootloader(coffeebrewer.arguments["bootloader"])

			# If user selected to copy the current ISO network configuration
			# Perform a copy of the config
			network_config = coffeebrewer.arguments.get('nic', None)

			if network_config:
				handler = NetworkConfigurationHandler(network_config)
				handler.config_installer(installation)

			if coffeebrewer.arguments.get('audio', None) is not None:
				installation.log(f"This audio server will be used: {coffeebrewer.arguments.get('audio', None)}", level=logging.INFO)
				if coffeebrewer.arguments.get('audio', None) == 'pipewire':
					coffeebrewer.Application(installation, 'pipewire').install()
				elif coffeebrewer.arguments.get('audio', None) == 'pulseaudio':
					print('Installing pulseaudio ...')
					installation.add_additional_packages("pulseaudio")
			else:
				installation.log("No audio server will be installed.", level=logging.INFO)

			if coffeebrewer.arguments.get('packages', None) and coffeebrewer.arguments.get('packages', None)[0] != '':
				installation.add_additional_packages(coffeebrewer.arguments.get('packages', None))

			if coffeebrewer.arguments.get('profile', None):
				installation.install_profile(coffeebrewer.arguments.get('profile', None))

			if users := coffeebrewer.arguments.get('!users', None):
				installation.create_users(users)

			if timezone := coffeebrewer.arguments.get('timezone', None):
				installation.set_timezone(timezone)

			if coffeebrewer.arguments.get('ntp', False):
				installation.activate_time_syncronization()

			if coffeebrewer.accessibility_tools_in_use():
				installation.enable_espeakup()

			if (root_pw := coffeebrewer.arguments.get('!root-password', None)) and len(root_pw):
				installation.user_set_pw('root', root_pw)

			# This step must be after profile installs to allow profiles to install language pre-requisits.
			# After which, this step will set the language both for console and x11 if x11 was installed for instance.
			installation.set_keyboard_language(coffeebrewer.arguments['keyboard-layout'])

			if coffeebrewer.arguments['profile'] and coffeebrewer.arguments['profile'].has_post_install():
				with coffeebrewer.arguments['profile'].load_instructions(namespace=f"{coffeebrewer.arguments['profile'].namespace}.py") as imported:
					if not imported._post_install():
						coffeebrewer.log(' * Profile\'s post configuration requirements was not fulfilled.', fg='red')
						exit(1)

		# If the user provided a list of services to be enabled, pass the list to the enable_service function.
		# Note that while it's called enable_service, it can actually take a list of services and iterate it.
		if coffeebrewer.arguments.get('services', None):
			installation.enable_service(*coffeebrewer.arguments['services'])

		# If the user provided custom commands to be run post-installation, execute them now.
		if coffeebrewer.arguments.get('custom-commands', None):
			coffeebrewer.run_custom_user_commands(coffeebrewer.arguments['custom-commands'], installation)

		installation.genfstab()

		installation.log("For post-installation tips, see https://wiki.archlinux.org/index.php/Installation_guide#Post-installation", fg="yellow")
		if not coffeebrewer.arguments.get('silent'):
			prompt = str(_('Would you like to chroot into the newly created installation and perform post-installation configuration?'))
			choice = Menu(prompt, Menu.yes_no(), default_option=Menu.yes()).run()
			if choice.value == Menu.yes():
				try:
					installation.drop_to_shell()
				except:
					pass

	# For support reasons, we'll log the disk layout post installation (crash or no crash)
	coffeebrewer.log(f"Disk states after installing: {coffeebrewer.disk_layouts()}", level=logging.DEBUG)


if coffeebrewer.arguments.get('skip-mirror-check', False) is False and coffeebrewer.check_mirror_reachable() is False:
	log_file = os.path.join(coffeebrewer.storage.get('LOG_PATH', None), coffeebrewer.storage.get('LOG_FILE', None))
	coffeebrewer.log(f"Coffee Linux mirrors are not reachable. Please check your internet connection and the log file '{log_file}'.", level=logging.INFO, fg="red")
	exit(1)

if not coffeebrewer.arguments.get('offline'):
	latest_version_archlinux_keyring = max([k.pkg_version for k in coffeebrewer.find_package('archlinux-keyring')])

	# If we want to check for keyring updates
	# and the installed package version is lower than the upstream version
	if coffeebrewer.arguments.get('skip-keyring-update', False) is False and \
		coffeebrewer.installed_package('archlinux-keyring').version < latest_version_archlinux_keyring:

		# Then we update the keyring in the ISO environment
		if not coffeebrewer.update_keyring():
			log_file = os.path.join(coffeebrewer.storage.get('LOG_PATH', None), coffeebrewer.storage.get('LOG_FILE', None))
			coffeebrewer.log(f"Failed to update the keyring. Please check your internet connection and the log file '{log_file}'.", level=logging.INFO, fg="red")
			exit(1)

if not coffeebrewer.arguments.get('silent'):
	ask_user_questions()

config_output = ConfigurationOutput(coffeebrewer.arguments)
if not coffeebrewer.arguments.get('silent'):
	config_output.show()
config_output.save()

if coffeebrewer.arguments.get('dry_run'):
	exit(0)

if not coffeebrewer.arguments.get('silent'):
	input(str(_('Press Enter to continue.')))

coffeebrewer.configuration_sanity_check()
perform_filesystem_operations()
perform_installation(coffeebrewer.storage.get('MOUNT_POINT', '/mnt'))
