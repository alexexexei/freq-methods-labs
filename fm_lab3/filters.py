import numpy as np

from help import get_U


def filter_U(u: list, freqs: list, v_0, filter):
    flt_U = get_U(u)
    for i in range(len(freqs)):
        freq = freqs[i]
        if not filter(freq, v_0):
            flt_U[i] = 0

    return flt_U


def high_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return True
    return False


def low_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return False
    return True


def filter_high(freqs: list, u: list, v_0):
    flt_U = filter_U(u, freqs, v_0, high_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_low(freqs: list, u: list, v_0):
    flt_U = filter_U(u, freqs, v_0, low_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U
