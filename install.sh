# Packages install
sudo pacman -Syu terminus-font feh python base-devel go cmus --no-confirm --needed
clear
# Copy dotfiles
cp -rf ~/.workflow/dotfiles/. ~/
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
sudo rm -rf ~/go
clear
