#Base Apps
sudo pacman -Syu i3-gaps fish alacritty thunderbird firefox --needed --noconfirm
#i3 config
sudo pacman -S dunst gnome-screenshot udiskie feh light signal-desktop rofi nautilus pavucontrol keepassxc --needed --noconfirm
#Music/Video
sudo pacman -S mpv youtube-dl cmus rhythmbox 
#Terminal Tools
sudo pacman -S wget curl repose screenkey htop gtop neofetch xdotool ranger --needed --noconfirm
#Mount devices
sudo pacman -S libimobiledevice gvfs gvfs-afc gvfs-gphoto2 gvfs-mtp gvfs-nfs gvfs-smb filemanager-actions--needed --noconfirm
#DTP/Graphic programs
sudo pacman -S gimp inkscape rawtherapee scribus --needed --noconfirm
#Another Stuff
sudo pacman -S libreoffice-fresh libreoffice-fresh-pl nano filezilla discord calibre audacity  obs-studio scribus keepassxc --needed --noconfirm
#GTK + QT tools
sudo pacman -S qt5ct papirus-icon-theme adapta-gtk-theme lxappearance gtk-chtheme breeze breeze-gtk kvantum-qt5  --needed --noconfirm
#Bluetooth + Printing + Syncthing 
sudo pacman -S blueman bluez bluez-utils cups cups-pdf avahi gutenprint foomatic-db-gutenprint-ppds syncthing --needed --noconfirm
#Fonts
sudo pacman -S ttf-bitstream-vera ttf-croscore ttf-dejavu gnu-free-fonts adobe-source-han-sans-jp-fonts adobe-source-han-serif-jp-fonts otf-ipafont ttf-hanazono --needed --noconfirm
#AUR apps
yay -Syu polybar clipit i3lock-color libinput-gestures picom-git siji-git termsyn-font ttf-material-icons-git ttf-ms-fonts wd719x-firmware sublime-music marktext-bin brother-dcpj315w brscan3 pyinstaller teams --needed --noconfirm
# Enable systemd service
sudo systemctl enable cups syncthing@$USER
sudo systemctl start cups syncthing@$USER