# .pyRINDE
Python Rinde is not desktop Environment
Zbiór skryptów i konfiguracji narzędzi suckless, których używam na codzień.
# Pakiety:
- Terminus
- Feh 
- python



# Instalacja oh-my-zsh i autosuggestion

sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions\

Dodaj do .zshrc:

plugins=( zsh-autosuggestions)
