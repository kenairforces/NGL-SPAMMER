# CODE BY KENAIRFORCES
# DO NOT CLAIM THIS TOOLS
# DO NOT SELL THIS TOOLS
# RECODE? GIVE AUTHOR NAME
# THANKS TO
# - ALLAH
# - ME
# - MY PC


import sys, threading, time, random, requests, argparse, os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, QRect
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

# ================== ARGUMENT PARSER ==================
parser = argparse.ArgumentParser(
    description="💀 [NGL SPAMMER - MODERN MODE by KENAIRFORCES] 💀\n🔥 CLI/GUI Hybrid for Maximum DOMINATION 🔥",
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('--cli', action='store_true', help="🔥 Aktifin CLI mode (buat Termux / no GUI)")
parser.add_argument('--user', type=str, help="🎯 Username target NGL (tanpa https://ngl.link/)")
parser.add_argument('--msg', type=str, help="💬 Pesan spam, pisah pake koma (contoh: hai,tes,kamu siapa?)")
parser.add_argument('--dur', type=int, help="⏱ Durasi spam (dalam detik)")
parser.add_argument('--threads', type=int, default=5, help="⚙️ Jumlah thread spam (default = 5)")
args = parser.parse_args()


# ================== GLOBAL ==================
stop_flag = False
console = Console()
cooldown_time = 20

# ================== SPAM FUNCTION ==================
def spam_ngl(target_user, messages, duration):
    global stop_flag
    end_time = time.time() + duration
    while time.time() < end_time and not stop_flag:
        msg = random.choice(messages)
        device_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
        payload = {
            "username": target_user,
            "question": msg,
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        try:
            res = requests.post("https://ngl.link/api/submit", json=payload, headers={"Content-Type": "application/json"})
            if res.status_code == 429:
                rprint(f"[bold red]🚫 RATE LIMITED:[/bold red] 429 DETECTED! Cooling down...")
                time.sleep(cooldown_time)
                continue
            rprint(f"[bold green]✅ SENT:[/bold green] {msg} [cyan]| Status:[/cyan] {res.status_code}")
        except Exception as e:
            rprint(f"[red]❌ ERROR:[/red] {e}")
        time.sleep(random.uniform(2, 5))  # Random delay to avoid detection

def start_multi_spam(username, messages, duration, thread_count=5):
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=spam_ngl, args=(username, messages, duration))
        t.daemon = True
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# ================== CLI MODE ==================
def run_cli():
    console.rule("[bold red]💀 CLI MODE ENABLED BY KENAIRFORCES 💀")
    console.print(Panel(f"[bold green]🎯 Target:[/bold green] {args.user}\n[cyan]💬 Messages:[/cyan] {args.msg}\n[yellow]⏱ Duration:[/yellow] {args.dur}s\n[magenta]🚀 Threads:[/magenta] {args.threads}", title="NGL SPAMMER", style="bold white"))
    console.rule("[bold green]SENDING STARTED")
    start_multi_spam(args.user, args.msg.split(","), args.dur, args.threads)

if args.cli and args.user and args.msg and args.dur:
    run_cli()
    sys.exit(0)

# ================== GUI MODE ==================
class NGLSpammerGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("💣 NGL Spammer GUI v2")
        self.setGeometry(200, 200, 460, 320)
        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f0f;
                color: #e0e0e0;
                font-size: 15px;
                font-family: 'Segoe UI';
            }
            QLineEdit, QPushButton {
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #555;
                background-color: #1e1e1e;
                color: white;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)
        self.init_ui()
        self.animate_window()

    def animate_window(self):
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(800)
        self.anim.setStartValue(QRect(100, 100, 100, 100))
        self.anim.setEndValue(QRect(200, 200, 460, 320))
        self.anim.start()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.link_input = QtWidgets.QLineEdit(placeholderText="https://ngl.link/username")
        layout.addWidget(self.link_input)

        self.message_input = QtWidgets.QLineEdit(placeholderText="Pesan (pisah pake koma)")
        layout.addWidget(self.message_input)

        self.duration_input = QtWidgets.QLineEdit()
        self.duration_input.setPlaceholderText("Durasi dalam detik (contoh: 30)")
        layout.addWidget(self.duration_input)

        self.thread_input = QtWidgets.QLineEdit()
        self.thread_input.setPlaceholderText("Jumlah thread (default 5)")
        layout.addWidget(self.thread_input)

        btn_layout = QtWidgets.QHBoxLayout()
        self.start_button = QtWidgets.QPushButton("🔥 MULAI")
        self.stop_button = QtWidgets.QPushButton("🛑 STOP")
        btn_layout.addWidget(self.start_button)
        btn_layout.addWidget(self.stop_button)
        layout.addLayout(btn_layout)

        self.start_button.clicked.connect(self.start_spam)
        self.stop_button.clicked.connect(self.stop_spam)

        self.setLayout(layout)

    def start_spam(self):
        try:
            link = self.link_input.text().strip()
            if not link.startswith("https://ngl.link/"):
                raise ValueError("Link NGL gak valid!")

            username = link.replace("https://ngl.link/", "").strip()
            messages = [m.strip() for m in self.message_input.text().split(",") if m.strip()]
            duration = int(self.duration_input.text().strip())
            threads = int(self.thread_input.text().strip()) if self.thread_input.text().strip() else 5

            if not messages:
                raise ValueError("Isi minimal 1 pesan!")

            global stop_flag
            stop_flag = False
            threading.Thread(target=start_multi_spam, args=(username, messages, duration, threads)).start()
            QtWidgets.QMessageBox.information(self, "✅ GASSKAN!", "Spammer jalan di background WAK!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "❌ ERROR", str(e))

    def stop_spam(self):
        global stop_flag
        stop_flag = True
        QtWidgets.QMessageBox.information(self, "🛑 STOP", "Spamming dihentikan WAK!")

# ================== RUN GUI ==================
app = QtWidgets.QApplication(sys.argv)
window = NGLSpammerGUI()
window.show()
sys.exit(app.exec_())
