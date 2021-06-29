cd ~
sudo pacman -S git base-devel --needed
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ~
rm -rf yay