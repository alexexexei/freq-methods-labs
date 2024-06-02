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

new_T = 200
new_dt = 0.01
new_t = np.arange(-new_T / 2, new_T / 2 + new_dt, new_dt)
new_rectf = hp.rectf(new_t)

new_V = 1 / new_dt
new_dv = 1 / new_T
new_v = np.arange(-new_V / 2, new_V / 2 + new_dv, new_dv)

tft_ = fm.tft(new_rectf, new_t, new_v)
tift_ = fm.tift(tft_, new_t, new_v)

# for some reason fft is not unitary despite the norm='ortho' argument
ufft, uifft = fm.dft(rectf_, norm='ortho')
sfft, sifft = fm.sdft(rectf_, t, v)

sh.showf(t,
         rectf_,
         xlim=(-3, 3),
         title=(name1[0].upper()) + name1[1:],
         xlabel=rf'$t$',
         ylabel=r'$\Pi(t)$')
sh.showf(v,
         sinc_,
         xlim=(-10, 10),
         title=(name2[0].upper()) + name2[1:],
         xlabel=rf'$\nu$',
         ylabel=r'$\hat{\Pi}(\nu)$')

sh.showfs([new_t, t], [tift_.real, rectf_],
          xlim=(-3, 3),
          title=f'Trapz ift {name1}',
          linest=['-', '--'],
          labels=['tift rectf', 'rectf'],
          xlabel=rf'$t,t\in {[new_t[0], round(new_t[-1], 2)]},dt={new_dt}$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs([new_v, v], [tft_.real, sinc_],
          xlim=(-10, 10),
          title=f'Trapz ft {name2}',
          linest=['-', '--'],
          labels=['tft rectf', 'sinc'],
          xlabel=rf'$\nu,\nu\in {[new_v[0], round(new_v[-1], 2)]},d\nu={new_dv}$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)

sh.showfs(t, [uifft.real, rectf_],
          xlim=(-3, 3),
          title=f'Unitary ifft {name1}',
          linest=['-', '--'],
          labels=['uifft', 'rectf'],
          xlabel=rf'$t$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs(v, [ufft.real, sinc_],
          xlim=(-10, 10),
          title=f'Unitary fft {name2}',
          linest=['-', '--'],
          labels=['ufft', 'sinc'],
          xlabel=rf'$\nu$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)

sh.showfs(t, [sifft.real, rectf_],
          xlim=(-3, 3),
          title=f'Smart ifft {name1}',
          linest=['-', '--'],
          labels=['sifft', 'rectf'],
          xlabel=rf'$t$',
          ylabel=r'$\Pi(t)$',
          legend=True)
sh.showfs(v, [sfft.real, sinc_],
          xlim=(-10, 10),
          title=f'Smart fft {name1}',
          linest=['-', '--'],
          labels=['sfft rectf', 'sinc'],
          xlabel=rf'$\nu$',
          ylabel=r'$\hat{\Pi}(\nu)$',
          legend=True)