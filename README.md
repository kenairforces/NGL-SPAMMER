
# 💣 NGL SPAMMER v6 - GUI + CLI by @kenairforces

🔥 Tool spam brutal ke NGL forms dengan tampilan GUI modern (PyQt5) dan mode CLI buat Termux warriors.  
Full power! Ada anti-429 cooldown, multithread, emoji support, dan vibes hacker maksimal‼️

---

## 🚀 FITUR

- ✅ GUI modern PyQt5 (support emoji & animasi)
- ⚙️ CLI mode for Termux & headless system
- 🔥 Multithread spam system (default 5)
- 🚫 Auto cooldown pas kena 429
- 🎭 Random device spoofing
- 🕵️‍♂️ Bisa jalan 24 jam++
- 🌈 Emoji safe spam payload

---

## 📦 INSTALLATION

### 🪟 Windows (GUI + CLI)

1. **Install Python** (3.10–3.11 recommended)  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Clone repo dan install dependencies**
   ```bash
   git clone https://github.com/kenairforces/NGL-SPAMMER.git
   cd NGL-SPAMMER
   ```

3. **Install dependencies win (windows)**
   ```bash
   pip install -r requirementswin.txt
   ```

4. **Jalankan GUI**
   ```bash
   python start.py
   ```

5. **Jalankan CLI**
   ```bash
   python start.py --cli --user USERNAME --msg "halo,kirim lagi,test" --dur 60 --threads 5
   ```

---

### 📱 Termux (CLI ONLY)

1. **Install Python**
   ```bash
   pkg update && pkg install python git -y
   ```

2. **Clone repo dan install dependencies**
   ```bash
   git clone https://github.com/kenairforces/NGL-SPAMMER.git
   cd NGL-SPAMMER
   ```

3. **Install dependencies tx (termux)**
   ```bash
   pip install -r requirementstx.txt
   ```

4. **Jalankan mode CLI**
   ```bash
   python start.py --cli --user USERNAME --msg "halo,test,apa kabar" --dur 60 --threads 5
   ```

---

## ⚔️ ARGUMENTS (CLI MODE)

| Flag         | Keterangan                                    |
|--------------|-----------------------------------------------|
| `-h`         | Bantuan                                       |
| `--cli`      | Aktifkan mode CLI                             |
| `--user`     | Username NGL target (tanpa `https://`)        |
| `--msg`      | Daftar pesan, pisahkan dengan koma `,`        |
| `--dur`      | Durasi spam dalam detik                       |
| `--threads`  | Jumlah thread spam (default = 5)              |

Contoh:
```bash
python start.py --cli --user kenairforces --msg "halo,kirim test,pesanku" --dur 120 --threads 10
```

---

## 🧠 CATATAN PENTING

- ❗ Jangan spam terlalu cepat, bisa kena ban IP.
- ❗ Rate limit (429) otomatis di-handle dengan sleep 20 detik.
- ❗ Bisa digunakan 24 jam nonstop (asal koneksi stabil).

---

## ⚠️ DISCLAIMER

This tool is for **educational purposes only**. Use it responsibly.

---

## 🧠 AUTHOR

- 🚀 Telegram: [@kenairforces](https://t.me/Kenairforces)
- 🎯 GitHub: [kenairforces](https://github.com/kenairforces)
