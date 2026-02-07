#!/usr/bin/env bash

set -e

echo "== Dotfiles installer starting =="

DOTFILES="$HOME/dotfiles"

# --------- Backup Function ----------
backup () {
    if [ -e "$1" ] || [ -L "$1" ]; then
        echo "Backing up $1 -> $1.bak"
        mv "$1" "$1.bak"
    fi
}

# --------- Kitty ----------
echo "Installing kitty config..."
mkdir -p ~/.config/kitty
backup ~/.config/kitty/kitty.conf
ln -sf "$DOTFILES/kitty/kitty.conf" ~/.config/kitty/kitty.conf

# --------- Nano ----------
echo "Installing nano config..."
backup ~/.nanorc
ln -sf "$DOTFILES/nano/.nanorc" ~/.nanorc

# --------- Bash ----------
echo "Installing bash config..."
backup ~/.bashrc
ln -sf "$DOTFILES/bash/.bashrc" ~/.bashrc

# --------- Useful packages ----------
echo "Installing essential packages..."
sudo apt update
sudo apt install -y \
    fastfetch \
    eza \
    btop \
    git \
    curl

# --------- Font cache ----------
echo "Refreshing font cache..."
fc-cache -fv > /dev/null 2>&1

# --------- Reload shell ----------
echo "Reloading bash..."
source ~/.bashrc

echo "== Installation complete! Restart terminal =="

