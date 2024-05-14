import numpy as np

import build_func as bf
import lin_filters as lf
import fourier_math as fm
import helper as hr


def perform(t, v, w, 
            u, a, b, 
            c, d, T, 
            W, W_LOG, g_f=None,
            name='Filter', xl0=None, xl01=None,
            xl1=None, xl2=None, xl3=None,
            xl4=None, xl5=None, xl6=None):
    flt_u, flt_U, U = fm.fft_flt(u, W)
    AFR = fm.get_AFR(W)
    LAFR = fm.get_LAFR(W_LOG)

    flist1 = [u, flt_u.real]
    flist2 = [abs(np.fft.fftshift(U)), abs(np.fft.fftshift(flt_U))]
    llist1 = ['Original signal', 'Filtered signal']
    llist2 = ['Abs original signal fft', 'Abs filtered signal fft']
    lslist = ['-', '-']
    clist = [None, None]
    if g_f is not None:
        flist1.append(g_f)
        llist1.append(r'Original function $g(t)$')
        lslist.append('--')
        clist.append('r')

    bf.build_fs(t, y=flist1, labels=llist1, colors=clist, ls=lslist,
                ttl=f'{name}. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Time', ylab='Amplitude', legend=True, xl1=xl0, xl2=xl01)
    bf.build_fs(v, y=flist2, labels=llist2, 
                ttl=f'{name} abs fft. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Frequency', ylab='Amplitude', legend=True, xl1=xl1, xl2=xl2)
    bf.build_f(w, y=AFR,
               ttl=f'{name} amplitude-frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               xlab='Angular frequency', ylab='Amplitude', xl1=xl3, xl2=xl4)
    bf.build_f(np.log10(w[w > 0]), y=LAFR,
               ttl=f'{name} logarithmic amplitude frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               ylab='Amplitude', xl1=xl5, xl2=xl6)


T = 10
dt = 0.01

V = 1 / dt
dv = 1 / T

t_1 = -1.5
t_2 = 2.5

v_to_w_coeff = 2 * np.pi

t = np.arange(-T / 2, T / 2 + dt, dt)
v = np.arange(-V / 2, V / 2 + dv, dv)
w = v_to_w_coeff * v

v_log = np.arange(0, V / 2 + dv, dv)
w_log = v_to_w_coeff * v_log

perform_W_1 = False
perform_W_2 = True

if perform_W_1:
    a = 1
    b = 0.6
    c = 0
    d = 0.7

    g_fun = hr.get_g_f(t, t_1, t_2, a)
    u = hr.get_u(g_fun, t, b, c, d)

    T_0 = 0.1
    W_1 = lf.W_1f(w, T_0)
    W_1_LOG = lf.W_1f(w_log, T_0)

    perform(t, v, w, 
            u, a, b, 
            c, d, T_0, 
            W_1, W_1_LOG, g_f=g_fun,
            name='First order linear filter',
            xl5=0, xl6=2.5)

if perform_W_2:
    a = 5
    b = 0
    c = 50
    d = 15

    g_fun = hr.get_g_f(t, t_1, t_2, a)
    u = hr.get_u(g_fun, t, b, c, d)

    T_1 = 0.001
    T_2 = 0.2
    T_3 = 0.3
    W_2 = lf.W_2f(w, T_1, T_2, T_3)
    W_2_LOG = lf.W_2f(w_log, T_1, T_2, T_3)

    perform(t, v, w, 
            u, a, b, 
            c, d, [T_1, T_2, T_3], 
            W_2, W_2_LOG, g_f=g_fun,
            name='Special filter',
            xl5=0, xl6=2.5)
