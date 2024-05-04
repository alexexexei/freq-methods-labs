import numpy as np


def get_t(T, dt):
    return np.arange(-T / 2, T / 2 + dt, dt)


def get_v(V, dv):
    return np.arange(-V / 2, V / 2 + dv, dv)
