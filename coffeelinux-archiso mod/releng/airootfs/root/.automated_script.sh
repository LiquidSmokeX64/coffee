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
    while [ "$typecheck00" != "1" ] && [ "$typecheck00" != "2" ] && [ "$typecheck00" != "3" ] && [ "$typecheck00" != "4" ]; do
    clear
    printf "%b" "\nWhat type of installation do you want? (Default: 1)\n"
    printf "%b" "\n1 - KDE\n"
    printf "%b" "\n2 - Gnome\n"
    printf "%b" "\n3 - Cinnamon\n"
    printf "%b" "\n4 - Custom\n"

    read -r typecheck00
    case $typecheck00 in
     1) printf "%b" "\nPerfect\n" ;;
     2) printf "%b" "\nLet's move on then.\n" ;;
     3) printf "%b" "\nPerfect\n" ;;
     4) printf "%b" "\nLet's move on then.\n" ;;
     *) printf "%b" "\nUnrecognized option, selecting default..\n" ;;
    esac

    if [ "$typecheck00" = "1" ]; then
    coffeebrewer3-kde
    fi
    if [ "$typecheck00" = "2" ]; then
    coffeebrewer3-gnome
    fi
    if [ "$typecheck00" = "3" ]; then
    coffeebrewer3-cinnamon
    fi
    if [ "$typecheck00" = "4" ]; then
    coffeebrewer2
    fi
    if [ "$typecheck00" != "1" ] && [ "$typecheck00" != "2" ] && [ "$typecheck00" != "3" ] && [ "$typecheck00" != "4" ]; then
    typecheck00=1
    coffeebrewer3-kde
    fi
    done
fi
