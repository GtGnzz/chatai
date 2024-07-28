from colorama import Fore as f
from datetime import datetime
import requests
import os
from rich.console import Console

console = Console()

# Tanggal dan waktu saat ini
now = datetime.now()
tahun = now.year
bulan = now.month
tanggal = now.strftime("%d")

hari_angka = now.weekday()
hari_nama = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][hari_angka]

jam = now.hour
menit = now.minute
detik_awal = now.second

os.system("clear")

logo = f"""
"""

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyALD_4lMsLnqlvXb3aOtLQ-eeYs6rhTaAY'
headers = {'Content-Type': 'application/json'}

print(logo)

while True:
    # Menampilkan prompt dengan gaya baru
    input_text = console.input("[bold yellow]👤 ME: [/bold yellow]").strip()

    if not input_text:
        continue

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }

    detik_awal = datetime.now().second
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    detik_akhir = datetime.now().second

    for candidate in result['candidates']:
        content = candidate['content']
        if 'parts' in content:
            for part in content['parts']:
                if 'text' in part:
                    reply_text = part['text']
                    console.print(f"[bold cyan]👾 AI: {reply_text}[/bold cyan]")
                    console.print(f"[dim]Riwayat: {tahun}/{bulan}/{tanggal} {hari_nama} {jam}:{menit} - Waktu Respon: {detik_akhir - detik_awal} detik[/dim]")
                    break
    print()
