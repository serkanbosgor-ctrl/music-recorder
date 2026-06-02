import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
from datetime import datetime

fs = 44100

print("🎧 Music Recorder")

duration = int(input("Kayıt süresi (saniye): "))

recordings = Path("recordings")
recordings.mkdir(exist_ok=True)

filename = recordings / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"

print("🎤 Kayıt başladı...")

audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

write(str(filename), fs, audio)

print("✔ Kaydedildi:", filename)
