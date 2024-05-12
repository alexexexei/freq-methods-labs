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

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
spdsin, Y, dY = fm.spectral_diff(y, t, v)
print(f'phase_shift={np.arctan2(np.imag(dY[0]), np.real(dY[0]))}')

phase = -np.pi / 2
tdcos = -np.sin(t)
tdcos2 = -np.sin(t + phase)

ndsin.append(y[-1] / 2)
spdsin = np.array(spdsin)
Y = np.array(Y)
flist = [ndsin, spdsin.real, tdcos]
flist2 = flist[:2]
flist2.append(tdcos2)
clist = [None, None, 'r']
llist = ['Num. der. of sine', 'Re. spec. der. of sine', 'True der. of cosine']
llist2 = llist[:2]
llist2.append(rf'True der. of cosine, $\phi$={phase}')


bf.build_f(t, y, ttl=f'Noisy sine, a={a}, dt={dt}',
           xlab='Time', ylab='Amplitude')
bf.build_f(t, ndsin, ttl=f'Numerical derivative of sine, a={a}, dt={dt}',
           xlab='Time', ylab='Amplitude')

bf.build_f(t, spdsin.real, ttl=f'Real part of spectral derivative of sine, a={a}, dt={dt}',
           xlab='Time', ylab='Amplitude')
bf.build_f(t, spdsin.imag, ttl=f'Imaginary part of spectral derivative of sine, a={a}, dt={dt}',
           xlab='Time', ylab='Amplitude')
bf.build_f(v, Y.real, ttl=f'Real part of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency', ylab='Amplitude')
bf.build_f(v, Y.imag, ttl=f'Imaginary part of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency', ylab='Amplitude', xl1=-0.763, xl2=0.763)
bf.build_f(v, dY.real, ttl=f'Real part of spectral derivative of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency', ylab='Amplitude')
bf.build_f(v, dY.imag, ttl=f'Imaginary part of spectral derivative of Fourier image of sine, a={a}, dt={dt}',
           xlab='Frequency', ylab='Amplitude')

bf.build_fs(t, y=flist, colors=clist, legend=True, 
            labels=llist, ttl=f'True der. of cosine, num. der. of sine and spec. der. of sine comparison; a={a}, dt={dt}')
bf.build_fs(t, y=flist2, colors=clist, legend=True, 
            labels=llist2, ttl=rf'True der. of cosine with phase shift, num. der. of sine and spec. der. of sine comparison; a={a}, dt={dt}')
