#Import 
import os
import pyfiglet

#Default
current = set()

#Shortcut
def clear():
  os.system('clear')
def Rinde():
    rinde = pyfiglet.figlet_format("pyRINDE v0.4", font = "slant")
    print(rinde)
    print("------------------------------------------------------------")
    print("Author: Szymon 'by-speece' Gałka 2020-2021")
    print("Codename: Fresh May | Build 22052021 | Version:0.5.4-testing")
    print("------------------------------------------------------------")
def GlobalMenu():
    print("------------------------------------------------------------")
    print("b | Back to Main Menu")
    print("q | Quit")
    print("------------------------------------------------------------")

#Code of Program
def Main(): #Main Code of Program
    clear()
    Rinde()
    print("1 | Package Manager")
    print("2 | Install Apps with Configs")
    print("3 | Extra Scripts")
    print("4 | Rinde Settings")
    print("5 | Power Manager")
    print("6 | Android USB Install")
    GlobalMenu()

    MainInput = input("Command: ")
    if MainInput == "1": #Package Manager
        clear()
        Rinde()
        print("# | Packages Manager  ")
        print("1 | Full Update | Pacman + Yay")
        print("2 | Full Update | Pacman")        
        print("3 | Fast Update | Pacman")
        print("4 | Fast Update | Yay")
        PackageInput = input("Command: ")
        if PackageInput == "1": #Full Update | Pacman + Yay
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            os.system('sudo pacman -Sc --noconfirm')
            os.system('sudo pacman -Rs $(pacman -Qtdq) --noconfirm')
            os.system('yay -Syu --noconfirm')
            os.system('yay -Rs $(yay -Qtdq) --noconfirm')
            Main()
        if PackageInput == "2": #Full Update | Pacman
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            os.system('sudo pacman -Sc --noconfirm')
            os.system('sudo pacman -Rs $(pacman -Qtdq) --noconfirm')
            Main()
        if PackageInput == "3": #Fast Update | Pacman
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            Main()
        if PackageInput == "4": #Fast Update | Yay
            os.system('yay -Syu --noconfirm')
            Main()
        if PackageInput == "b": #Back to Main Menu
            Main()
        if PackageInput == "q": #Quit
            exit()
        else: 
            Main()
    if MainInput == "2": #Install apps with configs
        clear()
    if MainInput == "3": #Extra Scripts
        clear()
    if MainInput == "4": #Rinde Settings
        clear()
        Rinde()
        print("# | Rinde Settings Menu ")
        print("1 | Packages Pack")
        print("2 | Drivers Pack")
        print("3 | Install Rice")
        print("4 | Install Yay-bin")
        GlobalMenu()
        RindeInput = input("Command: ")
        if RindeInput == "1": #Packages Pack
            clear()
            Rinde()
        if RindeInput == "2": #Drivers Pack
            clear()
            Rinde()
        if RindeInput == "3": #Install Rice
            os.system('sudo pacman -Syu i3-gaps cups cups-pdf avahi gutenprint foomatic-db-gutenprint-ppds papirus-icon-theme wget curl libreoffice-fresh libreoffice-fresh-pl gedit repose zsh firefox thunderbird mpv youtube-dl discord calibre audacity screenkey obs-studio scribus krita rawtherapee htop gtop adapta-gtk-theme syncthing blueman bluez pavucontrol nautilus keepassxc dunst gnome-screenshot udiskie feh alacritty neofetch inkscape gimp xdotool light ttf-bitstream-vera ttf-croscore ttf-dejavu gnu-free-fonts adobe-source-han-sans-jp-fonts  adobe-source-han-serif-jp-fonts otf-ipafont ttf-hanazono ranger lxappearance-gtk3 --needed')
            os.system('yay -S polybar brother-dcpj315w brscan3 clipit cava i3lock-color libinput-gestures picom-git pyinstaller siji-git teams termsyn-font ttf-material-icons-git ttf-ms-fonts waifu2x-ncnn-vulkan-git wd719x-firmware xava-git --needed')
            os.system('cp -rf ~/.pyRinde/Data/Rice/ ~/.config/')
            os.system('mkdir ~/.pyrinde-user')
            os.system('cp -rf ~/.pyRinde/Data/pyrinde-user-template/ ~/.pyrinde-user/')
            os.system('sudo chmod +s /usr/bin/light')
            clear()
            Rinde()
        if RindeInput == "4": #Install Yay-bin
            os.system('sh Data/Bash/yay-bin.sh')
            clear()
            Rinde()
        if RindeInput == "b": #Back to Main Menu
            Main()
        if RindeInput == "q": #Quit
            exit()
    if MainInput == "5": #Power Manager
        clear()
    if MainInput == "6": #Android USB Install
        clear()
    if MainInput == "b": #Classic Function
        Main()
    if MainInput == "q": #Classic Function
        exit()
    else: #User is just idiot 
        Main()


Main() #Start
