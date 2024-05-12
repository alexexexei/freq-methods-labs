import numpy as np


def trapz(y, t, v):
    Y = []
    for k in v:
        Y_k = np.trapz(y * np.exp(-1j * 2 * np.pi * k * t), t)
        Y.append(Y_k)
    return Y


def undo_trapz(Y, t, v):
    y = []
    for k in t:
        y_k = np.trapz(Y * np.exp(1j * 2 * np.pi * k * v), v)
        y.append(y_k)
    return y


def numerical_diff(y, dt):
    ndiff = []
    for k in range(len(y) - 1):
        ndiff_k = (y[k + 1] - y[k]) / dt
        ndiff.append(ndiff_k)
    return ndiff


def spectral_diff(y, t, v):
    Y = trapz(y, t, v)
    dY = 2 * np.pi * 1j * v * Y
    spdiff = undo_trapz(dY, t, v)
    return spdiff, Y, dY


def fft_flt(u, W, shift=True):
    U = np.fft.fft(u)
    maybe_shifted_U = U
    if shift:
        maybe_shifted_U = np.fft.fftshift(U)

    flt_U = W * maybe_shifted_U
    maybe_shifted_flt_U = flt_U
    if shift:
        maybe_shifted_flt_U = np.fft.ifftshift(flt_U)

    flt_u = np.fft.ifft(maybe_shifted_flt_U)
    return flt_u, maybe_shifted_flt_U, U


def get_AFR(W):
    return np.abs(W)


def get_LAFR(W):
    return 20 * np.log10(get_AFR(W))
