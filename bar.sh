while true; do 
	xsetroot -name "[Lid: $(cat /sys/class/backlight/amdgpu_bl0/brightness)][Wifi:$(cat /sys/class/net/wlp2s0/operstate)][Sound $(amixer get Master | awk -F '[][]' 'END{ print $4":"$2 }')][BAT:$(cat /sys/class/power_supply/BAT0/status) | $(cat /sys/class/power_supply/BAT0/capacity)%][$(uname -r)][$(date)]"
	sleep 1
done
