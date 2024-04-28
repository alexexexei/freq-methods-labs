import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b = 0.5
c = 1
d = 0.1
v_0 = st.V / 10

u = hp.u_f(g_fs, time, b, c, d)
flt_u, flt_U = ft.filter_low(freq, u, v_0)


bd.build_u__flt_u(time, u, flt_u,
                  title=rf'Low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, u, flt_U,
                           title=rf'Abs low frequency filter. b={b}, c={c}, d={d}, $\nu_0$={v_0}', fz1=12, fz2=6,
                           xl1=-20, xl2=20)
