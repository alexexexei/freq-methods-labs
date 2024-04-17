import numpy as np


def get_t(T, dt):
    return np.arange(-T/2, T/2 + dt, dt)


def get_v(V, dv):
    return np.arange(-V/2, V/2 + dv, dv)


def g_f(t, t_1, t_2, a):
    if (t_1 <= t <= t_2):
        return a
    return 0


def u_f(g_fs: list, times: list, b, c, d):
    return np.array(g_fs) + b*(np.random.rand(len(times))-0.5) + c*np.sin(d*times)


def get_g_fs(times: list, t_1, t_2, a):
    gs = []
    for t in range(len(times)):
        gs.append(g_f(times[t], t_1, t_2, a))

    return gs
