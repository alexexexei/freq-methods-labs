import numpy as np


def rectf(t):
    return np.where((-0.5 <= t) & (t <= 0.5), 1, 0)


def sinc(v):
    return np.where(v == 0, 1, np.sin(np.pi * v) / (np.pi * v))


def y_t(t, a1, a2, w1, w2, p1, p2):
    return a1 * np.sin(w1 * t + p1) + a2 * np.sin(w2 * t + p2)
