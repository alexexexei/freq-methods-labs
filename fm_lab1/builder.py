from sympy import plot, plot_parametric, re, im
from seaborn import set_theme, set_style

from calculations import calc_F_N, calc_G_N, calc_F_N_generic, calc_G_N_generic
from static import t


def configure_plot(stl: str):
    set_theme()
    set_style(stl, {'grid.linestyle': '--'})


configure_plot("whitegrid")


def build_f_t(f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
         axis_center=(ax1, ax2), xlim=(xl1, xl2), 
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_f_t_2(funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
         (funcs_t[1], (t,  gaps[1][0], gaps[1][1])), 
         axis_center=(ax1, ax2), xlim=(xl1, xl2), 
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_Re_f_t(funcs_t, gaps):
    plot((re(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
         (re(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
         (re(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
         (re(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
         xlabel=r'$t$', ylabel=r'Re$(f(t))$')


def build_Im_f_t(funcs_t, gaps):
    plot((im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
         (im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
         (im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
         (im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
         xlabel=r'$t$', ylabel=r'Im$(f(t))$')


def build_par_cf_t(funcs_t, gaps):
    plot_parametric((re(funcs_t[0]), im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
                    (re(funcs_t[1]), im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
                    (re(funcs_t[2]), im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
                    (re(funcs_t[3]), im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])), 
                    xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')


def build_F_N__f_t(N, f, f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    F_N = calc_F_N(N, gaps[0][0], gaps[-1][1], f)
    plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
         (F_N, (t, gaps[0][0], gaps[-1][1])), 
         axis_center=(ax1, ax2), xlim=(xl1, xl2),
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_F_N__f_t_2(N, funcs, funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    F_N = calc_F_N_generic(N, gaps, funcs)
    plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
         (funcs_t[1], (t, gaps[1][0], gaps[1][1])), 
         (F_N, (t, gaps[0][0], gaps[-1][1])),
         axis_center=(ax1, ax2), xlim=(xl1, xl2), 
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_G_N__f_t(N, f, f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    G_N = calc_G_N(N, gaps[0][0], gaps[-1][1], f)
    plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
         (G_N, (t, gaps[0][0], gaps[-1][1])), 
         axis_center=(ax1, ax2), xlim=(xl1, xl2), 
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_G_N__f_t_2(N, funcs, funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    G_N = calc_G_N_generic(N, gaps, funcs)
    plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
         (funcs_t[1], (t, gaps[1][0], gaps[1][1])), 
         (G_N, (t, gaps[0][0], gaps[-1][1])),
         axis_center=(ax1, ax2), xlim=(xl1, xl2), 
         ylim=(yl1, yl2), xlabel=r'$t$', 
         ylabel=r'$f(t)$')


def build_Re_G_N(N, funcs, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    plot((re(G_N), (t, gaps[0][0], gaps[-1][1])),
         xlabel=r'$t$', ylabel=r'Re$(G_{N}(t))$')


def build_Im_G_N(N, funcs, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    plot((im(G_N), (t, gaps[0][0], gaps[-1][1])),
         xlabel=r'$t$', ylabel=r'Im$(G_{N}(t))$')


def build_par_G_N__par_cf_t(N, funcs, funcs_t, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    plot_parametric((re(funcs_t[0]), im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
                    (re(funcs_t[1]), im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
                    (re(funcs_t[2]), im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
                    (re(funcs_t[3]), im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
                    (re(G_N), im(G_N), (t, gaps[0][0], gaps[-1][1])),
                    xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')
