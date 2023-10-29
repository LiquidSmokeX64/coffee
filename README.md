# Coffee Linux v.23.1.7 "Verona"

I believe using your PC should be as easy as a sip of coffee, so I fixed it up to be that way for you. No guesswork, it just does what its supposed to do. So kick back, relax and enjoy your cup.

The goal here with Coffee Linux is specifically to be a gaming powerhouse OS, but is still perfectly capable of normal tasks as well.

CoffeeLinux is a spin of Arch, but has been made easy for anyone to install and use for nearly anything. 
The idea here is to have everything ready for you right away. No updating after installation.
The whole OS is downloaded and preconfigured (default settings) piece by piece on demand by the installer so it is up to date immediately.

Gnome and KDE are the only tested Desktop Environments, though many are available to try.
(Installation speed is solely based on your network speed)

The installer itself is a handcrafted shell script, not multiple files, only one single file, it does everything typically done via the typical oversized/overly complex installers (ie: calamares) used by literally all other Linux distributions. 

It asks a few simple questions to customize the OS to your liking, then you just wait for the reboot. Everything is downloaded and installed on the system for the system. 
Everything that really can be given a user choice has been. I have just made things simpler to install with minimal hiccups as a "daily driver".

Notable Feature: Secure-Boot support is available to install on the OS [via SystemD-Bootloader ONLY] (however it does not boot the ISO itself in Secure-Boot mode)

(Simply turn on "Windows UEFI Mode" or similar in BIOS post-install of Secure-Boot enabled OS)

(You do need to enroll your generated .cer in the MOK manually post-install similar to Ubuntu, it is placed in /boot/ by default )

Java, Wine, Protontricks, DXVK, Vulkan, Steam, Discord, Heroic (Epic/GOG) Games Launcher, Lutris and Firefox setup.

Ext4 and BTRFS options for compatibility with some hardware.

A ton of critical and optional dependencies resolved for most common packages.

Latest Graphics drivers for AMD or Nvidia.

Latest Linux Kernel and broad spectrum set of drivers.

Bluetooth Support.

Latest Gamescope & Mangohud from SteamOS.

Yay AUR package manager (Terminal only).

Pamac GUI Package Manager.

Snap-Store support (if selected)

VMware Workstation/Player (if selected)

Hibernation Support (if selected)

Grub bootloader (no secure-boot support) or SystemD-Bootloader UEFI w/secure-boot support 

Just use Etcher to write the iso to usb, and go. Easy-peezy
============================================
Known issues...
RTW8852BE Wifi adapter may not work. [Found in many Lenovo Laptops] (lwfinger rtw89 packages added, but seems ineffective so far)
============================================

Like, Share, and Enjoy. My Linux is the cure to the distro war.

============================================

To build your own iso:

Install archiso first.

Then open a terminal an issue the following commands.

git clone https://github.com/Project-X-Mods/coffeelinux.git

sudo mkarchiso -v -w ~/work/ -o ~/out/ ~/coffeelinux/releng/

Iso will be created in ~/out/ (home directory /out)

===============================================

Join us on Discord: https://discord.gg/6Pz43wP
We love hearing what you think of our project, 
or have suggestions (polite ones)

===============================================

