import numpy as np

import build_func as bf
import fourier_math as fm
import helper as hr


T = 200
dt = 0.25
t = np.arange(-T / 2, T / 2 + dt, dt)

y = np.sin(t)
a = 0.2
y = hr.apply_noise(y, a, t)

ndsin = fm.numerical_diff(y, dt)
ndsin.append(y[-1] / 2)

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
spdsin, Y, dY = fm.spectral_diff(y, t, v)

bf.build_f(t,
           y,
           ttl=f'Noisy sine, a={a}, dt={dt}',
           xlab='Time',
           ylab='Amplitude')
bf.build_f(v,
           np.array(Y).real,
           ttl=f'Real part of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency',
           ylab='Amplitude')
bf.build_f(v,
           np.array(Y).imag,
           ttl=f'Imaginary part of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency',
           ylab='Amplitude',
           xl1=-0.763,
           xl2=0.763)
bf.build_f(
    v,
    dY.real,
    ttl=
    f'Real part of spectral derivative of Fourier image of sine, a={a}, dt={dt}',
    xlab='Frequency',
    ylab='Amplitude')
bf.build_f(
    v,
    dY.imag,
    ttl=
    f'Imaginary part of spectral derivative of Fourier image of sine, a={a}, dt={dt}',
    xlab='Frequency',
    ylab='Amplitude')

bf.build_f(t,
           ndsin,
           ttl=f'Numerical derivative of sine, a={a}, dt={dt}',
           xlab='Time',
           ylab='Amplitude')
bf.build_f(t,
           np.array(spdsin).real,
           ttl=f'Real part of spectral derivative of sine, a={a}, dt={dt}',
           xlab='Time',
           ylab='Amplitude')
bf.build_fs(
    t,
    y=[ndsin, np.array(spdsin).real, np.cos(t)],
    colors=[None, None, 'r'],
    legend=True,
    labels=[
        'numd(sine)', 'Re(spd(sine))', 'cos(t)'
    ],
    ttl=
    f'Numerical and spectral derivatives of sine and cosine comparison; a={a}, dt={dt}'
)
