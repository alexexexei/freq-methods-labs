import numpy as np
import matplotlib.pyplot as plt


def showf(x, y, xlim=(None, None), ylim=(None, None), title=None):
    plt.plot(x, y)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.title(title)
    plt.show()


def rectf(t):
    return np.where((-0.5 <= t) & (t <= 0.5), 1, 0)


def sinc(v):
    return np.where(v == 0, 1, np.sin(np.pi * v) / (np.pi * v))


def trapz(f, t, v):
    F = []
    for k in v:
        F_k = np.trapz(f * np.exp(-1j * 2 * np.pi * k * t), t)
        F.append(F_k)
    return F


def undo_trapz(F, t, v):
    f = []
    for k in t:
        f_k = np.trapz(F * np.exp(1j * 2 * np.pi * k * v), v)
        f.append(f_k)
    return f


T = 200
dt = 0.01
t = np.arange(-T / 2, T / 2 + dt, dt)
rectf_ = rectf(t)

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
sinc_ = sinc(v)

# trapz_ = trapz(rectf_, t, v)
# rest_trapz = undo_trapz(trapz_, t, v)

N = len(t)
unit = 1 / np.sqrt(N)
fft_ = unit * np.fft.fftshift(np.fft.fft(rectf_))
rest_fft = np.fft.ifft(np.fft.ifftshift(fft_)) / unit

smart_fft = unit * np.fft.fftshift(np.fft.fft(rectf_ * dt))
rest_smfft = np.fft.ifft(np.fft.ifftshift(smart_fft)) / unit / dt

showf(t, rectf_, title='Rectangular function')
showf(v, sinc_, title='Cardinal sine')

# showf(t, rest_trapz, title='Trapz rectangular function')
# showf(v, trapz_, title='Trapz cardinal sine')

showf(t, rest_fft, title='Unitary FFT rectangular function')
showf(v, fft_, title='Unitary FFT cardinal sine')

showf(t, rest_smfft, title='Smart FFT rectangular function')
showf(v, smart_fft, title='Smart FFT cardinal sine')