# Linux Dotfiles

My personal **Linux customization and configuration files** for development and terminal workflow.

This repository contains configuration for several tools I use daily such as **zsh, neovim, tmux, kitty, fastfetch, and more**.

The goal of this repository is to keep my development environment **organized, reproducible, and easy to install on a new system**.

---

# Features

- Clean and simple terminal workflow
- Neovim configuration for coding
- Tmux setup for terminal multiplexing
- Kitty terminal customization
- Fastfetch system information display
- Bash utilities and scripts
- Nano configuration
- Fonts for terminal usage
- Picom configuration for compositing (XFCE)

---

# Repository Structure

```
dotfiles/
│
├── bash/        # Bash configuration and scripts
├── docs/        # Documentation and guides
├── fastfetch/   # Fastfetch configuration
├── fonts/       # Terminal fonts
├── kitty/       # Kitty terminal config
├── nano/        # Nano editor configuration
├── picom/       # Picom compositor config
├── tmux/        # Tmux configuration
├── vim/         # Vim / Neovim configuration
│
├── install.sh   # Setup script
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/dotfiles.git
cd dotfiles
```

Run the install script:

```bash
chmod +x install.sh
./install.sh
```

This script will automatically apply the configurations.

---

# Requirements

Some tools need to be installed before using these configs.

Example packages:

```bash
sudo apt install \
neovim \
tmux \
kitty \
fastfetch \
nano \
picom
```

---

# Neovim Setup

Neovim uses **vim-plug** as the plugin manager.

Install vim-plug:

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Then install plugins inside Neovim:

```
:PlugInstall
```

More documentation can be found in:

[**vim/neovim documentation**](docs/vim-guide.md)

---

# Customization

You can modify any configuration inside the folders.

Example:

- `kitty/kitty.conf` → terminal appearance
- `tmux/tmux.conf` → tmux keybindings
- `vim/init.vim` → neovim configuration

---

# Why Dotfiles?

Using dotfiles makes it easy to:

- reproduce your development environment
- keep configs version controlled
- migrate setup to a new machine quickly

---

# Future Improvements

Planned improvements for this repository:

- Better documentation
- Screenshots of the setup
- More automation in `install.sh`
- Additional shell utilities

---

# License

This project is open-source and available under the **MIT License**.
