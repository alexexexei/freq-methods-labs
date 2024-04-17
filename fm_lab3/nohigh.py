import matplotlib.pyplot as plt

import help as hp
from static import times, freqs, g_fs


b = 0.5
c = 0
d = 0.1
u = hp.u_f(g_fs, times, b, c, d)
