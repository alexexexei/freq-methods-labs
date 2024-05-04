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


def get_LAFR(W):
    return 20 * np.log10(np.abs(W))


def perform(t, v, w, 
            u, a, b, 
            c, d, T, 
            W, LAFR, g_f=None, 
            shift=True, name='Filter'):
    U = np.fft.fft(u)
    flt_U = None
    if shift:
        flt_U = np.fft.fftshift(W) * U
    else:
        flt_U = W * U
    flt_u = np.fft.ifft(flt_U)

    sh_abs_U = abs(np.fft.fftshift(U))
    sh_abs_flt_U = abs(np.fft.fftshift(flt_U))
    flist1 = [u, flt_u.real]
    flist2 = [sh_abs_U, sh_abs_flt_U]
    llist1 = ['Original signal', 'Filtered signal']
    llist2 = ['Abs original signal fft', 'Abs filtered signal fft']
    lcolors = [None, None]
    abs_W = abs(W)
    if g_f is not None:
        flist1.append(g_f)
        llist1.append(r'Original function $g(t)$')
        lcolors.append('r')

    bf.build_fs(t, y=flist1, labels=llist1, colors=lcolors,
                ttl=f'{name}. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Time', ylab='Amplitude', legend=True)
    bf.build_fs(v, y=flist2, labels=llist2, 
                ttl=f'{name} abs fft. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Frequency', ylab='Amplitude', legend=True)
    bf.build_f(w, y=abs_W, ttl=f'{name} amplitude-frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               xlab='Angular frequency', ylab='Amplitude-frequency response')
    bf.build_f(w, y=LAFR, ttl=f'{name} logarithmic amplitude frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               xlab='Angular frequency', ylab='Amplitude')


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
W_1 = W_1f(w, T_0)
LAFR = get_LAFR(W_1)

perform(t, v, w, 
        u, a, b, 
        c, d, T_0, 
        W_1, LAFR, g_f=g_fun,
        name='First order filter')


a = 2
b = 0
c = 10
d = 15

g_fun = get_g_f(t, t_1, t_2, a)
u = get_u(g_fun, t, b, c, d)

T_1 = 0.2
T_2 = 0.5
T_3 = 0.1
W_2 = W_2f(w, T_1, T_2, T_3)
LAFR = get_LAFR(W_2)

perform(t, v, w, 
        u, a, b, 
        c, d, [T_1, T_2, T_3], 
        W_2, LAFR, g_f=g_fun, 
        shift=False, name='Special filter')