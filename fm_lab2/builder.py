from sympy.plotting import plot
from seaborn import set_theme, set_style
from finder import find_fimg

def configure_plot():
    set_theme()
    set_style("whitegrid", {'grid.linestyle': '--'})

configure_plot()

def build_f_t(f_t, clr, lbl):
    if (lbl == None):
        plot(f_t, line_color=clr, xlabel=r'$t$', ylabel=r'$f(t)$')
    else:
        plot(f_t, line_color=clr, xlabel=r'$t$', ylabel=r'$f(t)$', label=lbl, legend=True)

def build_fimg(f_t, intervals, clr, lbl):
    fimg = find_fimg(f_t, intervals[0], intervals[1])
    if (lbl == None):
        plot(fimg, line_color=clr, xlabel=r'$\omega$', ylabel=r'$c(\omega)$')
    else:
        plot(fimg, line_color=clr, xlabel=r'$\omega$', ylabel=r'$c(\omega)$', label=lbl, legend=True)
