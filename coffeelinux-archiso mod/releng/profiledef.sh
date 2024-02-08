#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="coffeelinux"
iso_label="COFFEE_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="Coffee Linux <https://archlinux.org>"
iso_application="Coffee Linux Live/Rescue CD"
iso_version="24.3.8-$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
           'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
           'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/shadow"]="0:0:0400"
  ["/etc/gshadow"]="0:0:0400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/root/.gnupg"]="0:0:700"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/usr/local/bin/coffeebrewer-custom"]="0:0:755"
  ["/usr/local/bin/coffeebrewer-kde"]="0:0:755"
  ["/usr/local/bin/coffeebrewer-gnome"]="0:0:755"
  ["/usr/local/bin/coffeebrewer-cinnamon"]="0:0:755"
  ["/usr/local/bin/coffeebrewer-sway"]="0:0:755"
)
