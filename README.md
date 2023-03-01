# Coffee Linux v.20.1.2 "Tower"

We believe using your PC should be as easy as a sip of coffee, so we fixed it up to be that way for you. No guesswork, it just does what its supposed to do. So kick back, relax and enjoy your cup. (LiveISO Password/s = coffee)

The goal here with Coffee Linux is specifically to outpace Windows OS in as many ways as possible and prove once and for all Linux is the best choice OS nowdays. MS has fallen very far from its glory days of being an actual good OS, and it's okay.
Open-Source reigns king these days. Its time to take the crown officially.
Coffee.. shall pave the way to this reality.

CoffeeLinux is a spin of Arch, but has been made easy for anyone to install and use for nearly anything.
The idea here is to have everything ready for you right away. No updating after installation.
The whole OS is downloaded and preconfigured (default settings) piece by piece on demand by the installer so it is up to date immediately.

 NO Updates that take forever. No drivers to setup (in most cases), It simply works out of the box similar to Windows but less corporate "sign your privacy away mumbo jumbo", or any of the other ridiculous crap in the Windows License terms you have to agree to just to use the OS at all. My OS is just as easy to use, faster in most cases, less prone to failure, has no need to defrag EVER, is less exposed to virus/malware automatically, and best of all free and open-source for everyone.

This OS is NOT developed by a team of developers, or any company whatsoever. Just me (LiquidSmokeX64), cause I feel I should be the guy that lights the way to a better, more feature rich, faster, user choice based computing experience than even some more major Linux Distributions (ie:Ubuntu or Manjaro) provide. Somebody had to do it, might as well be me. They act like making an OS is hard, but thats a misconception too it seems. They make convoluted tools to do this, but.. why? A single shell script with commands in the correct order can do the exact same thing just less pretty about it. Its an installer.. pretty is not required lol. In many cases it is these "tools" that are actually sorta messed up and not installing things correctly leading to performance issues.
But more aggressively.. My goal is to outpace Windows. Gaming is the only area Windows can do better in vary few cases at this point, many games actually run better on Vulkan API as opposed to MS Direct X. You get more stability in trade for a few fps in most cases. Worth it. Turning on the SteamPlay compatibility options in Steams settings is not rocket science. (Sorry, bit of a rant there lol)

Note: Gnome, KDE and Cinnamon are the most polished out of the DEs, and recommended for the full Coffee Linux experience. Other DEs are included as options but may have unknown bugs / issues and are generally unsupported by Coffee Linux officially. Use at your own risk. These are simply to provide all possible choices for possible future improvements to them without a need for multiple isos.
(Installation speed is solely based on your network speed)

The installer itself is a handcrafted (POSIX compliant) shell script, not multiple files, only one single file, it does everything typically done via the typical oversized/overly complex installers (ie: calamares) used by literally all other Linux distributions.

It asks a few simple questions to customize the OS to your liking, then you just wait for the reboot. Everything is downloaded and installed on the system for the system.
Everything that really can be given a user choice has been. This is YOUR OS YOUR WAY. We have just made simpler to install with minimal hiccups as a "daily driver".

Notable Feature: Secure-Boot support is available to install on the OS [via SystemD-Bootloader ONLY] (however it does not boot the ISO itself in Secure-Boot mode)

(Simply turn on "Windows UEFI Mode" or similar in BIOS post-install of Secure-Boot enabled OS)

(You do need to enroll your generated .cer in the MOK manually post-install similar to Ubuntu, it is placed in /boot/ by default )

=========================================================================

Choice of almost any Desktop Environment and WMs (for non-DE lovers)

=========================================================================

Java, Wine, Protontricks, DXVK, Vulkan, Steam, Discord, Heroic (Epic/GOG) games Launcher, Lutris and Firefox setup.

Functional Grub2 System Settings module for KDE.

Calamares-Git ready in KDE due to specific deps requiring Plasma.

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

Lots of Themes and Wallpapers depending on your DE/WM.

Just use Etcher to write the iso to usb, and go. Easy-peezy.

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
