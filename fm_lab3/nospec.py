import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b = 1.5
c = -2
d = -3
v_0 = 10
v_0_1 = 0.5
v_0_2 = [[-0.6, -0.37], [0.37, 0.6]]
u = hp.u_f(g_fs, time, b, c, d)

build_u_U = False
filter_low = True
filter_high = True
filter_special_out = True

flt_u, flt_U = None, None
flt_u_0, flt_U_0 = None, None
flt_u_1, flt_U_1 = None, None
flt_u_2, flt_U_2 = None, None


if build_u_U:
    bd.build_u_or_U(time, u, xlab='Time', title=f'Noisy signal. b={b}, c={c}, d={d}', legend=False, fz1=12, fz2=6)
    bd.build_u_to_U(freq, u, title=f'fft noisy signal. b={b}, c={c}, d={d}',
                    legend=False, fz1=12, fz2=6,
                    xl1=-10, xl2=10)


if filter_special_out:
    flt_u_0, flt_U_0 = ft.filter_special_out(freq, u, v_0_2)
    bd.build_u__flt_u(time, u, flt_u_0,
                      title=rf'Special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}', fz1=12, fz2=6)
    bd.build_abs_u_to_U__flt_U(freq, u, flt_U_0,
                               title=rf'Abs special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}', fz1=12, fz2=6,
                               xl1=-10, xl2=10)


if filter_low:
    flt_u, flt_U = ft.filter_low(freq, u, v_0)
    bd.build_u__flt_u(time, u, flt_u,
                      title=rf'Low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6)
    bd.build_abs_u_to_U__flt_U(freq, u, flt_U,
                               title=rf'Abs low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6,
                               xl1=-20, xl2=20)


if filter_high:
    flt_u_1, flt_U_1 = ft.filter_high(freq, u, v_0_1)
    bd.build_u__flt_u(time, u, flt_u_1,
                      title=rf'High frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_1}', fz1=12, fz2=6)
    bd.build_abs_u_to_U__flt_U(freq, u, flt_U_1,
                               title=rf'Abs high frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_1}', fz1=12, fz2=6,
                               xl1=-10, xl2=10)


if filter_low and filter_special_out:
    flt_u_2, flt_U_2 = ft.filter_special_out(freq, flt_u, v_0_2)
    bd.build_u__flt_u(time, u, flt_u_2,
                      title=rf'Low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
                      fz1=12, fz2=6)
    bd.build_abs_u_to_U__flt_U(freq, u, flt_U_2,
                               title=rf'Abs low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
                               fz1=12, fz2=6, xl1=-10,
                               xl2=10)


if filter_high and filter_special_out:
    flt_u_2, flt_U_2 = ft.filter_special_out(freq, flt_u_1, v_0_2)
    bd.build_u__flt_u(time, u, flt_u_2,
                      title=rf'High and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0_1}, (2) $\nu_0$={v_0_2}',
                      fz1=12, fz2=6)
    bd.build_abs_u_to_U__flt_U(freq, u, flt_U_2,
                               title=rf'Abs high and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0_1}, (2) $\nu_0$={v_0_2}',
                               fz1=12, fz2=6, xl1=-10,
                               xl2=10)
