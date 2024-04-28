import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b = 3
c = 1.5
d = 1
v_0 = 5
v_0_2 = [[-0.74, -0.39], [0.39, 0.74]]

u = hp.u_f(g_fs, time, b, c, d)
flt_u, flt_U = ft.filter_high(freq, u, v_0)
flt_u_0, flt_U_0 = ft.filter_special(freq, u, v_0_2)
flt_u_2, flt_U_2 = ft.filter_special(freq, flt_u, v_0_2)


bd.build_u_or_U(time, u, xlab='Time', title='Noisy signal', legend=False, fz1=12, fz2=6)
bd.build_u_to_U(freq, u, title='fft noisy signal', legend=False, fz1=12, fz2=6, xl1=-20, xl2=20, yl1=-400, yl2=500)

bd.build_u__flt_u(time, u, flt_u,
                  title=rf'High frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, u, flt_U,
                           title=rf'Abs high frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6,
                           xl1=-30, xl2=30)

bd.build_u__flt_u(time, u, flt_u_0,
                  title=rf'Special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}', fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, u, flt_U_0,
                           title=rf'Abs special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}', fz1=12, fz2=6,
                           xl1=-30, xl2=30)

bd.build_u__flt_u(time, u, flt_u_2,
                  title=rf'High and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
                  fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, u, flt_U_2,
                           title=rf'Abs high and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
                           fz1=12, fz2=6, xl1=-30,
                           xl2=30)
