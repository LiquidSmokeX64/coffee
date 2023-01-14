#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="coffeelinux"
iso_label="COFFEEISO_$(date +%Y%m)"
iso_publisher="Project X Mods"
iso_application="Coffee Linux Live/Rescue CD"
iso_version="Praxus-16.0.0-$(date +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
  ["/etc/group"]="0:0:400"
  ["/etc/os-release"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/usr/local/bin/coffeebrewer"]="0:0:755"
  ["/etc/skel/Desktop/coffeebrewer.desktop"]="0:0:755"
)
