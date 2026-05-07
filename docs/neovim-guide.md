# Neovim / Vim Guide

A complete setup guide for **Neovim/Vim** on Linux — covering plugin installation, theme, keybindings, and a full `.vimrc` configuration.

---

## Table of Contents

1. [Installation](#1-installation)
2. [Plugins](#2-plugins)
3. [Appearance & Theme](#3-appearance--theme)
4. [Keybindings](#4-keybindings)
5. [Tab & Indentation](#5-tab--indentation)
6. [Additional Features](#6-additional-features)
7. [Web Development (CoC.nvim)](#7-web-development-cocnvim)
8. [Plugin Manager Commands](#8-plugin-manager-commands)
9. [Full Configuration](#9-full-configuration)
10. [Setup Workflow](#10-setup-workflow)
11. [References](#references)

---

## 1. Installation

### 1.1 Install Plugin Manager (vim-plug)

`vim-plug` is a fast and minimal plugin manager for Vim/Neovim.

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

### 1.2 Install System Dependencies

```bash
# Clipboard support
sudo apt install xclip xsel

# Node.js & NPM (required by CoC.nvim)
sudo apt install nodejs npm
```

### 1.3 Install Nerd Font

`vim-devicons` requires a Nerd Font to display icons correctly in the terminal.

```bash
# Example: install FiraCode Nerd Font
sudo apt install fonts-firacode
```

Or download manually from [nerdfonts.com](https://www.nerdfonts.com/) and set it in your terminal emulator.

---

## 2. Plugins

All plugins are declared between `call plug#begin()` and `call plug#end()` inside `.vimrc`.

```vim
call plug#begin()

" --- Theme & UI ---
Plug 'catppuccin/vim', { 'as': 'catppuccin' }        " Catppuccin color theme
Plug 'vim-airline/vim-airline'                        " Informative status bar
Plug 'ryanoasis/vim-devicons'                         " File icons (requires Nerd Font)

" --- Navigation ---
Plug 'preservim/nerdtree'                             " File explorer sidebar
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }  " Fuzzy file finder

" --- Tools ---
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() } }  " Markdown live preview
Plug 'neoclide/coc.nvim', {'branch': 'release'}       " Auto-completion engine
Plug 'sheerun/vim-polyglot'                           " Multi-language syntax highlighting
Plug 'jiangmiao/auto-pairs'                           " Auto close brackets & quotes
Plug 'airblade/vim-gitgutter'                         " Git diff indicators in the gutter

call plug#end()
```

### Plugin List

| Plugin | Category | Description |
|--------|----------|-------------|
| `catppuccin/vim` | UI | Catppuccin color theme |
| `vim-airline` | UI | Informative bottom status bar |
| `vim-devicons` | UI | File and folder icons |
| `preservim/nerdtree` | Navigation | Sidebar file explorer |
| `junegunn/fzf` | Navigation | Fuzzy file search |
| `markdown-preview.nvim` | Tools | Live Markdown preview in browser |
| `neoclide/coc.nvim` | Tools | Auto-completion & LSP support |
| `vim-polyglot` | Tools | Syntax highlighting for many languages |
| `auto-pairs` | Tools | Auto close `()`, `[]`, `{}`, `""` |
| `vim-gitgutter` | Tools | Show Git diff next to line numbers |

---

## 3. Appearance & Theme

### Catppuccin Variants

| Colorscheme | Style |
|---|---|
| `catppuccin_latte` | Light |
| `catppuccin_frappe` | Medium dark |
| `catppuccin_macchiato` | Dark (currently used) |
| `catppuccin_mocha` | Darkest |

### Display Configuration

```vim
" --- Basic View ---
syntax on            " Enable syntax highlighting
set number           " Show line numbers
set relativenumber   " Show relative line numbers from cursor
set cursorline       " Highlight the active line
set termguicolors    " Enable 24-bit RGB color
set fillchars=eob:-  " Replace '~' at end of buffer with '-'

" --- Colors ---
highlight LineNr        ctermfg=grey   guifg=#808080  " Line number color
highlight CursorLineNr  ctermfg=yellow guifg=#FFFF00  " Active line number color

" Apply theme
colorscheme catppuccin_macchiato
```

---

## 4. Keybindings

```vim
" --- Shortcuts ---

" Toggle NERDTree with Ctrl+N
nnoremap <C-n> :NERDTreeToggle<CR>
```

### Shortcut Reference (Keybindings)

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl + N` | `:NERDTreeToggle` | Open / close file explorer sidebar |
| `Ctrl + P` | `:Files` | Fuzzy find files (via fzf) |
| `Ctrl + G` | `:Rg` | Fuzzy Search word (via fzf) |
| `Ctrl + B` | `:Buffers` | Fuzzy Which Open Files |
| `Tab` | Autocomplete | Select suggestion in CoC menu |
| `Shift + K` | Documentation | Show docs for word under cursor |
| `<Leader> + f` | `coc-format-selected` | Format selected code / block |

---

### File Management & Commands

| Command | Action | Description |
|---------|--------|-------------|
| `:w` | Save | Save current file |
| `:w filename.js` | Save As | Save as a new file name |
| `:wa` | Save All | Save all opened buffers |
| `:wq` | Save & Quit | Save and exit Vim |
| `:w!` | Force Save | Force write (for read-only files) |
| `:q!` | Force Quit | Exit without saving changes |
| `:e filename.js` | Edit | Open/Edit a file in current window |
| `:new filename.js` | Horizontal Split | Open new file in horizontal split |
| `:vnew filename.js`| Vertical Split | Open new file in vertical split |
| `:!touch file.js` | Terminal Command | Run shell command to create file |
| `:Prettier` | Format | Run Prettier on entire document |

## 5. Tab & Indentation

```vim
" --- Tab & Indentation ---
set tabstop=4    " 1 tab = 4 spaces wide
set shiftwidth=4 " Indent width when using >> or <<
set expandtab    " Convert tabs to spaces
```

| Setting | Value | Description |
|---------|-------|-------------|
| `tabstop` | `4` | 1 tab character = 4 spaces |
| `shiftwidth` | `4` | Auto-indent width |
| `expandtab` | enabled | Tabs are converted to spaces on input |

---

## 6. Additional Features

```vim
" --- Additional Features ---
set mouse=a               " Enable mouse support in all modes
set clipboard=unnamedplus " Use system clipboard (requires xclip/xsel)
set ignorecase            " Case-insensitive search
set smartcase             " Case-sensitive if query contains uppercase
```

| Setting | Description |
|---------|-------------|
| `mouse=a` | Mouse enabled in normal, insert, and visual mode |
| `clipboard=unnamedplus` | Copy/paste synced with system clipboard |
| `ignorecase` | `/foo` matches `Foo`, `FOO`, etc. |
| `smartcase` | `/Foo` stays case-sensitive due to uppercase letter |

---

## 7. Web Development (CoC.nvim)

### Install Language Servers

Run the following inside Vim/Neovim after `:PlugInstall`:

```vim
:CocInstall coc-html coc-css coc-tsserver coc-json coc-prettier coc-emmet
```

### CoC Extensions

| Extension | Description |
|-----------|-------------|
| `coc-html` | Auto-complete & diagnostics for HTML |
| `coc-css` | Auto-complete for CSS / SCSS |
| `coc-tsserver` | IntelliSense for JavaScript & TypeScript |
| `coc-json` | JSON validation and formatting |
| `coc-prettier` | Auto-format via `:CocCommand prettier.formatFile` |
| `coc-emmet` | Snippet expansion, e.g. `div>ul>li*3` + `Tab` |

---

## 8. Plugin Manager Commands

### vim-plug

| Command | Description |
|---------|-------------|
| `:source %` | Reload the current configuration file |
| `:PlugInstall` | Install all listed plugins |
| `:PlugUpdate` | Update all installed plugins |
| `:PlugClean` | Remove plugins no longer in config |
| `:PlugStatus` | Check status of all plugins |

### CoC

| Command | Description |
|---------|-------------|
| `:CocList extensions` | View and manage installed CoC extensions |
| `:CocInstall <name>` | Install a CoC extension |
| `:CocUninstall <name>` | Uninstall a CoC extension |
| `:CocCommand prettier.formatFile` | Format current file with Prettier |

---
## 10. Setup Workflow

Follow these steps for a fresh setup:

1. Install `vim-plug` using the `curl` command in the [Installation](#1-installation) section.
2. Install system dependencies: `xclip`, `xsel`, `nodejs`, `npm`.
3. Install a Nerd Font and set it in your terminal emulator.
4. Copy the [full configuration](/vim/.vimrc) to `~/.vimrc` or `~/.config/nvim/init.vim`.
5. Open Vim/Neovim and run `:PlugInstall`.
6. Install CoC extensions with `:CocInstall coc-html coc-css coc-tsserver coc-json coc-prettier coc-emmet`.
7. Restart Vim/Neovim — setup complete.

---

## References

- [vim-plug GitHub](https://github.com/junegunn/vim-plug)
- [NERDTree Documentation](https://github.com/preservim/nerdtree)
- [coc.nvim Wiki](https://github.com/neoclide/coc.nvim/wiki)
- [Catppuccin for Vim](https://github.com/catppuccin/vim)
- [FZF GitHub](https://github.com/junegunn/fzf)
- [Nerd Fonts](https://www.nerdfonts.com/)
