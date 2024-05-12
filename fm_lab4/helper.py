import numpy as np


def apply_noise(y, a, t):
    return y + a * (np.random.rand(len(t)) - 0.5)


def g_func(t, t_1, t_2, a):
    if (t_1 <= t <= t_2):
        return a
    return 0


def get_g_f(t: list, t_1, t_2, a):
    g_f = []
    for k in range(len(t)):
        g_f.append(g_func(t[k], t_1, t_2, a))
    return g_f


def get_u(g_fs: list, t: list, b, c, d):
    return np.array(g_fs) + b * (np.random.rand(len(t)) - 0.5) + c * np.sin(d * t)
