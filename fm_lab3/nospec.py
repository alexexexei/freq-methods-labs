import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b, c, d = 1.5, -2, -3
v0, v01 = [[-0.52, -0.3], [0.3, 0.52]], 10
u = hp.u_f(g_fs, time, b, c, d)

flt_u_so, flt_U_so = ft.filter_special_out(freq, u, v0)
bd.build_u__flt_u(
    time,
    u,
    flt_u_so.real,
    title=rf'Special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v0}',
    fz1=12,
    fz2=6)
bd.build_abs_u_to_U__flt_U(
    freq,
    u,
    flt_U_so,
    title=rf'Abs special frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v0}',
    fz1=12,
    fz2=6,
    xl1=-10,
    xl2=10)

flt_u_lso, flt_U_lso = ft.filter_low(freq, flt_u_so, v01)
bd.build_u__flt_u(
    time,
    u,
    flt_u_lso.real,
    title=
    rf'Low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v01}, (2) $\nu_0$={v0}',
    fz1=12,
    fz2=6)
bd.build_abs_u_to_U__flt_U(
    freq,
    u,
    flt_U_lso,
    title=
    rf'Abs low and special frequency filter. b={b}, c={c}, d={d}, (1) $\nu_0$={v01}, (2) $\nu_0$={v0}',
    fz1=12,
    fz2=6,
    xl1=-10 - v01,
    xl2=10 + v01)
