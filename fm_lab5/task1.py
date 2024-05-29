import numpy as np

import helpf as hp
import ftmath as fm
import showf as sh


T = 200
dt = 0.01
t = np.arange(-T / 2, T / 2 + dt, dt)
rectf_ = hp.rectf(t)
name1 = 'rectangular function'

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
sinc_ = hp.sinc(v)
name2 = 'cardinal sine'

trapz_ft = fm.trapz(rectf_, t, v)
trapz_ift = fm.undo_trapz(trapz_ft, t, v)

ortho_fft, ortho_ifft = fm.dft(rectf_, norm='ortho')

const = dt * np.exp(-2 * np.pi * 1j * v * t[0])
smart_fft, smart_ifft = fm.dft(rectf_, coeff=const)

sh.showf(t,
         rectf_,
         xlim=(-3, 3),
         title=(name1[0].upper()) + name1[1:],
         xlabel=rf'$t$',
         ylabel=r'$\Pi(t)$')
sh.showf(v,
         sinc_,
         xlim=(-3, 3),
         title=(name2[0].upper()) + name2[1:],
         xlabel=rf'$\nu$',
         ylabel=r'$\hat{\Pi}(\nu)$')

sh.showfs(t, [np.asarray(trapz_ift).real, rectf_],
          xlim=(-3, 3),
          title=f'Trapz ift {name1}',
          linest=['-', '--'],
          labels=['itft rectf', 'rectf'],
          xlabel=rf'$t,t\in {[t[0], round(t[-1], 2)]},dt={dt}$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs(v, [np.asarray(trapz_ft).real, sinc_],
          xlim=(-3, 3),
          title=f'Trapz ft {name2}',
          linest=['-', '--'],
          labels=['tft rectf', 'sinc'],
          xlabel=rf'$\nu$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)

sh.showfs(t, [ortho_ifft.real, rectf_],
          xlim=(-3, 3),
          title=f'Unitary ifft {name1}',
          linest=['-', '--'],
          labels=['uifft', 'rectf'],
          xlabel=rf'$t$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs(v, [ortho_fft.real, sinc_],
          xlim=(-3, 3),
          title=f'Unitary fft {name2}',
          linest=['-', '--'],
          labels=['ufft', 'sinc'],
          xlabel=rf'$\nu$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)

sh.showfs(t, [smart_ifft.real, rectf_],
          xlim=(-3, 3),
          title=f'Smart ifft {name1}',
          linest=['-', '--'],
          labels=['sifft', 'rectf'],
          xlabel=rf'$t$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs(v, [smart_fft.real, sinc_],
          xlim=(-3, 3),
          title=f'Smart fft {name1}',
          linest=['-', '--'],
          labels=['sfft rectf', 'sinc'],
          xlabel=rf'$\nu$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)
