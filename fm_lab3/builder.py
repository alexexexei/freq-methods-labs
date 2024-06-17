import matplotlib.pyplot as plt
import numpy as np

from help import get_U


def build_u_to_U(freq: list,
                 u: list,
                 clr='b',
                 xl1=None,
                 xl2=None,
                 yl1=None,
                 yl2=None,
                 xlab='Frequency',
                 ylab='Amplitude',
                 label=None,
                 title=None,
                 fz1=6.4,
                 fz2=4.8,
                 legend: bool = True,
                 grid: bool = True):
    U = get_U(u)
    build_u_or_U(freq, U, clr, xl1, xl2, yl1, yl2, xlab, ylab, label, title,
                 fz1, fz2, legend, grid)


def build_u_or_U(torv: list,
                 uorU: list,
                 clr='b',
                 xl1=None,
                 xl2=None,
                 yl1=None,
                 yl2=None,
                 xlab=None,
                 ylab='Amplitude',
                 label=None,
                 title=None,
                 fz1=6.4,
                 fz2=4.8,
                 legend: bool = True,
                 grid: bool = True):
    plt.plot(torv, uorU, color=clr, label=label)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(title)
    if legend:
        plt.legend()
    plt.grid(grid)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.show()


def build_u__flt_u(time: list,
                   u: list,
                   flt_u: list,
                   clr1='b',
                   clr2='r',
                   lab1='Noisy signal',
                   lab2='Filtered signal',
                   xlab='Time',
                   ylab='Amplitude',
                   title=None,
                   fz1=6.4,
                   fz2=4.8,
                   legend: bool = True,
                   grid: bool = True,
                   xl1=None,
                   xl2=None,
                   yl1=None,
                   yl2=None):
    plt.plot(time, u, color=clr1, label=lab1)
    plt.plot(time, flt_u, color=clr2, label=lab2)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(title)
    if legend:
        plt.legend()
    plt.grid(grid)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.show()


def build_abs_u_to_U__flt_U(freq: list,
                            u: list,
                            flt_U: list,
                            clr1='b',
                            clr2='r',
                            lab1='Abs noisy signal',
                            lab2='Abs filtered signal',
                            xlab='Frequency',
                            ylab='Amplitude',
                            xl1=None,
                            xl2=None,
                            yl1=None,
                            yl2=None,
                            title=None,
                            fz1=6.4,
                            fz2=4.8,
                            legend: bool = True,
                            grid: bool = True):
    U = get_U(u)
    build_abs_U__flt_U(freq, U, flt_U, clr1,
                       clr2, lab1, lab2, xlab,
                       ylab, xl1, xl2, yl1, yl2,
                       title, fz1, fz2, legend, grid)


def build_abs_U__flt_U(freq: list,
                       U: list,
                       flt_U: list,
                       clr1='b',
                       clr2='r',
                       lab1='Abs noisy signal',
                       lab2='Abs filtered signal',
                       xlab='Frequency',
                       ylab='Amplitude',
                       xl1=None,
                       xl2=None,
                       yl1=None,
                       yl2=None,
                       title=None,
                       fz1=6.4,
                       fz2=4.8,
                       legend: bool = True,
                       grid: bool = True):
    plt.plot(freq, np.abs(U), color=clr1, label=lab1)
    plt.plot(freq, np.abs(flt_U), color=clr2, label=lab2)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(title)
    if legend:
        plt.legend()
    plt.grid(grid)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.show()
