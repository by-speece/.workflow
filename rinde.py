import os
import pyfiglet

current = set()

def clear():
  os.system('clear')

def Rinde():
    rinde = pyfiglet.figlet_format("RINDE v0.4", font = "slant")
    print(rinde)
    print("---------------------------------------------------------")
    print("Author: Szymon 'by-speece' Gałka 2020-2021")
    print("Codename: Fresh May | Build 03052021 | Version:0.4-stable")
    print("---------------------------------------------------------")
def GlobalMenu():
    print("---------------------------------------------------------")
    print("b | Back to Main Menu")
    print("q | Quit")
    print("---------------------------------------------------------")

def Main():
    clear()
    Rinde()
    print("1 | Package Manager")
    print("2 | Install Apps with Configs")
    print("3 | Extra Scripts")
    print("4 | Rinde Settings")
    print("5 | Power Manager")
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
            clear()
            Rinde()
        if RindeInput == "4": #Install Yay-bin
            clear()
            Rinde()
        if RindeInput == "b": #Back to Main Menu
            Main()
        if RindeInput == "q": #Quit
            exit()
    if MainInput == "5": #Power Manager
        clear()
    if MainInput == "b":
        Main()
    if MainInput == "q":
        exit()
    else:
        Main()
Main()
