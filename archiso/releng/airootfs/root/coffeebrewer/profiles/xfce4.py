# A desktop environment using "Xfce4"

import coffeebrewer

is_top_level_profile = False

__packages__ = [
	"xfce4",
	"xfce4-goodies",
	"pavucontrol",
	"lightdm",
	"lightdm-slick-greeter",
	"gvfs",
	"xarchiver",
    "arc-gtk-theme",
    "capitaine-cursors",
    "cpupower",
    "epdfview",
    "galculator",
    "geary",
    "gtk3",
    "mousepad",
    "parole",
    "ristretto",
    "thunar-archive-plugin",
    "thunar-media-tags-plugin",
    "xdg-user-dirs-gtk",
    "xfce4-battery-plugin",
    "xfce4-datetime-plugin",
    "xfce4-mount-plugin",
    "xfce4-netload-plugin",
    "xfce4-notifyd",
    "xfce4-pulseaudio-plugin",
    "xfce4-screensaver",
    "xfce4-taskmanager",
    "xfce4-wavelan-plugin",
    "xfce4-weather-plugin",
    "xfce4-whiskermenu-plugin",
    "xfce4-xkb-plugin",
    "xfwm4",
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

	# XFCE requires a functional xorg installation.
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("xfce4", "/somewhere/xfce4.py")
# or through conventional import xfce4
if __name__ == 'xfce4':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')

	# Install the XFCE4 packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
    coffeebrewer.storage['installation_session'].add_additional_packages(__yaypackages__)

	coffeebrewer.storage['installation_session'].enable_service('lightdm')  # Light Display Manager
    printf "%b\n[Seat:*]\ngreeter-session=lightdm-slick-greeter\n" "$*" >> /mnt/etc/lightdm/lightdm.conf
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
