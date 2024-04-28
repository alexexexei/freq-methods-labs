import help as hp
import static as st

import filters as ft
import builder as bd

b = 1
c = 2
d = 1
v_0 = [[-st.V / 6, st.V / 6], [-st.V / 12, st.V / 12]]

u = hp.u_f(st.g_fs, st.times, b, c, d)
flt_u, flt_U = ft.filter_special2(st.freqs, u, v_0)

# bd.build_u_or_U(st.times, u, xlab='Time', label='Noisy signal')
# bd.build_u_to_U(st.freqs, u, label='fft noisy signal')

bd.build_u__flt_u(st.times, u, flt_u, title='Special frequencies filter')
bd.build_abs_u_to_U__flt_U(st.times, u, flt_U, title='Abs special frequencies filter')

