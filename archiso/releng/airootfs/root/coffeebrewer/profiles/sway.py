# A desktop environment using "Sway"
import coffeebrewer
from coffeebrewer import Menu

is_top_level_profile = False

__packages__ = [
	"sway",
	"swaylock",
	"swayidle",
	"waybar",
	"dmenu",
	"light",
	"grim",
	"slurp",
	"pavucontrol",
	"foot",
]


def _check_driver() -> bool:
	packages = coffeebrewer.storage.get("gfx_driver_packages", [])

	if packages and "nvidia" in packages:
		prompt = 'The proprietary Nvidia driver is not supported by Sway. It is likely that you will run into issues, are you okay with that?'
		choice = Menu(prompt, Menu.yes_no(), default_option=Menu.no(), skip=False).run()

		if choice.value == Menu.no():
			return False

	return True


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
		if not _check_driver():
			return _prep_function(args, kwargs)
		return True

	return False


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("sway", "/somewhere/sway.py")
# or through conventional import sway
if __name__ == "sway":
	if not _check_driver():
		raise coffeebrewer.lib.exceptions.HardwareIncompatibilityError("Sway does not support the proprietary nvidia drivers.")

	# Install the Sway packages
	coffeebrewer.storage['installation_session'].add_additional_packages(__packages__)
    mkdir -p /mnt/usr/share/backgrounds/gnome/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/backgrounds/gnome/
    mkdir -p /mnt/usr/share/wallpapers/coffee/
    cp /opt/backgrounds/coffee/* /mnt/usr/share/wallpapers/coffee/

	# Install the graphics driver packages
	coffeebrewer.storage['installation_session'].add_additional_packages(f"xorg-server xorg-xinit {' '.join(coffeebrewer.storage.get('gfx_driver_packages', None))}")
