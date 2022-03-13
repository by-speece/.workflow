sh ~/.workflow/modules/autostart/autorun-kill.sh
setxkbmap pl
feh --bg-scale ~/.workflow/feh/wallpaper.png
udiskie 2>&1 >/dev/null &
dunst 2>&1 >/dev/null &
systemctl --user import-enviroment DISPLAY
clipmenud &
sh ~/.workflow/modules/dwm-bar.sh
