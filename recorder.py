import sounddevice as sd
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

fs = 44100
recording = None

def start_record():
    global recording
    duration = int(entry.get())

    label.config(text="🎤 Kayıt başladı...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    filename = f"recordings/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
    write(filename, fs, recording)

    label.config(text="✔ Kayıt bitti!")
    messagebox.showinfo("Kaydedildi", filename)

# GUI
window = tk.Tk()
window.title("🎧 Music Recorder")
window.geometry("300x200")

tk.Label(window, text="Süre (saniye):").pack()

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="🎤 Kaydı Başlat", command=start_record).pack(pady=10)

label = tk.Label(window, text="")
label.pack()

window.mainloop()
