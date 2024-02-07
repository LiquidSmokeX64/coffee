#!/usr/bin/env bash

script_cmdline() {
    local param
    for param in $(</proc/cmdline); do
        case "${param}" in
            script=*)
                echo "${param#*=}"
                return 0
                ;;
        esac
    done
}

automated_script() {
    local script rt
    script="$(script_cmdline)"
    if [[ -n "${script}" && ! -x /tmp/startup_script ]]; then
        if [[ "${script}" =~ ^((http|https|ftp|tftp)://) ]]; then
            # there's no synchronization for network availability before executing this script
            printf '%s: waiting for network-online.target\n' "$0"
            until systemctl --quiet is-active network-online.target; do
                sleep 1
            done
            printf '%s: downloading %s\n' "$0" "${script}"
            curl "${script}" --location --retry-connrefused --retry 10 -s -o /tmp/startup_script
            rt=$?
        else
            cp "${script}" /tmp/startup_script
            rt=$?
        fi
        if [[ ${rt} -eq 0 ]]; then
            chmod +x /tmp/startup_script
            printf '%s: executing automated script\n' "$0"
            # note that script is executed when other services (like pacman-init) may be still in progress, please
            # synchronize to "systemctl is-system-running --wait" when your script depends on other services
            /tmp/startup_script
        fi
    fi
}

if [[ $(tty) == "/dev/tty1" ]]; then
    automated_script
    rfkill unblock all
    clear
    pacman-key --init
    clear
    pacman-key --populate archlinux
    clear
    while [ "$typecheck00" != "1" ] && [ "$typecheck00" != "2" ]; do
    clear
    printf "%b" "\n#### Welcome to Coffee Linux v.24.1.8 ####\n"
    printf "%b" "\n#### Warning: Some Non-Standard Desktop Environments may be Experimental ####\n"
    printf "%b" "\nWhat type of installation do you want? (Default: 1)\n"
    printf "%b" "\n1 - Standard\n"
    printf "%b" "\n2 - Custom\n"

    read -r typecheck00
    case $typecheck00 in
     1) printf "%b" "\nPerfect\n" ;;
     2) printf "%b" "\nLet's move on then.\n" ;;
     *) printf "%b" "\nUnrecognized option, selecting default..\n" ;;
    esac

    if [ "$typecheck00" = "1" ]; then

      while [ "$typecheck01" != "1" ] && [ "$typecheck01" != "2" ] && [ "$typecheck01" != "3" ] && [ "$typecheck01" != "4" ]; do
      clear
      printf "%b" "\nWhat type of Desktop Environment do you want?\n"
      printf "%b" "\n1 - KDE\n"
      printf "%b" "\n2 - Gnome\n"
      printf "%b" "\n3 - Cinnamon\n"
      printf "%b" "\n4 - Sway\n"
      read -r typecheck01
      case $typecheck01 in
       1) printf "%b" "\nPerfect\n" ;;
       2) printf "%b" "\nLet's move on then.\n" ;;
       3) printf "%b" "\nPerfect\n" ;;
       4) printf "%b" "\nLet's move on then.\n" ;;
       *) printf "%b" "\nUnrecognized option...\n" ;;
      esac
      if [ "$typecheck01" = "1" ]; then
      coffeebrewer-kde
      fi
      if [ "$typecheck01" = "2" ]; then
      coffeebrewer-gnome
      fi
      if [ "$typecheck01" = "3" ]; then
      coffeebrewer-cinnamon
      fi
      if [ "$typecheck01" = "4" ]; then
      coffeebrewer-sway
      fi
      done
    fi
    if [ "$typecheck00" = "2" ]; then
    coffeebrewer-custom
    fi
    if [ "$typecheck00" != "1" ] && [ "$typecheck00" != "2" ]; then
    typecheck00=2
    coffeebrewer-custom
    fi
    done
fi
