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
    #Network Setup Begins
    while [ "$netcheck00" != "1" ] && [ "$netcheck00" != "2" ] && [ "$netcheck00" != "3" ]; do

    clear

    printf "%b" "\nWhat type of network do you have? (Default: 1)\n"
    printf "%b" "\n1 - Ethernet\n"
    printf "%b" "\n2 - Wifi\n"
    printf "%b" "\n3 - I have already connected to the internet\n"
    read -r netcheck00
    case $netcheck00 in
     1) printf "%b" "\nPerfect\n" ;;
     2) printf "%b" "\nLet's move on then.\n" ;;
     3) printf "%b" "\nLet's move on then.\n" ;;
     *) printf "%b" "\nUnrecognized option, selecting default..\n" ;;
    esac

    if [ "$netcheck00" = "1" ]; then
    netpass00=ethernet
    fi
    if [ "$netcheck00" = "2" ]; then
    netpass00=wifi
    fi
    if [ "$netcheck00" = "3" ]; then
    netpass00=ethernet
    fi
    if [ "$netcheck00" != "3" ] && [ "$netcheck00" != "2" ] && [ "$netcheck00" != "1" ]; then
    netcheck00=3
    netpass00=ethernet
    fi
    done

    clear

    if [ "$netpass00" = "ethernet" ]; then
    printf "%b" "\nEthernet selected, or already connected, skipping this part.\n"
    fi
    if [ "$netpass00" = "wifi" ]; then
    while [ "$wifipasscheck" != "1" ]; do
    clear

    rfkill unblock all
    iwctl station list
    printf "%b" "\nSet your Wifi device ID. (Usually 'wlan0')\n"
    read -r wifi00
    wifi0=$wifi00
    printf "%b" "\n$wifi00. Is this correct?\n"
    printf "%b" "\n1 - yes\n"
    printf "%b" "\n2 - no\n"
    read -r wifipasscheck
    case $wifipasscheck in
     1) printf "%b" "\nPerfect\n" ;;
     *) printf "%b" "\nLet's retry\n" ;;
    esac

    done
    fi

    clear

    if [ "$netpass00" = "ethernet" ]; then
    printf "%b" "\nNo Wifi, skipping this part.\n"
    fi

    if [ "$netpass00" = "wifi" ]; then
    while [ "$ssidcheck" != "1" ]; do
    iwctl station "$wifi0" get-networks
    printf "%b" "\nSet your Network SSID (Your network name).\n"
    read -r ssid00
    ssid0=$ssid00
    printf "%b" "\n$ssid00. Is this correct?\n"
    printf "%b" "\n1 - yes\n"
    printf "%b" "\n2 - no\n"
    read -r ssidcheck
    case $ssidcheck in
     1) printf "%b" "\nPerfect\n" ;;
     *) printf "%b" "\nLet's retry\n" ;;
    esac
    done
    fi

    clear

    if [ "$netpass00" = "ethernet" ]; then
    printf "%b" "\nNo Wifi, skipping this part.\n"
    fi

    if [ "$netpass00" = "wifi" ]; then
    while [ "$netpasswordcheck" != "1" ]; do
    printf "%b" "\nEnter your Wifi password.\n"
    read -r netpassword00
    netpassword0=$netpassword00
    printf "%b" "\n$netpassword00. Is this correct?\n"
    printf "%b" "\n1 - yes\n"
    printf "%b" "\n2 - no\n"
    read -r netpasswordcheck
    case $netpasswordcheck in
     1) printf "%b" "\nPerfect\n" ;;
     *) printf "%b" "\nLet's retry\n" ;;
    esac
    done
    fi

    networkready="yes"

    while [ "$command17finished" != "1" ]; do
    if [ "$networkready" = "yes" ]; then
    #- Set variables for iwctl
    clear
    if [ "$netpass00" = "wifi" ]; then
    rfkill unblock all
    printf "%b" "\n" | iwctl device $wifi0 set-property Powered on
    printf "%b" "\nPowering on wifi device for a minute..\n"
    sleep 5
    printf "%b" "\n" | iwctl --passphrase $netpassword0 station $wifi0 connect $ssid0
    printf "%b" "\nEnsuring we have a connection...\n"
    sleep 10
    printf "%b" "\nSetting intial pacman keyring up...\n"
    pacman-key --init
    pacman-key --populate archlinux
    printf "%b" "\nSet keys successfully..\n"
    sleep 5
    pacman -Syy --noconfirm archlinux-keyring
    else
    printf "%b" "\nWe are already connected to the internet, preparing for launch..\n"
    sleep 10
    printf "%b" "\nSetting intial local pacman keyring up...\n"
    pacman-key --init
    pacman-key --populate archlinux
    printf "%b" "\nSet local pacman keys successfully..\n"
    sleep 5
    pacman -Syy --noconfirm archlinux-keyring
    clear
    fi
    fi
    command17finished="1"
    done
    command17finished="0"
    #Network Setup Finished
    #Update Needed Files
    rm /opt/os-release
    rm /opt/lsb-release
    rm /etc/os-release
    rm /etc/lsb-release
    rm /usr/local/bin/coffeebrewer-custom
    rm /usr/local/bin/coffeebrewer-cinnamon
    rm /usr/local/bin/coffeebrewer-kde
    rm /usr/local/bin/coffeebrewer-gnome
    rm /usr/local/bin/coffeebrewer-sway
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/coffeebrewer-custom -P /usr/local/bin/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/coffeebrewer-kde -P /usr/local/bin/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/coffeebrewer-cinnamon -P /usr/local/bin/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/coffeebrewer-gnome -P /usr/local/bin/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/coffeebrewer-sway -P /usr/local/bin/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/os-release -P /opt/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/lsb-release -P /opt/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/os-release -P /etc/
    clear
    wget -L https://raw.githubusercontent.com/LiquidSmokeX64/coffee/master/coffeelinux-archiso%20mod/releng/airootfs/opt/lsb-release -P /etc/
    clear
    chmod 755 /usr/local/bin/coffeebrewer-custom
    chmod 755 /usr/local/bin/coffeebrewer-kde
    chmod 755 /usr/local/bin/coffeebrewer-gnome
    chmod 755 /usr/local/bin/coffeebrewer-cinnamon
    chmod 755 /usr/local/bin/coffeebrewer-sway
    clear
    #Finished Updating
    #Main Menu
    while [ "$typecheck00" != "1" ] && [ "$typecheck00" != "2" ]; do
    clear
    printf "%b" "\n#### Welcome to Coffee Linux ####\n"
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
