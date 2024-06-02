import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

# Нужно подобрать такие значения, чтобы слева и справа от нуля были высокие амплитуды,
# которые (обычно) выше, чем высокая амплитуда по середине. Зануляем эти две амплитуды
# и получаем график с убранным влиянием параметра c (гармонический шум)
b = 1.5
c = -2
d = -3
v_0 = 10
v_0_1 = 0.3
v_0_2 = [[-0.52, -0.3], [0.3, 0.52]]
u = hp.u_f(g_fs, time, b, c, d)

build_u_U = False
filter_low = True
filter_sp_o = True

flt_u_l, flt_U_l = None, None
flt_u_so, flt_U_so = None, None
flt_u_lso, flt_U_lso = None, None

if build_u_U:
    bd.build_u_or_U(time,
                    u,
                    xlab='Time',
                    title=f'Noisy signal. b={b}, c={c}, d={d}',
                    legend=False,
                    fz1=12,
                    fz2=6)
    bd.build_u_to_U(freq,
                    u,
                    title=f'fft noisy signal. b={b}, c={c}, d={d}',
                    legend=False,
                    fz1=12,
                    fz2=6,
                    xl1=-10,
                    xl2=10)

if filter_sp_o:
    flt_u_so, flt_U_so = ft.filter_special_out(freq, u, v_0_2)
    bd.build_u__flt_u(
        time,
        u,
        flt_u_so,
        title=
        rf'Special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}',
        fz1=12,
        fz2=6)
    bd.build_abs_u_to_U__flt_U(
        freq,
        u,
        flt_U_so,
        title=
        rf'Abs special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0_2}',
        fz1=12,
        fz2=6,
        xl1=-10,
        xl2=10)

if filter_low:
    flt_u_l, flt_U_l = ft.filter_low(freq, u, v_0)
    bd.build_u__flt_u(
        time,
        u,
        flt_u_l,
        title=rf'Low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}',
        fz1=12,
        fz2=6)
    bd.build_abs_u_to_U__flt_U(
        freq,
        u,
        flt_U_l,
        title=rf'Abs low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}',
        fz1=12,
        fz2=6,
        xl1=-20,
        xl2=20)

if filter_low and filter_sp_o:
    flt_u_lso, flt_U_lso = ft.filter_special_out(freq, flt_u_l, v_0_2)
    bd.build_u__flt_u(
        time,
        u,
        flt_u_lso,
        title=
        rf'Low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
        fz1=12,
        fz2=6)
    bd.build_abs_u_to_U__flt_U(
        freq,
        u,
        flt_U_lso,
        title=
        rf'Abs low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v_0}, (2) $\nu_0$={v_0_2}',
        fz1=12,
        fz2=6,
        xl1=-10,
        xl2=10)
