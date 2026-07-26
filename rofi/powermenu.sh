#!/usr/bin/env bash

chosen=$(printf "  Power Off\n  Reboot\n󰌾  Lock\n󰍃  Log Out" | rofi -dmenu -i -p "Power" -theme ~/.config/rofi/themes/catppuccin-mocha.rasi)

case "$chosen" in
    "  Power Off") systemctl poweroff ;;
    "  Reboot") systemctl reboot ;;
    "󰌾  Lock") xflock4 ;;
    "󰍃  Log Out") xfce4-session-logout --logout ;;
esac
