import sounddevice as sd
from scipy.io.wavfile import write
import time

fs = 44100

name = input("Kayıt adı: ")
duration = int(input("Süre: "))

audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

filename = f"{name}_{int(time.time())}.wav"
write(filename, fs, audio)

print("Kaydedildi:", filename)
