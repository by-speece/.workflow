# Packages install
sudo pacman -Syu terminus-font feh python base-devel go xdg-users-dirs zsh --no-confirm --needed
sudo pacman -Syu cmus syncthing vim odt2txt poppler ueberzug ffmpegthumbnailer highlight mediainfo --no-confirm --needed
sudo systemctl enable syncthing@$USER 
go env -w GOPATH=$HOME/.go
clear 
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
clear
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions\
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
#GLOW
echo Kompilowanie GLOW
cd ~/.workflow/to_compile/glow
go build
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
sh ~/.workflow/modules/universalbright/install/install.sh

#CZYSZCZENIE
echo Czyszczenie
clear
