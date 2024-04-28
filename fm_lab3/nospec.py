import help as hp
import static as st

import filters as ft
import builder as bd


time = st.time
freq = st.freq
g_fs = st.g_fs

b = 1
c = 2
d = 1
v_0 = [[-2, 2]]

u = hp.u_f(g_fs, time, b, c, d)
flt_u, flt_U = ft.filter_special(freq, u, v_0)


bd.build_u_or_U(time, u, xlab='Time', label='Noisy signal')
bd.build_u_to_U(freq, u, label='fft noisy signal')

bd.build_u__flt_u(time, u, flt_u, title='Special frequency filter')
bd.build_abs_u_to_U__flt_U(freq, u, flt_U, title='Abs special frequency filter')
