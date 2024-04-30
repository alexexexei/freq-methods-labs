import numpy as np

from help import get_U


def filter_U(u: list, freq: list, v_0, filter):
    flt_U = get_U(u)
    for i in range(len(freq)):
        freq_i = freq[i]
        if filter(freq_i, v_0):
            flt_U[i] = 0

    return flt_U


def low_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return False
    return True


def high_filter(freq, v_0):
    return not low_filter(freq, v_0)


def special_filter_in(freq, v_0: list):
    for i in range(len(v_0)):
        if v_0[i][0] <= freq <= v_0[i][1]:
            return False
    return True


def special_filter_out(freq, v_0: list):
    return not special_filter_in(freq, v_0)


def filter_low(freq: list, u: list, v_0):
    if isinstance(v_0, list) or \
            len(freq) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freq, v_0, low_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_high(freq: list, u: list, v_0):
    if isinstance(v_0, list) or \
            len(freq) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freq, v_0, high_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_special_in(freq: list, u: list, v_0: list):
    if not isinstance(v_0, list) or \
            len(v_0) <= 0 or \
            len(freq) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freq, v_0, special_filter_in)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_special_out(freq: list, u: list, v_0: list):
    if not isinstance(v_0, list) or \
            len(v_0) <= 0 or \
            len(freq) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freq, v_0, special_filter_out)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U
