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


def dft(f, norm=None, coeff=1):
    fft_ = coeff * np.fft.fftshift(np.fft.fft(f, norm=norm))
    ifft_ = np.fft.ifft(np.fft.ifftshift(fft_ / coeff), norm=norm)
    return fft_, ifft_


T = 200
dt = 0.01
t = np.arange(-T / 2, T / 2 + dt, dt)
rectf_ = rectf(t)
name1 = 'rectangular function'

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
sinc_ = sinc(v)
name2 = 'cardinal sine'

trapz_ft = trapz(rectf_, t, v)
trapz_ift = undo_trapz(trapz_ft, t, v)

ortho_fft, ortho_ifft = dft(rectf_, norm='ortho')

const = dt * np.exp(-2 * np.pi * 1j * v * t[0])
smart_fft, smart_ifft = dft(rectf_, coeff=const)

showf(t, rectf_, xlim=(-3, 3), title=(name1[0].upper()) + name1[1:])
showf(v, sinc_, xlim=(-3, 3), title=(name2[0].upper()) + name2[1:])

showf(t, trapz_ift, xlim=(-3, 3), title=f'Trapz ift {name1}')
showf(v, trapz_ft, xlim=(-3, 3), title=f'Trapz ft {name2}')

showf(t, ortho_ifft.real, xlim=(-3, 3), title=f'Unitary ifft {name1}')
showf(v, ortho_fft.real, xlim=(-3, 3), title=f'Unitary fft {name2}')

showf(t, smart_ifft.real, xlim=(-3, 3), title=f'Smart ifft {name1}')
showf(v, smart_fft.real, xlim=(-3, 3), title=f'Smart fft {name2}')