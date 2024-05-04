import numpy as np

import build_func as bf
import helper as hp


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


def W_1f(w, T):
    p = 1j * w
    return 1 / (T * p + 1)


def W_2f(w, T_1, T_2, T_3):
    p = 1j * w
    return (T_1 * p + 1) ** 2 / ((T_2 * p + 1) * (T_3 * p + 1))


def perform_1(t, v, w, u, a, b, c, d, T_0, g_f=None):
    U = np.fft.fft(u)
    W = W_1f(w, T_0)
    flt_U = np.fft.fftshift(W) * U
    flt_u = np.fft.ifft(flt_U)

    sh_abs_U = abs(np.fft.fftshift(U))
    sh_abs_flt_U = abs(np.fft.fftshift(flt_U))
    flist1 = [u, flt_u.real]
    if g_f is not None:
        flist1.append(g_f)
    flist2 = [sh_abs_U, sh_abs_flt_U]
    llist1 = ['Original signal', 'Filtered signal']
    if g_f is not None:
        llist1.append(r'Original function $g(t)$')
    llist2 = ['Abs original signal fft', 'Abs filtered signal fft']
    abs_W = abs(W)

    bf.build_fs(t, y=flist1, labels=llist1,
                ttl=rf'First order filter. a={a}, b={b}, c={c}, d={d}, $T_0={T_0}$', 
                xlab='Time', ylab='Amplitude', legend=True)
    bf.build_fs(v, y=flist2, labels=llist2, 
                ttl=rf'First order filter abs fft. a={a}, b={b}, c={c}, d={d}, $T_0={T_0}$', 
                xlab='Frequency', ylab='Amplitude', legend=True)
    bf.build_f(w, abs_W, ttl=rf'First order filter amplitude-frequency response. a={a}, b={b}, c={c}, d={d}, $T_0={T_0}$',
               xlab='Angular frequency', ylab='Amplitude-frequency response')


def perform_2(t, v, w, u, a, b, c, d, T_1, T_2, T_3, g_f=None):
    U = np.fft.fft(u)
    W = W_2f(w, T_1, T_2, T_3)
    flt_U = W * U
    flt_u = np.fft.ifft(flt_U)

    sh_abs_U = abs(np.fft.fftshift(U))
    sh_abs_flt_U = abs(np.fft.fftshift(flt_U))
    flist1 = [u, flt_u.real]
    if g_f is not None:
        flist1.append(g_f)
    flist2 = [sh_abs_U, sh_abs_flt_U]
    llist1 = ['Original signal', 'Filtered signal']
    if g_f is not None:
        llist1.append(r'Original function $g(t)$')
    llist2 = ['Abs original signal fft', 'Abs filtered signal fft']
    abs_W = abs(W)

    bf.build_fs(t, y=flist1, labels=llist1,
                ttl=rf'Special filter. a={a}, b={b}, c={c}, d={d}, $T_1={T_1},T_2={T_2},T_3={T_3}$', 
                xlab='Time', ylab='Amplitude', legend=True)
    bf.build_fs(v, y=flist2, labels=llist2, 
                ttl=rf'Special filter abs fft. a={a}, b={b}, c={c}, d={d}, $T_1={T_1},T_2={T_2},T_3={T_3}$', 
                xlab='Frequency', ylab='Amplitude', legend=True)
    bf.build_f(w, abs_W, ttl=rf'Special filter amplitude-frequency response. a={a}, b={b}, c={c}, d={d}, $T_1={T_1},T_2={T_2},T_3={T_3}$', 
               xlab='Angular frequency', ylab='Amplitude-frequency response')


T = 10
dt = 0.01

V = 1 / dt
dv = 1 / T

t_1 = -1.5
t_2 = 2.5

t = hp.get_t(T, dt)
v = hp.get_v(V, dv)
w = 2 * np.pi * v


a = 1
b = 0.6
c = 0
d = 0.7

g_fun = get_g_f(t, t_1, t_2, a)
u = get_u(g_fun, t, b, c, d)

T_0 = 1

perform_1(t, v, w, u, a, b, c, d, T_0, g_fun)


a = 10
b = 0
c = 10
d = 15

g_fun = get_g_f(t, t_1, t_2, a)
u = get_u(g_fun, t, b, c, d)

T_1 = 0.4
T_2 = 0.8
T_3 = 1

perform_2(t, v, w, u, a, b, c, d, T_1, T_2, T_3, g_fun)