from sympy import plot, re, im, Abs
from numpy import arange

import matplotlib.pyplot as plt
from seaborn import set_theme, set_style

from finder import find_fimg


def configure_plot(stl: str):
    set_theme()
    set_style(stl, {'grid.linestyle': '--'})


configure_plot("whitegrid")


def build_f_t(f_t, clr, lbl):
    if (lbl == None):
        plot(f_t, line_color=clr, xlabel=r'$t$', ylabel=r'$f(t)$')
    else:
        plot(f_t, line_color=clr, xlabel=r'$t$', ylabel=r'$f(t)$', label=lbl, legend=True)


def build_f_t_rec(fs: list, clr, lbls: list):
    for i in range(len(fs)):
        build_f_t(fs[i], clr, lbls[i])


def build_fimg(f_t, interval: list, clr, lbl):
    fimg = find_fimg(f_t, interval[0], interval[1])
    build_fimg2(fimg, clr, lbl)


def build_fimg2(fimg, clr, lbl):
    if (lbl == None):
        plot(fimg, line_color=clr, xlabel=r'$\omega$', ylabel=r'$c(\omega)$')
    else:
        plot(fimg, line_color=clr, xlabel=r'$\omega$', ylabel=r'$c(\omega)$', label=lbl, legend=True)


def build_fimg2_rec(fimgs: list, clr, lbls: list):
    for i in range(len(fimgs)):
        build_fimg2(fimgs[i], clr, lbls[i])


def build_re_shfimg(shfimg, clr, lbl):
    if (lbl == None):
        plot(re(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'Re$\hat{g}(\omega)$')
    else:
        plot(re(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'Re$\hat{g}(\omega)$', label=lbl, legend=True)


def build_re_shfimg_rec(shfimgs: list, clr, lbls: list):
    for i in range(len(shfimgs)):
        build_re_shfimg(shfimgs[i], clr, lbls[i])


def build_im_shfimg(shfimg, clr, lbl):
    if (lbl == None):
        plot(im(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'Im$\hat{g}(\omega)$')
    else:
        plot(im(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'Im$\hat{g}(\omega)$', label=lbl, legend=True)


def build_im_shfimg_rec(shfimgs: list, clr, lbls: list):
    for i in range(len(shfimgs)):
        build_im_shfimg(shfimgs[i], clr, lbls[i])


def build_re_im_shfimg(shfimg, clr1, clr2, lbl):
    if (lbl == None):
        p = plot(re(shfimg), line_color=clr1, show=False, xlabel=r'$\omega$', ylabel=r'$\hat{g}(\omega)$')
        p.extend(plot(im(shfimg), line_color=clr2, show=False))
        p.show()
    else:
        p = plot(re(shfimg), line_color=clr1, show=False, xlabel=r'$\omega$', ylabel=r'$\hat{g}(\omega)$', label=lbl, legend=True)
        p.extend(plot(im(shfimg), line_color=clr2, show=False, legend=True))
        p.show()


def build_re_im_shfimg_rec(shfimgs: list, clr1, clr2, lbls: list):
    for i in range(len(shfimgs)):
        build_re_im_shfimg(shfimgs[i], clr1, clr2, lbls[i])


def build_abs_shfimg(shfimg, clr, lbl):
    if (lbl == None):
        plot(Abs(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'$|\hat{g}(\omega)|$')
    else:
        plot(Abs(shfimg), line_color=clr, xlabel=r'$\omega$', ylabel=r'$|\hat{g}(\omega)$|', label=lbl, legend=True)

    
def build_abs_shfimg_rec(shfimgs: list, clr, lbls: list):
    for i in range(len(shfimgs)):
        build_abs_shfimg(shfimgs[i], clr, lbls[i])


def build_audio_f_t(t, y, clr=None):
    if (clr != None):
        plt.plot(t, y, color=clr)
    else:
        plt.plot(t, y)

    plt.xlabel(r'$t$')
    plt.ylabel(r'$f(t)$')
    plt.grid(True)
    plt.show()


def build_audio_f_v(freqs, ampls, start=None, stop=None, step=None, fz1=None, fz2=None, clr=None):
    if ((fz1 != None) and (fz2 != None)):
        plt.figure(figsize=(fz1, fz2))

    if (clr != None):
        plt.plot(freqs, ampls, color=clr)
    else:
        plt.plot(freqs, ampls)

    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\left|\hat{f}\left(\nu\right)\right|$')
    plt.grid(True)
    if ((start != None) and (stop != None and stop != 0) and (step != None and step != 0)):
        plt.xticks(arange(start, stop, step))
    plt.show()
    