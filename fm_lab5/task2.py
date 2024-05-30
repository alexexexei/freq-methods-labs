import numpy as np

import helpf as hp
import ftmath as fm
import showf as sh


T = 20
dt = 0.0001
t = np.arange(-T / 2, T / 2 + dt, dt)

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)

a1 = 1
a2 = 2
w1 = 3
w2 = 4
p1 = np.pi / 5
p2 = np.pi / 6
y = hp.y_t(t, a1, a2, w1, w2, p1, p2)

B = 7
dt_s = 0.05  # ideal dt_s < 1/2B (Nyquist-Shannon-Kotelnikov theorem)
t_s = np.arange(-B, B + dt_s, dt_s)
y_s = hp.y_t(t_s, a1, a2, w1, w2, p1, p2)


def f(t):
    return a1 * np.sin(w1 * t + p1) + a2 * np.sin(w2 * t + p2)


y_ip = fm.interp(f, t, t_s, B)

b = 2
y_2 = hp.y_t_sinc(t, b)
y_2s = hp.y_t_sinc(t_s, b)


def g(t):
    return np.sinc(b * t)


const = dt * np.exp(-2 * np.pi * 1j * v * t[0])
y_2ip = fm.interp(g, t, t_s, B)
y_2_dft = fm.dft(y_2, coeff=const)
y_2ip_dft = fm.dft(y_2ip, coeff=const)

sh.showfs([t, t_s], [y, y_s],
          title='Original and sampled signal',
          labels=['orig signal', 'sampl signal'],
          xlabel=rf'$t, dt_s={dt_s}$',
          ylabel=r'$y(t)$',
          legend=True)
sh.showfs(t, [y, y_ip],
          title='Interpolated and original signal',
          linest=['-', '--'],
          labels=['orig signal', 'interp signal'],
          xlabel=rf'$t, dt_s={dt_s}$',
          ylabel=r'$y(t)$',
          legend=True)

sh.showfs([t, t_s], [y_2, y_2s],
          title='Original and sampled signal',
          labels=['orig signal', 'sampl signal'],
          xlabel=rf'$t, dt_s={dt_s}$',
          ylabel=r'$y(t)$',
          legend=True)
sh.showfs(t, [y_2, y_2ip],
          title='Interpolated and original signal',
          linest=['-', '--'],
          labels=['orig signal', 'interp signal'],
          xlabel=rf'$t, dt_s={dt_s}$',
          ylabel=r'$y(t)$',
          legend=True)
sh.showfs(v, [y_2_dft[0].real, y_2ip_dft[0].real],
          xlim=(-3, 3),
          title='Smart fft interpolated and original signal',
          labels=['sfft orig', 'sfft interp'],
          xlabel=rf'$\nu, dt_s={dt_s}$',
          ylabel=r'$\hat{y}(\nu)$',
          legend=True)
