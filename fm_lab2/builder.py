from sympy import plot, re, im, Abs
from numpy import arange

import matplotlib.pyplot as plt
from seaborn import set_theme, set_style

from finder import find_fimg


def configure_plot(stl: str):
    set_theme()
    set_style(stl, {'grid.linestyle': '--'})


configure_plot("whitegrid")


def build_f_t(f_t, ax1=None, ax2=None, clr=None, lbl=None):
    if (ax1 == None or ax2 == None):
        ax1, ax2 = 0, 0

    if (lbl == None):
        plot(f_t,
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$t$',
             ylabel=r'$f(t)$')
    else:
        plot(f_t,
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$t$',
             ylabel=r'$f(t)$',
             label=lbl,
             legend=True)


def build_f_t_rec(fs: list, ax1=None, ax2=None, clr=None, lbls: list = None):
    if (len(fs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(fs)

    for i in range(len(fs)):
        build_f_t(fs[i], ax1, ax2, clr, lbls[i])


def build_fimg(f_t,
               interval: list,
               ax1=None,
               ax2=None,
               xl1=None,
               xl2=None,
               yl1=None,
               yl2=None,
               clr=None,
               lbl=None):
    if (len(interval) <= 0):
        return

    fimg = find_fimg(f_t, interval[0], interval[1])
    build_fimg2(fimg, ax1, ax2, xl1, xl2, yl1, yl2, clr, lbl)


def build_fimg2(fimg,
                ax1=None,
                ax2=None,
                xl1=None,
                xl2=None,
                yl1=None,
                yl2=None,
                clr=None,
                lbl=None):
    if (ax1 == None or ax2 == None):
        ax1, ax2 = 0, 0

    if lbl is None:
        if xl1 != None and xl2 != None and yl1 != None and yl2 != None:
            plot(fimg,
                 xlim=(xl1, xl2),
                 ylim=(yl1, yl2),
                 line_color=clr,
                 xlabel=r'$\omega$',
                 ylabel=r'$c(\omega)$')
        else:
            plot(fimg,
                 line_color=clr,
                 xlabel=r'$\omega$',
                 ylabel=r'$c(\omega)$')
    else:
        if xl1 != None and xl2 != None and yl1 != None and yl2 != None:
            plot(fimg,
                 xlim=(xl1, xl2),
                 ylim=(yl1, yl2),
                 line_color=clr,
                 xlabel=r'$\omega$',
                 ylabel=r'$c(\omega)$',
                 label=lbl,
                 legend=True)
        else:
            plot(fimg,
                 line_color=clr,
                 xlabel=r'$\omega$',
                 ylabel=r'$c(\omega)$',
                 label=lbl,
                 legend=True)


def build_fimg2_rec(fimgs: list,
                    ax1=None,
                    ax2=None,
                    xl1=None,
                    xl2=None,
                    yl1=None,
                    yl2=None,
                    clr=None,
                    lbls: list = None):
    if (len(fimgs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(fimgs)

    for i in range(len(fimgs)):
        build_fimg2(fimgs[i],
                    ax1,
                    ax2,
                    xl1,
                    xl2,
                    yl1,
                    yl2,
                    clr=clr,
                    lbl=lbls[i])


def build_re_shfimg(shfimg, ax1=None, ax2=None, clr=None, lbl=None):
    if (ax1 == None or ax2 == None):
        ax1, ax2 = 0, 0

    if (lbl == None):
        plot(re(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'Re$\hat{g}(\omega)$')
    else:
        plot(re(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'Re$\hat{g}(\omega)$',
             label=lbl,
             legend=True)


def build_re_shfimg_rec(shfimgs: list,
                        ax1=None,
                        ax2=None,
                        clr=None,
                        lbls: list = None):
    if (len(shfimgs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(shfimgs)

    for i in range(len(shfimgs)):
        build_re_shfimg(shfimgs[i], ax1, ax2, clr, lbls[i])


def build_im_shfimg(shfimg, ax1=None, ax2=None, clr=None, lbl=None):
    if (ax1 == None or ax2 == None):
        ax1, ax2 = 0, 0

    if (lbl == None):
        plot(im(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'Im$\hat{g}(\omega)$')
    else:
        plot(im(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'Im$\hat{g}(\omega)$',
             label=lbl,
             legend=True)


def build_im_shfimg_rec(shfimgs: list,
                        ax1=None,
                        ax2=None,
                        clr=None,
                        lbls: list = None):
    if (len(shfimgs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(shfimgs)

    for i in range(len(shfimgs)):
        build_im_shfimg(shfimgs[i], ax1, ax2, clr, lbls[i])


def build_re_im_shfimg(shfimg, clr1=None, clr2=None, lbl=None):
    if (lbl == None):
        p = plot(re(shfimg),
                 line_color=clr1,
                 show=False,
                 xlabel=r'$\omega$',
                 ylabel=r'$\hat{g}(\omega)$')
        p.extend(plot(im(shfimg), line_color=clr2, show=False))
        p.show()
    else:
        p = plot(re(shfimg),
                 line_color=clr1,
                 show=False,
                 xlabel=r'$\omega$',
                 ylabel=r'$\hat{g}(\omega)$',
                 label=lbl,
                 legend=True)
        p.extend(plot(im(shfimg), line_color=clr2, show=False, legend=True))
        p.show()


def build_re_im_shfimg_rec(shfimgs: list,
                           clr1=None,
                           clr2=None,
                           lbls: list = None):
    if (len(shfimgs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(shfimgs)

    for i in range(len(shfimgs)):
        build_re_im_shfimg(shfimgs[i], clr1, clr2, lbls[i])


def build_abs_shfimg(shfimg, ax1=None, ax2=None, clr=None, lbl=None):
    if (ax1 == None or ax2 == None):
        ax1, ax2 = 0, 0

    if (lbl == None):
        plot(Abs(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'$|\hat{g}(\omega)|$')
    else:
        plot(Abs(shfimg),
             axis_center=(ax1, ax2),
             line_color=clr,
             xlabel=r'$\omega$',
             ylabel=r'$|\hat{g}(\omega)$|',
             label=lbl,
             legend=True)


def build_abs_shfimg_rec(shfimgs: list,
                         ax1=None,
                         ax2=None,
                         clr=None,
                         lbls: list = None):
    if (len(shfimgs) <= 0):
        return

    if (lbls == None):
        lbls = [None] * len(shfimgs)

    for i in range(len(shfimgs)):
        build_abs_shfimg(shfimgs[i], ax1, ax2, clr, lbls[i])


def build_audio_f_t(t, y, clr=None):
    plt.plot(t, y, color=clr)
    plt.xlabel(r'$t$')
    plt.ylabel(r'$f(t)$')
    plt.grid(True)
    plt.show()


def build_audio_f_v(freqs,
                    ampls,
                    start=None,
                    stop=None,
                    step=None,
                    fz1=None,
                    fz2=None,
                    clr=None):
    if ((fz1 != None) and (fz2 != None)):
        plt.figure(figsize=(fz1, fz2))

    plt.plot(freqs, ampls, color=clr)
    plt.xlabel(r'$\nu$')
    plt.ylabel(r'$\left|\hat{f}\left(\nu\right)\right|$')
    plt.grid(True)
    if ((start != None) and (stop != None and stop != 0)
            and (step != None and step != 0)):
        plt.xticks(arange(start, stop, step))
    plt.show()
