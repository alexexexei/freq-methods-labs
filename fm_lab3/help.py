import numpy as np


def get_t(T, dt):
    return np.arange(-T/2, T/2 + dt, dt)


def get_v(V, dv):
    return np.arange(-V/2, V/2 + dv, dv)


def get_U(u):
    return np.fft.fftshift(np.fft.fft(u))


def g_f(t, t_1, t_2, a):
    if (t_1 <= t <= t_2):
        return a
    return 0


def u_f(g_fs: list, time: list, b, c, d):
    return np.array(g_fs) + b*(np.random.rand(len(time))-0.5) + c*np.sin(d*time)


def get_g_fs(time: list, t_1, t_2, a):
    gs = []
    for t in range(len(time)):
        gs.append(g_f(time[t], t_1, t_2, a))

    return gs
