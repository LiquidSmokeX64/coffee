# A desktop environment using "MATE"

import coffeebrewer

is_top_level_profile = False

__packages__ = [
	"mate",
	"mate-extra",
	"lightdm",
	"lightdm-slick-greeter",
    "engrampa",
    "eom",
    "gnome-calculator",
    "gnome-color-manager",
    "gnome-console",
    "gnome-keyring",
    "gnome-menus",
    "leafpad",
    "gtk3",
    "gtk-engines",
    "marco",
    "mate-applet-dock",
    "mate-applet-streamer",
    "mate-common",
    "mate-media",
    "mate-menu",
    "mate-netbook",
    "mate-power-manager",
    "mate-system-monitor ",
    "mate-terminal",                 
]

__yaypackages__ = [
	"lightdm-settings",
    "mint-themes",
    "mint-x-icons",
    "mint-y-icons",
    "mint-backgrounds",
    "yaru-gtk-theme",
    "yaru-icon-theme",
    "mintlocale",
    "humanity-icon-theme",
    "mint-themes-legacy",
    "mint-artwork",
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# MATE requires a functional xorg installation.
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("mate", "/somewhere/mate.py")
# or through conventional import mate
if __name__ == 'mate':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')

	# Install the MATE packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
    coffeebrewer.storage['installation_session'].add_additional_packages(__yaypackages__)

	coffeebrewer.storage['installation_session'].enable_service('lightdm')  # Light Display Manager
    printf "%b\n[Seat:*]\ngreeter-session=lightdm-slick-greeter\n" "$*" >> /mnt/etc/lightdm/lightdm.conf
     
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
