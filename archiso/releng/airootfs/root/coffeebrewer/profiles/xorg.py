# A system with "xorg" installed

import coffeebrewer
import logging
from coffeebrewer.lib.hardware import __packages__ as __hwd__packages__

is_top_level_profile = True

__description__ = str(_('Installs a minimal system as well as xorg and graphics drivers.'))

__packages__ = [
	'dkms',
	'xorg-server',
	'xorg-xinit',
	'nvidia-open',
    'nvidia-utils',
    'nvidia-settings',
    'opencl-nvidia',
	*__hwd__packages__,
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	driver = coffeebrewer.select_driver()

	if driver:
		coffeebrewer.storage["gfx_driver_packages"] = driver
		return True

	# TODO: Add language section and/or merge it with the locale selected
	#       earlier in for instance guided.py installer.

	return False


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("xorg", "/somewhere/xorg.py")
# or through conventional import xorg
if __name__ == 'xorg':
	try:
		if "nvidia" in coffeebrewer.storage.get("gfx_driver_packages", []):
			if "linux-zen" in coffeebrewer.storage['installation_session'].base_packages or "linux-lts" in coffeebrewer.storage['installation_session'].base_packages:
				for kernel in coffeebrewer.storage['installation_session'].kernels:
					coffeebrewer.storage['installation_session'].add_additional_packages(f"{kernel}-headers") # Fixes https://github.com/archlinux/coffeebrewer/issues/585
				coffeebrewer.storage['installation_session'].add_additional_packages("dkms")  # I've had kernel regen fail if it wasn't installed before nvidia-dkms
				coffeebrewer.storage['installation_session'].add_additional_packages("xorg-server", "xorg-xinit", "nvidia-open", "nvidia-utils", "nvidia-settings", "opencl-nvidia")
			else:
				coffeebrewer.storage['installation_session'].add_additional_packages(f"xorg-server", "xorg-xinit", *coffeebrewer.storage.get('gfx_driver_packages', []))
		elif 'amdgpu' in coffeebrewer.storage.get("gfx_driver_packages", []):
			# The order of these two are important if amdgpu is installed #808
			if 'amdgpu' in coffeebrewer.storage['installation_session'].MODULES:
				coffeebrewer.storage['installation_session'].MODULES.remove('amdgpu')
			coffeebrewer.storage['installation_session'].MODULES.append('amdgpu')

			if 'radeon' in coffeebrewer.storage['installation_session'].MODULES:
				coffeebrewer.storage['installation_session'].MODULES.remove('radeon')
			coffeebrewer.storage['installation_session'].MODULES.append('radeon')

			coffeebrewer.storage['installation_session'].add_additional_packages(f"xorg-server", "xorg-xinit", *coffeebrewer.storage.get('gfx_driver_packages', []))
		else:
			coffeebrewer.storage['installation_session'].add_additional_packages(f"xorg-server", "xorg-xinit", *coffeebrewer.storage.get('gfx_driver_packages', []))
	except Exception as err:
		coffeebrewer.log(f"Could not handle nvidia and linuz-zen specific situations during xorg installation: {err}", level=logging.WARNING, fg="yellow")
		coffeebrewer.storage['installation_session'].add_additional_packages("xorg-server", "xorg-xinit")  # Prep didn't run, so there's no driver to install
