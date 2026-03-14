<div align="center">
<img src="/assets/penguin.webp" width="200" alt="Dotfiles Banner">
<br>

![Linux](https://img.shields.io/badge/Linux-Dotfiles-3E8BC3?style=flat&logo=linux&logoColor=white)
![Kitty](https://img.shields.io/badge/Kitty-Terminal-D18692?style=flat&logo=kitty&logoColor=white)
![Tmux](https://img.shields.io/badge/Tmux-3.6a-00ad00?style=flat&logo=tmux&logoColor=white)
![Fastfetch](https://img.shields.io/badge/Fastfetch-System-f5c2e7?style=flat&logo=linux&logoColor=white)
![Vim](https://img.shields.io/badge/Editor-Vim-019733?style=flat&logo=vim&logoColor=white)

</div>

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
├── assets/      # Images and assets
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
git clone https://github.com/azrilpramudia/dotfiles.git
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

```bash
sudo apt install \
  neovim \
  tmux \
  kitty \
  fastfetch \
  nano \
  picom
```

For Neovim clipboard and CoC support:

```bash
# Clipboard support
sudo apt install xclip xsel

# Node.js & NPM (required by CoC.nvim)
sudo apt install nodejs npm
```

---

# Neovim Setup

Neovim uses **vim-plug** as the plugin manager.

### Install vim-plug

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

### Install Plugins

Open Neovim and run:

```vim
:PlugInstall
```

### Plugins Used

| Plugin | Category | Description |
|--------|----------|-------------|
| `catppuccin/vim` | UI | Catppuccin color theme |
| `vim-airline/vim-airline` | UI | Informative status bar |
| `ryanoasis/vim-devicons` | UI | File icons (requires Nerd Font) |
| `preservim/nerdtree` | Navigation | Sidebar file explorer |
| `junegunn/fzf` | Navigation | Fuzzy file finder |
| `iamcco/markdown-preview.nvim` | Tools | Live Markdown preview in browser |
| `neoclide/coc.nvim` | Tools | Auto-completion & LSP support |
| `sheerun/vim-polyglot` | Tools | Syntax highlighting for many languages |
| `jiangmiao/auto-pairs` | Tools | Auto close brackets and quotes |
| `airblade/vim-gitgutter` | Tools | Git diff indicators in the gutter |

### Install CoC Extensions

```vim
:CocInstall coc-html coc-css coc-tsserver coc-json coc-prettier coc-emmet
```

### Nerd Font

`vim-devicons` requires a Nerd Font to display icons correctly. Install FiraCode Nerd Font:

```bash
sudo apt install fonts-firacode
```

Or download from [nerdfonts.com](https://www.nerdfonts.com/) and set it in your terminal emulator.

More documentation: [**vim/neovim guide**](docs/neovim-guide.md)

---

# Customization

You can modify any configuration inside the folders.

| File | Description |
|------|-------------|
| `kitty/kitty.conf` | Terminal appearance and behavior |
| `tmux/tmux.conf` | Tmux keybindings and layout |
| `vim/init.vim` | Neovim plugins and settings |
| `fastfetch/config.jsonc` | System info display |
| `bash/.bashrc` | Shell aliases and environment |

---

# Troubleshooting

### Garbled escape codes on Vim startup (Kitty terminal)

If you see random escape characters when opening Vim with Kitty terminal, add this to `~/.config/kitty/kitty.conf`:

```bash
# Force Vim-compatible TERM value
term xterm-256color
```

Then restart Kitty. This fixes the conflict between `xterm-kitty` and Vim's `termguicolors`.

Alternatively, add this to your `.vimrc` before `set termguicolors`:

```vim
if exists('+termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif
```

### Icons not showing correctly

Make sure a Nerd Font is installed and set as the font in your terminal emulator. Without it, `vim-devicons` will display broken characters instead of icons.

### CoC not working

Ensure `nodejs` and `npm` are installed:

```bash
node --version
npm --version
```

If not installed, run `sudo apt install nodejs npm` and restart Neovim.

---

# Why Dotfiles?

Using dotfiles makes it easy to:

- Reproduce your development environment on any machine
- Keep configs version controlled with Git
- Migrate your full setup to a new system quickly

---

# Future Improvements

- Screenshots of the setup
- More automation in `install.sh`
- Additional shell utilities
- Zsh configuration documentation

---

# License

This project is open-source and available under the **MIT License**.
