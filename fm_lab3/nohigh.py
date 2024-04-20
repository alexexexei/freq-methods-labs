import help as hp
import static as st

import filters as ft
import builder as bd


b = 0.5
c = 0
d = 0.1
v_0 = st.V / 10

u = hp.u_f(st.g_fs, st.times, b, c, d)
flt_u, flt_U = ft.filter_high(st.freqs, u, v_0)

bd.build_u__flt_u(st.times, u, flt_u, title='High frequencies filter')
bd.build_abs_u_to_U__flt_U(st.times, u, flt_U, title='Abs high frequencies filter')

