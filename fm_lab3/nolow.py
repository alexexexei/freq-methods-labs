import help as hp
import static as st

import filters as ft
import builder as bd


b = 0.5
c = 1
d = 0.1
v_0 = st.V / 20

u = hp.u_f(st.g_fs, st.times, b, c, d)
flt_u, U = ft.filter_low(st.freqs, u, v_0)

bd.build_u__flt_u(st.times, u, flt_u, clr1='b', clr2='r', title='Low frequencies filter')
bd.build_abs_u__flt_u(st.times, u, U, clr1='b', clr2='r', title='Abs low frequencies filter')