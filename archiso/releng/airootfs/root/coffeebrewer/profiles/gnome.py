# A desktop environment using "Gnome"

import coffeebrewer

is_top_level_profile = False

# Note: GDM should be part of the gnome group, but adding it here for clarity
__packages__ = [
	"gnome",
    "gnome-extra",
	"gnome-tweaks",
	"gdm",
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
    "gdm-settings",
]

def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# Gnome optionally supports xorg, we'll install it since it also
	# includes graphic driver setups (this might change in the future)
	profile = coffeebrewer.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("gnome", "/somewhere/gnome.py")
# or through conventional import gnome
if __name__ == 'gnome':
	# Install dependency profiles
	coffeebrewer.storage['installation_session'].install_profile('xorg')

	# Install the GNOME packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
    coffeebrewer.storage['installation_session'].add_additional_packages_yay(__yaypackages__)

	coffeebrewer.storage['installation_session'].enable_service('gdm')  # Gnome Display Manager
    rm -r /mnt/usr/share/xsessions/gnome*
    rm -r /mnt/usr/share/wayland-sessions/gnome*
    rm -R /mnt/usr/share/backgrounds/gnome/ 
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/
# We could also start it via xinitrc since we do have Xorg,
# but for gnome that's deprecated and wayland is preferred.
