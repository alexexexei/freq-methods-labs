import numpy as np
import matplotlib.pyplot as plt
from scipy import fft


def rect_wave(a, t):
    return np.array([a if np.abs(val) <= 0.5 else 0 for val in t])


T = 100
dt = 0.01
t = np.arange(-T / 2, T / 2 + dt, dt)

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)

y = rect_wave(1, t)

c = dt * np.exp(-2j * np.pi * v * t[0])

fur1 = fft.fftshift(fft.dct(y))
fur2 = fft.fftshift(fft.fft(y))
fur3 = fft.fftshift(fft.fft(y)) * c

plt.figure(figsize=(8, 5))
plt.xlim(-5, 5)
plt.plot(v, fur1, label='DCT(rect)', alpha=0.75, color='r')
plt.legend()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('DCT of rectangular function')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.xlim(-5, 5)
plt.plot(v, fur2.real, label='FFT(rect)', alpha=0.75, color='b')
plt.legend()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('FFT of rectangular function')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.xlim(-5, 5)
plt.plot(v, fur3.real, label='SFFT(rect)', alpha=0.75, color='b')
plt.legend()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Smart FFT of rectangular function')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.xlim(0, 10)
plt.plot(v, fur1, label='DCT(rect)', alpha=0.75, color='r')
plt.plot(v, fur2.real, label='FFT(rect)', alpha=0.75, color='b')
plt.legend()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('DCT and FFT of rectangular function')
plt.grid(True)
plt.show()