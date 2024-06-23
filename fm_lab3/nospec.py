import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b, c, d = 0.5, 10, 20
u = hp.u_f(g_fs, time, b, c, d)

v = [2.594, 3.858]
v0, v01 = [[-v[1], -v[0]], v], 3.8

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
    xl1=0,
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
    xl1=0,
    xl2=10)
