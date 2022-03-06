# Packages install
sudo pacman -Syu terminus-font feh python base-devel go xdg-users-dirs zsh --noconfirm
sudo pacman -Syu cmus syncthing vim odt2txt poppler w3m feh ranger ffmpegthumbnailer highlight mediainfo glow mpv --noconfirm 
sudo pacman -Syu noto-fonts-emoji
sudo systemctl enable syncthing@$USER 
clear 
# Copy dotfiles
cp -rf ~/.workflow/dotfiles/. ~/
source ~/.bashrc
source ~/.zshrc
clear
# Install universalbright
sh ~/.workflow/modules/universalbright
clear
# Compile tools
# DMENU
echo Kompilowanie DMENU
cd ~/.workflow/to_compile/dmenu
sudo make clean install
clear
#DWM
echo Kompilowanie DWM
cd ~/.workflow/to_compile/dwm
sudo make clean install
clear
#MDP
echo Kompilowanie MDP
cd ~/.workflow/to_compile/mdp
make 
sudo make install
clear
#SLOCK
echo Kompilowanie SLOCK
cd ~/.workflow/to_compile/slock
sudo make clean install
clear
#ST
echo Kompilowanie ST
cd ~/.workflow/to_compile/st
sudo make clean install
clear

#MODUŁY
#INSTALOWANIE UNIVERSALBRIGHT
echo instalowanie modyłów
sudo sh ~/.workflow/modules/universalbright/install/install.sh

#YAY
cd ~
git clone https://aur.archlinux.org/yay-bin.git
cd ~/yay-bin
makepkg -si

#CZYSZCZENIE
echo Czyszczenie
rm -rf ~/yay-bin
#INSTALL AUR PACKAGES
yay -S yt-dlp
clear

