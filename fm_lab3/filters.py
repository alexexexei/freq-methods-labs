import numpy as np


def get_U(u):
    return np.fft.fftshift(np.fft.fft(u))


def filter_U(u: list, freqs: list, v_0, filter):
    U = get_U(u)
    for i in range(len(freqs)):
        freq = freqs[i]
        if not filter(freq, v_0):
            U[i] = 0

    return U


def high_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return True
    return False


def low_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return False
    return True


def filter_high(freqs: list, u: list, v_0):
    U = filter_U(u, freqs, v_0, high_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(U))
    return flt_u, U


def filter_low(freqs: list, u: list, v_0):
    U = filter_U(u, freqs, v_0, low_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(U))
    return flt_u, U
