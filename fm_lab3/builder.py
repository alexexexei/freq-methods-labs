import matplotlib.pyplot as plt
import numpy as np


def build_u__flt_u(times: list, u: list, flt_u: list, clr1=None, clr2=None, title=None):
    plt.plot(times, u, color=clr1, label='Noisy signal')
    plt.plot(times, flt_u, color=clr2, label='Filtered signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def build_abs_u__flt_u(times: list, u: list, flt_u: list, clr1=None, clr2=None, title=None):
    plt.plot(times, np.abs(np.fft.fftshift(np.fft.fft(u))), color=clr1, label='Abs noisy signal')
    plt.plot(times, np.abs(flt_u), color=clr2, label='Abs filtered signal')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xlim(0, times[-1])
    plt.ylim(0, 200)
    plt.show()
