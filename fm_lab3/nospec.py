import help as hp
import static as st

import filters as ft
import builder as bd

b = 1
c = 2
d = 1
v_0 = st.V / 6

u = hp.u_f(st.g_fs, st.times, b, c, d)

bd.build_u_or_U(st.times, u, xlab='Time', label='Noisy signal')
bd.build_u_to_U(st.freqs, u, label='fft noisy signal')