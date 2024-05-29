import numpy as np

import helpf as hp
import showf as sh


T = 200
dt = 0.001
t = np.arange(-T / 2, T / 2 + dt, dt)
a1 = 1
a2 = 2
w1 = 3
w2 = 4
p1 = np.pi / 6
p2 = np.pi / 3

y = hp.y_t(t, a1, a2, w1, w2, p1, p2)
sh.showf(t, y)