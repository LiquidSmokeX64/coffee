# Koffee Linux v.17.0.0 "Quark"

![Screenshot_20221209_223429](https://user-images.githubusercontent.com/8603363/206835846-3e6e3eab-7632-471e-8a88-d2ffb548faa9.png)

We believe using your PC should be as easy as a sip of coffee, so we fixed it up to be that way for you. No guesswork, it just does what its supposed to do. So kick back, relax and enjoy your cup.

CoffeeLinux is a spin of Arch, but has been made easy for anyone to install and use for nearly anything. 
The idea here is to have everything ready for you right away.

It asks a few simple questions to customize the OS to your liking, then you just wait for the reboot. Everything is downloaded and installed on the system for the system. 
Everything that really can be given a user choice has been. This is still YOUR OS YOUR WAY. We have just made simpler to install with minimal hiccups.

Notable Feature: Secure-Boot support is available to install on the OS [via SystemD-Bootloader ONLY] (however it does not boot the ISO itself in Secure-Boot mode)

(Simply turn on "Windows UEFI Mode" or similar in BIOS post-install of Secure-Boot enabled OS)

(You do need to enroll your generated .cer in the MOK manually post-install similar to Ubuntu, it is placed in /boot/ by default )

=========================================================================

KDE Desktop Environment and Sway WM (for non-DE lovers)

All password/s for live environment are "coffee"

Install OS with the "(classic)" installer on the liveuser desktop.
(GUI installer is still EXPERIMENTAL, may still have some bugs)

=========================================================================

Java, Wine, Protontricks, DXVK, Vulkan, Steam, Discord, Heroic (Epic/GOG) games Launcher, Lutris and Firefox setup.

Ext4 and BTRFS options for compatibility with some hardware.

A ton of critical and optional dependencies resolved for most common packages.

Additional firmware from mkinitcpio-firmware to eliminate most default kernel module warnings.

Latest Controller and Graphics drivers (AMD/Nvidia).

Latest Linux Kernel and broad spectrum set of drivers.

Bluetooth Support.

Latest Gamescope and MangoHud.

Yay AUR package manager (Terminal only).

Sway settings GUI app. (Good to have) (sway-nvidia for nvidia gpus)

Pamac GUI Package Manager.

Snap-Store support (if selected)

VMware Workstation/Player (if selected)

SystemD-Bootloader UEFI w/secure-boot support 

Just use Etcher to write the iso to usb, and go. Easy-peezy.

=======================================================
Like, Share, and Enjoy. My Linux is the cure to the distro war.
=======================================================

To build your own iso:

Install archiso first.

Then open a terminal an issue the following commands.

git clone https://github.com/Project-X-Mods/coffeelinux-sources.git

sudo mkarchiso -v -w ~/work/ -o ~/out/ ~/coffeelinux-sources/releng/

Iso will be created in ~/out/ (home directory /out)

===============================================

Join us on Discord: https://discord.gg/6Pz43wP
We love hearing what you thing of our project, 
or have suggestions (polite ones)

===============================================

