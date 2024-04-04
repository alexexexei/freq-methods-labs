import librosa

import numpy as np
import matplotlib.pyplot as plt

audio_file = 'fm_lab2/chord/chord26.mp3'
y, sr = librosa.load(audio_file)

y = y[0] if len(y.shape) > 1 else y

t = np.arange(len(y)) / sr

# plt.figure(figsize=(10, 4))
plt.plot(t, y)
# plt.title(r'$\text{График } f(t)$')
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.grid(True)
plt.show()

plt.clf()
plt.cla()

frequencies = np.linspace(0, sr / 2, len(y) // 2)
amplitudes = []

for freq in frequencies:
    integral = np.trapz(y * np.exp(-1j * 2 * np.pi * freq * t), t)
    amplitudes.append(np.abs(integral))

plt.figure()
plt.plot(frequencies, amplitudes)
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
# plt.title('Частотная характеристика')
plt.show()
