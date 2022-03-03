#STANDARD PROGRAMS
sudo pacman -Syu diffutils dosfstools gptfdisk mc ntfs-3g ntp openssh parted gparted rsync sudo usbutils nano vim wget git udftools --needed  --no-confirm
#SOUND
sudo pacman -S pulseaudio pulseaudio-alsa pamixer paprefs alsa alsa-utils alsa-firmware sof-firmware alsa-ucm-conf alsa-lib alsa-plugins libcanberra libcanberra-pulse --needed --no-confirm
#DISPLAY
sudo pacman -S xorg-server xf86-input-evdev xf86-video-vesa xorg-xinit xorg-apps --needed --no-confirm
#NETWORK
sudo pacman -S net-tools networkmanager network-manager-applet --needed --no-confirm
sudo systemctl enable NetworkManager 

