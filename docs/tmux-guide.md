# 🚀 Tmux Configuration & Usage Guide

This documentation contains the Tmux usage guide, customized with **Vim-style** navigation, **Ctrl+a** prefix, and **Linux/XFCE** integration.

---

## 🛠️ Key Mappings
Main Prefix: `Ctrl + a` (replacing `Ctrl + b`)

| Category | Shortcut | Function |
| :--- | :--- | :--- |
| **System** | `Prefix` + `r` | Reload `~/.tmux.conf` configuration |
| **System** | `Prefix` + `I` | Install plugins (TPM) |
| **Navigation** | `Prefix` + `h/j/k/l` | Switch pane focus (Left, Down, Up, Right) |
| **Pane** | `Prefix` + `\|` | Split pane vertically |
| **Pane** | `Prefix` + `-` | Split pane horizontally |
| **Resize** | `Prefix` + `H/J/K/L` | Resize pane (Hold Prefix) |

---

## 📋 Copy & Paste (Linux Integration)
This configuration supports the system clipboard using `xclip`.

1. Press `Prefix` + `[` to enter **Copy Mode**.
2. Use `h, j, k, l` to navigate the cursor.
3. Press `v` to start **visual selection**.
4. Press `y` to **yank** (copy) to the system clipboard.
5. Press `q` to exit Copy Mode.

---

## 🗂️ Session Management
Tmux allows you to leave your coding session without killing the processes.

* **Detach Session:** `Prefix` + `d` (Session keeps running in the background).
* **Attach Back:** Type `tmux a` in the terminal.
* **Switch Session:** `Prefix` + `s` (Select session visually).

---

## 🎨 Appearance & UI
* **Status Bar:** Located at the **top**.
* **Colors:** Dark theme with **Neon Green** accents (`#00e68a`) for active elements.
* **Mouse:** Enabled (`on`), you can click panes or scroll with the mouse.

---

## 🔌 Plugins (TPM)
Plugins are managed by **Tmux Plugin Manager (TPM)**:
1. `tmux-sensible`: Optimal default settings.
2. `tmux-resurrect`: Save sessions manually.
3. `tmux-continuum`: Automatically save sessions every 15 minutes and restore on startup.

---

## 💡 Troubleshooting
* **Messy Colors:** Ensure your terminal emulator (XFCE Terminal) supports 256 colors.
* **Copy Failed:** Ensure `xclip` is installed via `sudo apt install xclip`.
* **Plugins Not Working:** Ensure the TPM folder is cloned to `~/.tmux/plugins/tpm`.
