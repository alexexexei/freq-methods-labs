import numpy as np


def tft(f, t, v):
    F = []
    for k in v:
        F_k = np.trapz(f * np.exp(-2j * np.pi * k * t), t)
        F.append(F_k)
    return np.array(F)


def tift(F, t, v):
    f = []
    for k in t:
        f_k = np.trapz(F * np.exp(2j * np.pi * k * v), v)
        f.append(f_k)
    return np.array(f)


def dft(f, norm=None):
    fft_ = np.fft.fftshift(np.fft.fft(f, norm=norm))
    ifft_ = np.fft.ifft(np.fft.ifftshift(fft_), norm=norm)
    return fft_, ifft_


def sdft(f, t, v, norm=None):
    dt = t[1] - t[0]
    c = dt * np.exp(-2j * np.pi * v * t[0])
    fft_, ifft_ = dft(f, norm=norm)
    fft_ *= c
    return fft_, ifft_


def interp(f, t, t_s, B):
    ans = np.zeros_like(t)
    for n in range(-len(t_s) // 2, len(t_s) // 2):
        t_n = n / (2 * B)
        ans += f(t_n) * np.sinc(2 * B * (t - t_n))
    return ans
