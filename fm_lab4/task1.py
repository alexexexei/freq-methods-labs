import numpy as np
import matplotlib.pyplot as plt


def build_f(xfunc, yfunc, fz1=12,
            fz2=6, clr='b', ttl=None,
            grid=True, xlab=None, ylab=None,
            xl1=None, xl2=None, yl1=None,
            yl2=None):
    plt.plot(xfunc, yfunc, color=clr)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(ttl)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.grid(grid)
    plt.show()


def apply_noise(y, a, t):
    return y + a*(np.random.rand(len(t))-0.5)


def numerical_diff(y, dt):
    ndiff = []
    for k in range(len(y) - 1):
        ndiff_k = (y[k+1]-y[k])/dt
        ndiff.append(ndiff_k)
    return ndiff


def spectral_diff(y, t, v):
    Y = []
    for k in v:
        Y_k = np.trapz(y * np.exp(-1j * 2 * np.pi * k * t), t)
        Y.append(Y_k)
    temp = 1j * 2 * np.pi * v * Y
    return np.fft.ifft(temp), Y


dt = 0.1
t = np.arange(-100, 100 + dt, dt)
y = np.sin(t)
build_f(t, y, ttl='Clear sine', xlab='Time', ylab='Amplitude')

a = 0.5
y = apply_noise(y, a, t)
build_f(t, y, ttl=f'Noisy sine, a={a}', xlab='Time', ylab='Amplitude')

nsin = numerical_diff(y, dt)
build_f(t[:-1], nsin, ttl='Numerical derivative of sine', xlab='Time', ylab='Amplitude')

v = np.fft.fftfreq(len(t), dt)
res, Y = spectral_diff(y, t, v)
build_f(v, res.real, ttl='Real part of spectral derivative of sine', xlab='Frequency', ylab='Amplitude')
build_f(v, res.imag, ttl='Imaginary part of spectral derivative of sine', xlab='Frequency', ylab='Amplitude')
build_f(v, np.array(Y).real, ttl='Real part of Fourier image of sine', xlab='Frequency', ylab='Amplitude')
build_f(v, np.array(Y).imag, ttl='Imaginary part of Fourier image of sine', xlab='Frequency', ylab='Amplitude')

tdcos = -np.sin(t)
build_f(t, tdcos, ttl='True derivative of cosine', xlab='Time', ylab='Frequency')
