# A desktop environment selector.
from typing import Any, TYPE_CHECKING

import coffeebrewer
from coffeebrewer import log, Menu
from coffeebrewer.lib.menu.menu import MenuSelectionType

if TYPE_CHECKING:
	_: Any

is_top_level_profile = True

__description__ = str(_("Provides a selection of desktop environments and tiling window managers, e.g. gnome, kde, sway"))

# New way of defining packages for a profile, which is iterable and can be used out side
# of the profile to get a list of "what packages will be installed".
__packages__ = [
	"nano",
	"vim",
	"openssh",
	"htop",
	"wget",
	"iwd",
	"wireless_tools",
	"wpa_supplicant",
	"smartmontools",
	"xdg-utils",
]

__yaypackages__ = [
	"ast-firmware",
    "mkinitcpio-firmware",
    "text-engine-git",
    "pamac-aur",
    "vmware-workstation",
    "amdgpu-fan",
    "shim-signed",
    "preloader-signed",
    "protontricks",
    "game-devices-udev",
    "microsoft-edge-stable",
    "mangohud",
    "gamescope",
    "dxvk-bin",
    "ntfix",
    "snapd",
    "snapd-glib",
]

__coffeepackages__ = [
	"nano",
	"vim",
	"openssh",
	"htop",
	"wget",
	"iwd",
	"wireless_tools",
	"wpa_supplicant",
	"smartmontools",
	"xdg-utils",
    "alsa-lib",
    "alsa-plugins",
    "amd-ucode",
    "apparmor",
    "archinstall",
    "arch-install-scripts",
    "archiso",
    "archivetools",
    "archlinux-wallpaper",
    "aria2",
    "b43-fwcutter",
    "base",
    "base-devel",
    "bash-completion",
    "bash-language-server",
    "bind",
    "bluez-libs",
    "brltty",
    "broadcom-wl",
    "btrfs-progs",
    "cabextract",
    "chrony",
    "clang",
    "clonezilla",
    "cloud-init",
    "cmake",
    "colord",
    "cronie",
    "cryptsetup",
    "cups",
    "darkhttpd",
    "dbus",
    "dbus-python",
    "dconf",
    "ddrescue",
    "dhclient",
    "dhcpcd",
    "diffutils",
    "directx-headers",
    "discord",
    "dkms",
    "dmidecode",
    "dmraid",
    "dnsmasq",
    "dosfstools",
    "e2fsprogs",
    "edk2-shell",
    "efibootmgr",
    "efitools",
    "egl-wayland",
    "elfutils",
    "espeakup",
    "ethtool",
    "exfatprogs",
    "expat",
    "extra-cmake-modules",
    "f2fs-tools",
    "fatresize",
    "file-roller",
    "firewalld",
    "flatpak",
    "fsarchiver",
    "gettext",
    "giflib",
    "gimp",
    "git",
    "glib2",
    "glibc",
    "gnu-free-fonts",
    "gnu-netcat",
    "gnutls",
    "go",
    "gpart",
    "gpm",
    "gptfdisk",
    "grml-zsh-config",
    "grub",
    "gst-libav",
    "gst-plugin-pipewire",
    "gst-plugins-bad",
    "gst-plugins-base",
    "gst-plugins-base-libs",
    "gst-plugins-good",
    "gst-plugins-ugly",
    "gstreamer",
    "gtk4",
    "gtk-engine-murrine",
    "hdparm",
    "hicolor-icon-theme",
    "hyperv",
    "innoextract",
    "intel-ucode",
    "irssi",
    "iw",
    "iwd",
    "jdk-openjdk",
    "jfsutils",
    "jre-openjdk",
    "jre-openjdk-headless",
    "kcmutils",
    "kitty-terminfo",
    "less",
    "lftp",
    "lib32-alsa-lib",
    "lib32-alsa-plugins",
    "lib32-giflib",
    "lib32-gnutls",
    "lib32-gst-plugins-base-libs",
    "lib32-libjpeg-turbo",
    "lib32-libldap",
    "lib32-libpng",
    "lib32-libpulse",
    "lib32-libva",
    "lib32-libva-mesa-driver",
    "lib32-libxcomposite",
    "lib32-libxinerama",
    "lib32-libxslt",
    "lib32-mesa-vdpau",
    "lib32-mpg123",
    "lib32-ncurses",
    "lib32-openal",
    "lib32-opencl-icd-loader",
    "lib32-opencl-mesa",
    "lib32-pipewire",
    "lib32-pipewire-jack",
    "lib32-v4l-utils",
    "lib32-vkd3d",
    "lib32-vulkan-icd-loader",
    "lib32-vulkan-mesa-layers",
    "lib32-vulkan-radeon",
    "lib32-vulkan-radeon",
    "libclc",
    "libdrm",
    "libelf",
    "libfido2",
    "libglvnd",
    "libjpeg-turbo",
    "libldap",
    "libnotify",
    "libomxil-bellagio",
    "libpng",
    "libpulse",
    "libreoffice-fresh",
    "libunwind",
    "libusb-compat",
    "libva",
    "libva-mesa-driver",
    "libva-utils",
    "libva-vdpau-driver",
    "libvdpau",
    "libx11",
    "libxcomposite",
    "libxdamage",
    "libxinerama",
    "libxml2",
    "libxrandr",
    "libxshmfence",
    "libxslt",
    "libxxf86vm",
    "linux",
    "linux-atm",
    "linux-firmware",
    "linux-firmware-marvell",
    "linux-headers",
    "livecd-sounds",
    "llvm",
    "llvm-libs",
    "lm_sensors",
    "lsscsi",
    "lutris",
    "lvm2",
    "lynx",
    "make",
    "man-db",
    "man-pages",
    "mc",
    "mdadm",
    "memtest86+",
    "mesa",
    "mesa-utils",
    "mesa-vdpau",
    "meson",
    "mkinitcpio",
    "mkinitcpio-archiso",
    "mkinitcpio-nfs-utils",
    "modemmanager",
    "mokutil",
    "mpg123",
    "mtools",
    "nano",
    "nbd",
    "ncurses",
    "ndisc6",
    "neofetch",
    "net-tools",
    "networkmanager",
    "nfs-utils",
    "nftables",
    "nilfs-utils",
    "nitrogen",
    "nmap",
    "nm-connection-editor",
    "noto-fonts",
    "noto-fonts-cjk",
    "noto-fonts-emoji",
    "noto-fonts-extra",
    "ntfs-3g",
    "ntfsprogs",
    "ntp",
    "nullmailer",
    "nvme-cli",
    "openal",
    "opencl-icd-loader",
    "opencl-mesa",
    "openconnect",
    "opengl-man-pages",
    "open-iscsi",
    "openjdk-doc",
    "openjdk-src",
    "openssh",
    "open-vm-tools",
    "openvpn",
    "os-prober",
    "partclone",
    "parted",
    "partimage",
    "pcsclite",
    "pipewire",
    "pipewire-alsa",
    "pipewire-jack",
    "pipewire-pulse",
    "polkit-gnome",
    "power-profiles-daemon",
    "ppp",
    "pptpclient",
    "pv",
    "python-gobject",
    "python-mako",
    "python-pyqt6",
    "qemu-guest-agent",
    "qt6",
    "qt6-imageformats",
    "qt6-multimedia-ffmpeg",
    "qt6-wayland",
    "refind",
    "reflector",
    "reiserfsprogs",
    "rp-pppoe",
    "rsync",
    "rxvt-unicode-terminfo",
    "samba",
    "sbctl",
    "sbsigntools",
    "screen",
    "sdparm",
    "sg3_utils",
    "shellcheck",
    "shotwell",
    "smartmontools",
    "sof-firmware",
    "squashfs-tools",
    "steam",
    "sudo",
    "syslinux",
    "systemd",
    "systemd-resolvconf",
    "tcpdump",
    "terminus-font",
    "tesseract-data-eng",
    "testdisk",
    "texinfo",
    "tmux",
    "tpm2-tss",
    "ttf-liberation",
    "ttf-ms-fonts",
    "ttf-vista-fonts",
    "udev",
    "udftools",
    "ufw",
    "unrar",
    "unzip",
    "usb_modeswitch",
    "usbmuxd",
    "usbutils",
    "v4l-utils",
    "valgrind",
    "vim",
    "virtualbox",
    "virtualbox-guest-utils",
    "virtualbox-host-modules-arch",
    "vkd3d",
    "vlc",
    "vpnc",
    "vulkan-icd-loader",
    "vulkan-mesa-layers",
    "vulkan-radeon",
    "w3m",
    "wine",
    "wine-gecko",
    "wine-mono",
    "winetricks",
    "wireless-regdb",
    "wireless_tools",
    "wireplumber",
    "wpa_supplicant",
    "wvdial",
    "xdg-utils",
    "xf86-video-amdgpu",
    "xfsprogs",
    "xl2tpd",
    "xorg",
    "xorg-apps",
    "xorgproto",
    "xorg-server",
    "xorg-xwayland",
    "xreader",
    "yay",
    "zenity",
    "zsh",
    "zstd",
    "gnome-disk-utility",
]

__supported__ = [
	"gnome",
	"kde",
	"awesome",
	"sway",
	"cinnamon",
	"xfce4",
	"lxqt",
	"i3",
	"bspwm",
	"budgie",
	"mate",
	"deepin",
	"enlightenment",
	"qtile"
]


def _prep_function(*args, **kwargs) -> bool:
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it"s a safe way to ask the user
	for more input before any other installer steps start.
	"""
	choice = Menu(str(_("Select your desired desktop environment")), __supported__).run()

	if choice.type_ != MenuSelectionType.Selection:
		return False

	if choice.value:
		# Temporarily store the selected desktop profile
		# in a session-safe location, since this module will get reloaded
		# the next time it gets executed.
		if not coffeebrewer.storage.get("_desktop_profile", None):
			coffeebrewer.storage["_desktop_profile"] = choice.value
		if not coffeebrewer.arguments.get("desktop-environment", None):
			coffeebrewer.arguments["desktop-environment"] = choice.value
		profile = coffeebrewer.Profile(None, choice.value)
		# Loading the instructions with a custom namespace, ensures that a __name__ comparison is never triggered.
		with profile.load_instructions(namespace=f"{choice.value}.py") as imported:
			if hasattr(imported, "_prep_function"):
				return imported._prep_function()
			else:
				log(f"Deprecated (??): {choice.value} profile has no _prep_function() anymore")
				exit(1)

	return False


if __name__ == "desktop":
	"""
	This "profile" is a meta-profile.
	There are no desktop-specific steps, it simply routes
	the installer to whichever desktop environment/window manager was chosen.

	Maybe in the future, a network manager or similar things *could* be added here.
	We should honor that Arch Linux does not officially endorse a desktop-setup, nor is
	it trying to be a turn-key desktop distribution.

	There are plenty of desktop-turn-key-solutions based on Arch Linux,
	this is therefore just a helper to get started
	"""

	# Install common packages for all desktop environments
	coffeebrewer.storage["installation_session"].add_additional_packages(__packages__)
    coffeebrewer.storage["installation_session"].add_additional_packages(__coffeepackages__)
    coffeebrewer.storage['installation_session'].add_additional_packages_yay(__yaypackages__)

	coffeebrewer.storage["installation_session"].install_profile(coffeebrewer.storage["_desktop_profile"])
    coffeebrewer.storage['installation_session'].enable_service('apparmor')
    printf "%b1\n[Unit]\nDescription=VMware daemon\nRequires=vmware-usbarbitrator.service\nBefore=vmware-usbarbitrator.service\nAfter=network.target\n[Service]\nExecStart=/etc/init.d/vmware start\nExecStop=/etc/init.d/vmware stop\nPIDFile=/var/lock/subsys/vmware\nRemainAfterExit=yes\n[Install]\nWantedBy=multi-user.target\n" "$*" >> /mnt/etc/systemd/system/vmware.service
    printf "%b1\n[Unit]\nDescription=VMware USB Arbitrator\nRequires=vmware.service\n[Service]\nExecStart=/usr/bin/vmware-usbarbitrator\nExecStop=/usr/bin/vmware-usbarbitrator --kill\nRemainAfterExit=yes\n[Install]\nWantedBy=multi-user.target\n" "$*" >> /mnt/etc/systemd/system/vmware-usbarbitrator.service
    printf "%b\n[Unit]\nDescription=VMware Networks\nWants=vmware-networks-configuration.service\nAfter=vmware-networks-configuration.service\n[Service]\nType=forking\nExecStartPre=-/sbin/modprobe vmnet\nExecStart=/usr/bin/vmware-networks --start\nExecStop=/usr/bin/vmware-networks --stop\n[Install]\nWantedBy=multi-user.target\n" "$*" >> /mnt/etc/systemd/system/vmware-networks-server.service
    coffeebrewer.storage['installation_session'].enable_service('vmware')
    coffeebrewer.storage['installation_session'].enable_service('vmware-networks-server')
    coffeebrewer.storage['installation_session'].enable_service('vmware-usbarbitrator')
    coffeebrewer.storage['installation_session'].enable_service('snapd.apparmor')
    coffeebrewer.storage['installation_session'].enable_service('snapd')
    coffeebrewer.storage['installation_session'].enable_service('systemd-boot-update')
    coffeebrewer.storage['installation_session'].enable_service('dhcpcd')
    coffeebrewer.storage['installation_session'].enable_service('cronie')
    coffeebrewer.storage['installation_session'].enable_service('chronyd')
    coffeebrewer.storage['installation_session'].enable_service('NetworkManager')
    coffeebrewer.storage['installation_session'].enable_service('firewalld')
    coffeebrewer.storage['installation_session'].enable_service('pipewire')
    coffeebrewer.storage['installation_session'].enable_service('pipewire-pulse')
    coffeebrewer.storage['installation_session'].enable_service('wireplumber')

