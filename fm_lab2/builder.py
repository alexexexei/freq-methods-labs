from sympy.plotting import plot
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
