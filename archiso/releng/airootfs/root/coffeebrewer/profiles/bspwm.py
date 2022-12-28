# A desktop environment using the bspwm window manager.

import coffeebrewer

is_top_level_profile = False

__packages__ = [
	'bspwm',
	'sxhkd',
	'dmenu',
	'xdo',
	'rxvt-unicode',
	'lightdm',
	'lightdm-gtk-greeter',
]

def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# bspwm requires a functioning Xorg installation.
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("bspwm", "/somewhere/bspwm.py")
# or through conventional import bspwm
if __name__ == 'bspwm':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')
	# Install bspwm packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
	# Set up LightDM for login
	coffeebrewer.storage['installation_session'].enable_service('lightdm')
     
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
