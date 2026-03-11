# Neovim Guide

A simple guide for setting up **Neovim/Vim**, installing plugins, and
enabling clipboard support on Linux.

------------------------------------------------------------------------

## 1. Installation

### 1.1 Install Plugin Manager (vim-plug)

`vim-plug` is a fast and minimal plugin manager for Vim/Neovim.

Run the following command to install it:

``` bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

This command downloads `plug.vim` and places it inside the Vim autoload
directory.

------------------------------------------------------------------------

### 1.2 Install Clipboard Dependencies

To allow Vim/Neovim to interact with the **system clipboard**, install
the following packages:

``` bash
sudo apt install xclip xsel
```

These tools allow copying and pasting between Vim and your system
clipboard.

------------------------------------------------------------------------

## 2. Plugin Installation

After adding plugins to your Vim configuration file (`.vimrc` or
`init.vim`), you need to install them.

### Reload Vim Configuration

Inside Vim, run:

``` vim
:source %
```

This reloads the current configuration file.

------------------------------------------------------------------------

### Install Plugins

Then install all declared plugins using:

``` vim
:PlugInstall
```

Wait until the installation process finishes.

After the installation is complete, **restart Vim/Neovim** to ensure all
plugins load correctly.

------------------------------------------------------------------------

## 3. Plugin Management

Useful commands for managing plugins:

  Command          Description
  ---------------- ---------------------------------------
  `:PlugInstall`   Install plugins listed in your config
  `:PlugUpdate`    Update installed plugins
  `:PlugClean`     Remove unused plugins
  `:PlugStatus`    Check plugin status

------------------------------------------------------------------------

## 4. Recommended Workflow

Typical setup process:

1.  Install **vim-plug**
2.  Configure plugins inside `.vimrc` or `init.vim`
3.  Reload configuration using `:source %`
4.  Install plugins using `:PlugInstall`
5.  Restart Vim/Neovim

------------------------------------------------------------------------

## 5. Notes

-   Always run `:PlugInstall` after adding new plugins.
-   Restart Vim if plugins are not loaded correctly.
-   Keep your plugins updated regularly using `:PlugUpdate`.

------------------------------------------------------------------------

## References

-   https://github.com/junegunn/vim-plug
