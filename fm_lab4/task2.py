import numpy as np

import build_func as bf


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


def fft_flt(u, W, shift):
    U = np.fft.fft(u)
    flt_U = None
    if shift:
        flt_U = np.fft.fftshift(W) * U
    else:
        flt_U = W * U
    flt_u = np.fft.ifft(flt_U)
    return flt_u, flt_U, U


def perform(t, v, w, 
            u, a, b, 
            c, d, T, 
            W, LAFR, g_f=None, 
            shift=True, name='Filter'):
    flt_u, flt_U, U = fft_flt(u, W, shift)

    sh_abs_U = abs(np.fft.fftshift(U))
    sh_abs_flt_U = abs(np.fft.fftshift(flt_U))
    flist1 = [u, flt_u.real]
    flist2 = [sh_abs_U, sh_abs_flt_U]
    llist1 = ['Original signal', 'Filtered signal']
    llist2 = ['Abs original signal fft', 'Abs filtered signal fft']
    lslist = ['-', '-']
    clist = [None, None]
    abs_W = abs(W)
    log_w = np.log10(w[w > 0])
    if g_f is not None:
        flist1.append(g_f)
        llist1.append(r'Original function $g(t)$')
        lslist.append('--')
        clist.append('r')

    bf.build_fs(t, y=flist1, labels=llist1, colors=clist, ls=lslist,
                ttl=f'{name}. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Time', ylab='Amplitude', legend=True)
    bf.build_fs(v, y=flist2, labels=llist2, 
                ttl=f'{name} abs fft. a={a}, b={b}, c={c}, d={d}, T={T}', 
                xlab='Frequency', ylab='Amplitude', legend=True)
    bf.build_f(w, y=abs_W, ttl=f'{name} amplitude-frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               xlab='Angular frequency', ylab='Amplitude-frequency response', xl1=0, xl2=50)
    bf.build_f(log_w, y=LAFR, ttl=f'{name} logarithmic amplitude frequency response. a={a}, b={b}, c={c}, d={d}, T={T}',
               ylab='Amplitude', xl1=0)


if __name__=='__main__':
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

    perform_W_1 = True
    perform_W_2 = True


    if perform_W_1:
        a = 1
        b = 0.6
        c = 0
        d = 0.7

        g_fun = get_g_f(t, t_1, t_2, a)
        u = get_u(g_fun, t, b, c, d)

        T_0 = 1
        W_1 = W_1f(w, T_0)
        W_1_LOG = W_1f(w_log, T_0)
        LAFR = get_LAFR(W_1_LOG)

        perform(t, v, w, 
                u, a, b, 
                c, d, T_0, 
                W_1, LAFR, g_f=g_fun,
                name='First order linear filter')


    if perform_W_2:
        a = 3
        b = 0
        c = 5
        d = 15

        g_fun = get_g_f(t, t_1, t_2, a)
        u = get_u(g_fun, t, b, c, d)

        T_1 = 1
        T_2 = 2+np.sqrt(2)
        T_3 = 2-np.sqrt(2)
        W_2 = W_2f(w, T_1, T_2, T_3)
        W_2_LOG = W_2f(w_log, T_1, T_2, T_3)
        LAFR = get_LAFR(W_2_LOG)

        perform(t, v, w, 
                u, a, b, 
                c, d, [T_1, T_2, T_3], 
                W_2, LAFR, g_f=g_fun, 
                shift=False, name='Special filter')