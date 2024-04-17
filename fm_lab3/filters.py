import numpy as np


def flt_high(times: list, freqs: list, u: list, v_0):
    U = np.fft.fftshift(np.fft.fft(u))
    bool_list = [False] * len(U)
    for i in range(len(freqs)):
        if -v_0 <= freqs[i] <= v_0:
            bool_list[i] = True

    for j in range(len(U)):
        if not bool_list[j]:
            U[j] = 0

    flt_u = np.fft.ifft(np.fft.ifftshift(U))
    return flt_u, U
