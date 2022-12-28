# A desktop environment using "LXQt"

import coffeebrewer

is_top_level_profile = False

# NOTE: SDDM is the only officially supported greeter for LXQt, so unlike other DEs, lightdm is not used here.
# LXQt works with lightdm, but since this is not supported, we will not default to this.
# https://github.com/lxqt/lxqt/issues/795
__packages__ = [
	"lxqt",
	"breeze-icons",
	"oxygen-icons",
	"xdg-utils",
	"ttf-freefont",
	"leafpad",
	"slock",
	"sddm",
    "lximage-qt",
    "lxqt-about",
    "lxqt-admin",
    "lxqt-archiver",
    "lxqt-config",
    "lxqt-globalkeys",
    "lxqt-notificationd",
    "lxqt-openssh-askpass",
    "lxqt-panel",
    "lxqt-policykit",
    "lxqt-powermanagement",
    "lxqt-qtplugin",
    "lxqt-runner",
    "lxqt-session",
    "lxqt-sudo",
    "lxqt-themes",         
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# LXQt requires a functional xorg installation.
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("lxqt", "/somewhere/lxqt.py")
# or through conventional import lxqt
if __name__ == 'lxqt':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')

	# Install the LXQt packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)

	# Enable autostart of LXQt for all users
	coffeebrewer.storage['installation_session'].enable_service('sddm')
     
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
