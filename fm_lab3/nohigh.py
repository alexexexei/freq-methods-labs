import help as hp
import static as st

import filters as ft
import builder as bd


b = 0.5
c = 0
d = 0.1
v_0 = st.V / 10

u = hp.u_f(st.g_fs, st.times, b, c, d)
flt_u, U = ft.filter_high(st.freqs, u, v_0)

bd.build_u__flt_u(st.times, u, flt_u, clr1='b', clr2='r', title='High frequencies filter')
bd.build_abs_u__flt_u(st.times, u, U, clr1='b', clr2='r', title='Abs high frequencies filter')

