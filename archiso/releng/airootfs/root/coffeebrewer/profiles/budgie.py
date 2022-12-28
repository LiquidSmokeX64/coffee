# A desktop environment using "budgie"

import coffeebrewer

is_top_level_profile = False

# "It is recommended also to install the gnome group, which contains applications required for the standard GNOME experience." - Arch Wiki
__packages__ = [
	"budgie-desktop",
	"gnome",
    "gnome-extra",
	"lightdm",
	"lightdm-gtk-greeter",
    "gnome-color-manager",
    "gnome-console",
    "gnome-firmware",
    "gnome-keyring",
    "gnome-menus",
    "gnome-online-accounts",
    "gnome-text-editor", 
    "xdg-desktop-portal-gnome",
]

__yaypackages__ = [
	"gnome-themes-extra",
    "humanity-icon-theme",
    "gnome-shell-extension-ubuntu-dock",
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-desktop-icons-ng",
    "yaru-gtk-theme",
    "yaru-icon-theme",
    "yaru-gnome-shell-theme",
    "yaru-session",
    "yaru-sound-theme",
    "yaru-unity-theme",
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# budgie requires a functioning Xorg installation.
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("budgie", "/somewhere/budgie.py")
# or through conventional import budgie
if __name__ == 'budgie':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')

	# Install the Budgie packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
    coffeebrewer.storage['installation_session'].add_additional_packages(__yaypackages__)
    
	coffeebrewer.storage['installation_session'].enable_service('lightdm')  # Light Display Manager
    rm -R /mnt/usr/share/backgrounds/gnome/ 
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
