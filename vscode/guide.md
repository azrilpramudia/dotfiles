## Remove Chache on Dock Plank

```bash
rm ~/.config/plank/dock1/launchers/code.dockitem 2>/dev/null
rm ~/.config/plank/dock1/launchers/visual-studio-code.dockitem 2>/dev/null
```

## Verify code.desktop Launcher
```bash
ls ~/.local/share/applications/code.desktop
```

## Reload
```bash
xfdesktop --reload
```

## if not work, try to logout or reboot this device
