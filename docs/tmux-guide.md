# 🚀 Tmux Configuration & Usage Guide

Dokumentasi ini berisi panduan penggunaan Tmux yang sudah dikustomisasi dengan navigasi ala **Vim**, prefix **Ctrl+a**, dan integrasi **Linux/XFCE**.

---

## 🛠️ Key Mappings
Prefix utama: `Ctrl + a` (menggantikan `Ctrl + b`)

| Kategori | Shortcut | Fungsi |
| :--- | :--- | :--- |
| **Sistem** | `Prefix` + `r` | Reload konfigurasi `~/.tmux.conf` |
| **Sistem** | `Prefix` + `I` | Install plugin (TPM) |
| **Navigasi** | `Prefix` + `h/j/k/l` | Pindah fokus pane (Kiri, Bawah, Atas, Kanan) |
| **Pane** | `Prefix` + `\|` | Split pane secara vertikal |
| **Pane** | `Prefix` + `-` | Split pane secara horizontal |
| **Resize** | `Prefix` + `H/J/K/L` | Ubah ukuran pane (tahan Prefix) |

---

## 📋 Copy & Paste (Linux Integration)
Konfigurasi ini sudah mendukung *system clipboard* menggunakan `xclip`.

1. Tekan `Prefix` + `[` untuk masuk ke **Copy Mode**.
2. Gunakan `h, j, k, l` untuk navigasi kursor.
3. Tekan `v` untuk mulai memilih teks (*visual selection*).
4. Tekan `y` untuk menyalin (*yank*) ke clipboard sistem.
5. Tekan `q` untuk keluar dari Copy Mode.

---

## 🗂️ Session Management
Tmux memungkinkan kamu meninggalkan sesi coding tanpa mematikan prosesnya.

* **Detach Session:** `Prefix` + `d` (Sesi tetap jalan di background).
* **Attach Kembali:** Ketik `tmux a` di terminal.
* **Switch Session:** `Prefix` + `s` (Memilih sesi secara visual).

---

## 🎨 Appearance & UI
* **Status Bar:** Berada di bagian **atas** (`top`).
* **Warna:** Tema gelap dengan aksen **Hijau Neon** (`#00e68a`) untuk elemen aktif.
* **Mouse:** Aktif (`on`), kamu bisa klik pane atau scroll dengan mouse.

---

## 🔌 Plugins (TPM)
Plugin dikelola oleh **Tmux Plugin Manager (TPM)**:
1. `tmux-sensible`: Pengaturan dasar yang optimal.
2. `tmux-resurrect`: Menyimpan sesi secara manual.
3. `tmux-continuum`: Menyimpan sesi otomatis setiap 15 menit dan me-restore saat startup.

---

## 💡 Troubleshooting
* **Warna Berantakan:** Pastikan terminal emulator (XFCE Terminal) mendukung 256 color.
* **Copy Gagal:** Pastikan sudah install xclip dengan `sudo apt install xclip`.
* **Plugin Tidak Jalan:** Pastikan folder TPM sudah di-clone ke `~/.tmux/plugins/tpm`.
