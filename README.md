# Coffee Linux v.23.7.1 "Winey"

What is CoffeeLinux?

Effectively it's pure Arch Linux with a different type of Installer.

The standard installation script for a standard Arch Linux is kinda broken, and incomplete to assembe an actually functional environment.

Coffee Linux aims to correct this problem through a much simpler script that assembles the OS via a series of questions to cater to exactly what you want.

The entire installation process features a default setup in case one just wants to hit "Enter" a few times and be done.

With Coffee Linux there is no longer any confusing guides to follow, no need to use a forked distro like Manjaro. You can have real Arch Linux, don't settle for second best.

Coffee Linux provides a full set of packages for every desktop environment, and a series of quality of life improvements via the Coffee Linux Extras.

Coffee Linux extras include many dependencies for a ton of everday applications, firmware patches, and other little things to make your experience the best I can provide out of the box.

There are a list of optional applications and services as well to choose from such as Steam, Java, LibreOffice, VMWare, Snapd framework, Heroic Games Launcher, Lutris, Github Desktop, and a few popular Web Browsers.

The idea here is to bring real Arch Linux to everyone, and effectively end the need for a distro war.

Everyone knows Arch is king under Gentoo, it's just confusing to install in a similar way. I've fixed that problem. Enjoy.

Stop settling for hackjob distros. You're better than that aren't you?

[Features List]

Pure Arch Linux not a fork (this is a feature)

Single file only installer script (this is a feature)

Web Browser Choices: Chrome, Firefox, and MS Edge

App Choices: Snapd framework, Steam, Java, VMWare, Discord, Github Desktop, Heroic Games, Lutris, and LibreOffice.

GPU Driver Choices: AMD, Nvidia, and Intel (Intel is still WIP because I do not own an ARC GPU)

Bootloader Choices: Grub UEFI, Grub BIOS, and Systemd-Boot (with optional Secure-boot)

Desktop Environment Choices: Gnome, KDE, Cinnamon, Mate, XFCE, LXQT, LXDE, i3, Sway, Cutefish, Deepin, Budgie, Enlightenment, and Awesome. (Some have styled versions to choose from as well)

Simply download from the Releases page and use Etcher to write the iso to usb. Use like any other ArchIso.

============================================

Known issues...

RTW8852BE Wifi adapter may not work. [Found in many Lenovo Laptops] (lwfinger rtw89 packages added, but seems ineffective so far)

============================================

Like, Share, and Enjoy. My Linux is the cure to the distro war.

============================================

To build your own iso:

Install archiso first.

Then open a terminal and issue the following commands.

git clone https://github.com/Project-X-Mods/coffeelinux.git

sudo mkarchiso -v -w ~/work/ -o ~/out/ ~/coffeelinux/releng/

Iso will be created in ~/out/ (home directory /out)

===============================================

Join us on Discord: https://discord.gg/6Pz43wP

We love hearing what you think of our project, 
or have suggestions (polite ones)

Donations accepted to keep our project alive and well.

Paypal: paypal.me/DanMaxie

CashApp: $FahrWander

===============================================


