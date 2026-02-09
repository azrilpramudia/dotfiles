## remove chache on dock plank

rm ~/.config/plank/dock1/launchers/code.dockitem 2>/dev/null
rm ~/.config/plank/dock1/launchers/visual-studio-code.dockitem 2>/dev/null

## verify code.desktop launcher
ls ~/.local/share/applications/code.desktop

## reload
xfdesktop --reload

## if not work, try to logout or reboot this device 
