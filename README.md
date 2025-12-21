# Welcome to CoffeeLinux.
-----------------------------------

CoffeeLinux is a Linux distribution optimized for gaming, yet its performance extends to other areas as well, offering a noticeable improvement across the board.

Built on Arch, CoffeeLinux is designed to provide a streamlined, hassle-free installation process. From start to finish, the setup is simple, enabling users to begin their experience quickly and efficiently.

The installer is a lightweight, shell-based setup. We believe in a straightforward approach, foregoing unnecessary graphical interfaces in favor of a direct, efficient installation process. With just a few simple steps, you’ll be up and running in no time.

What sets CoffeeLinux apart from other distributions is its custom-crafted installer, a modified version of the Arch ISO (releng profile). This installer uses a single script to perform the entire installation based on your preferences, significantly reducing the need for copying packages from the installation medium. The installation process mirrors a manual Arch Linux setup, ensuring greater flexibility and control.

CoffeeLinux delivers the power of Arch with added ease and convenience. Join us and experience it for yourself.

However, it should be noted that gaming performance can vary depending on the Desktop Environment you choose. This is because each uses its own compositors, some game better than others.
Also the display rendering differences between Wayland or X11 play a factor to overall gaming horsepower.
Which is why CoffeeLinux provides a short list of some of the most popular DEs to choose from. If one doest suit you, try another, it might work better for your machine.

----------------------------------

**Features of CoffeeLinux:**

- **Command Line installation**:  Simple easy to use universal installer without all that flashy unneeded GUI to cause problems. (Trust me it's better this way.)

- **Zen Kernel**: A more focused kernel to get the most out of your gaming experience.

- **ZRAM Enabled**: A more modern, efficient alternative to the default ZSWAP, giving back that precious Hard Drive space for more of what you want instead.

- **QoL Packages**: Essential packages and dependencies, designed to optimize the experience across a wide range of applications and services. ie: Java, etc.

- **Wayland Focused**:  The software stack is built with Wayland functionality in mind (in most cases).

- **GPU Friendly**:  AMD or Nvidia GPUs welcome (Intel... maybe..)

- **Gaming Ready**:  Lutris, Wine, Steam, Heroic Games Launcher (Epic/GOG/Amazon), and Discord built in.

- **Gaming Tools**: DXVK-Bin, Winetricks, Protontricks, and ProtonUp-QT built in.

- **Installer Self-Updater**: Installer script, and misc files are auto-updated on the installation medium prior to use to always give the latest available version.

- **Bootloader Options**: Supports both **Grub UEFI** and **Grub BIOS** for flexible boot management.

- **Multiple Desktop Environment Choices**: 
   1. Cosmic. A very fast and unique Rust based environment by System 76. (Default)
   2. Gnome. Simple and modern interface from Gnome.org.
   3. Cinnamon. Sleek and stylish yet classic environment by Linux Mint.
   4. Plasma. A cutting edge, looks and customization forward environment from KDE Neon.
   5. Budgie. A gnome based environment featured in Solarus.
   6. XFCE. A superlightweight environment featured in Manjaro.

- **OS level fixes**: Some games and apps require extra push to get running so fixes have been integrated for this such as:
   1. **CPU Mitigations and SplitLock Detection Disabled**: Fixes stuttering with 13th Gen+ Intel CPUs, and some AMD CPUs as well.
   2. **VM Max Map Count Fix**: Prevents most CTDs in Horizon Zero Dawn Remastered, and helps with motion jitters in many games.
   3. **DotNet 4.8 Installation Fix**: Prevents some issues with Space Engineers, possibly any other titles that require it. (protontricks)
   4. **Nvidia Smooth Motion**: Globally enabled by default if selected. (Nvidia 40xx+ GPU required)

- **CoffeeLinux Manager (WIP)**: A console scripted application designed to simplify common tasks, including:
   1. **System Updater**: For distribution-specific updates.
   2. **Application manager**: Basic installing and removal of software.
   3. **System information**: Fastfetch Info.
   4. **Coffee ISO Maker**: Easily create updated CoffeeLinux ISOs.
   5. **Pacman Switcher**: Switch between stable and beta system update channels.
   6. **Steam Library Fixer**: Resolve Steam library links on secondary NTFS drives.
   7. **Discord Updater Tool**: Manually updates Discord app from official tar.gz file.

To get started, simply download the ISO from the *Releases* page, use Etcher to write it to a USB drive, and proceed as you would with any other Arch ISO installation.

**Known Potential Issues**
1. Updating via "pacman -Syu" command or through the Package Manager app on Cinnamon DE may break lightdm-slick-greeter. (Use the distro-specific updater in CoffeeLinux Manager)
2. Sometimes the ISO does not wipe the destination drive properly (automated fdisk/hardware bug).
3. Audio may be quieter than usual on some speakers / laptops.
4. Steam Client on Gnome with Nvidia GPUs may have mouse input issues.
5. Cosmic Desktop is still very new thus has some minor bugs it's developers need to resolve.
------------------------------------

Like, Share, and Enjoy. 
My Linux is the end of the distro war. It just needs some coffee to calm down.

------------------------------------

Join us on Discord: https://discord.gg/6Pz43wP

We love hearing what you think of our project, 
or have suggestions (polite ones)

Donations accepted to keep our project alive and well.

CashApp: $FahrWander

------------------------
