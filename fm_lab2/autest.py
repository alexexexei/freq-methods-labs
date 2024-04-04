import wave

import numpy as np
import matplotlib.pyplot as plt

wav = wave.open("fm_lab2/chord/chord26.wav", "r")
raw = wav.readframes(-1)
raw = np.frombuffer(raw, dtype=np.int16)

if wav.getnchannels() == 2:
    print("asdasda")

plt.title("f(t)")

sampleRate = wav.getframerate()

time = np.linspace(0, len(raw) / sampleRate, num=len(raw))

raw = np.array(raw)

ans = []
n = len(time)
f = np.linspace(0, 3000, 3000)
for i in f:
    integral = np.trapz(raw * np.exp(-1j * 2 * np.pi * i * time), time)
    ans.append(np.abs(integral))

plt.figure()
plt.ylabel(r'$|\widehat{f}(v)|$')
plt.xlabel("frequency")
plt.plot(f, ans)
plt.show()