import sympy as sp
import seaborn as sns
from static import t
from calculations import calc_F_N, calc_G_N, calc_F_N_generic, calc_G_N_generic

def configure_plot():
    sns.set_theme()
    sns.set_style("whitegrid", {'grid.linestyle': '--'})

configure_plot()

def build_f_t(f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    sp.plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
            axis_center=(ax1, ax2), xlim=(xl1, xl2), 
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')
    
def build_f_t_2(funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    sp.plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
            (funcs_t[1], (t,  gaps[1][0], gaps[1][1])), 
            axis_center=(ax1, ax2), xlim=(xl1, xl2), 
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')
    
def build_Re_f_t(funcs_t, gaps):
    sp.plot((sp.re(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
            (sp.re(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
            (sp.re(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
            (sp.re(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
            xlabel=r'$t$', ylabel=r'Re$(f(t))$')

def build_Im_f_t(funcs_t, gaps):
    sp.plot((sp.im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
            (sp.im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
            (sp.im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
            (sp.im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
            xlabel=r'$t$', ylabel=r'Im$(f(t))$')

def build_par_cf_t(funcs_t, gaps):
    sp.plot_parametric((sp.re(funcs_t[0]), sp.im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
                       (sp.re(funcs_t[1]), sp.im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
                       (sp.re(funcs_t[2]), sp.im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
                       (sp.re(funcs_t[3]), sp.im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])), 
                       xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')

def build_F_N__f_t(N, f, f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    F_N = calc_F_N(N, gaps[0][0], gaps[-1][1], f)
    sp.plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
            (F_N, (t, gaps[0][0], gaps[-1][1])), 
            axis_center=(ax1, ax2), xlim=(xl1, xl2),
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')
    
def build_F_N__f_t_2(N, funcs, funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    F_N = calc_F_N_generic(N, gaps, funcs)
    sp.plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
            (funcs_t[1], (t, gaps[1][0], gaps[1][1])), 
            (F_N, (t, gaps[0][0], gaps[-1][1])),
            axis_center=(ax1, ax2), xlim=(xl1, xl2), 
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')

def build_G_N__f_t(N, f, f_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    G_N = calc_G_N(N, gaps[0][0], gaps[-1][1], f)
    sp.plot((f_t, (t, gaps[0][0], gaps[-1][1])), 
            (G_N, (t, gaps[0][0], gaps[-1][1])), 
            axis_center=(ax1, ax2), xlim=(xl1, xl2), 
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')

def build_G_N__f_t_2(N, funcs, funcs_t, gaps, xl1, xl2, yl1, yl2, ax1, ax2):
    G_N = calc_G_N_generic(N, gaps, funcs)
    sp.plot((funcs_t[0], (t, gaps[0][0], gaps[0][1])), 
            (funcs_t[1], (t, gaps[1][0], gaps[1][1])), 
            (G_N, (t, gaps[0][0], gaps[-1][1])),
            axis_center=(ax1, ax2), xlim=(xl1, xl2), 
            ylim=(yl1, yl2), xlabel=r'$t$', 
            ylabel=r'$f(t)$')

def build_Re_G_N(N, funcs, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    sp.plot((sp.re(G_N), (t, gaps[0][0], gaps[-1][1])),
            xlabel=r'$t$', ylabel=r'Re$(G_{N}(t))$')

def build_Im_G_N(N, funcs, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    sp.plot((sp.im(G_N), (t, gaps[0][0], gaps[-1][1])),
            xlabel=r'$t$', ylabel=r'Im$(G_{N}(t))$')

def build_par_G_N__par_cf_t(N, funcs, funcs_t, gaps):
    G_N = calc_G_N_generic(N, gaps, funcs)
    sp.plot_parametric((sp.re(funcs_t[0]), sp.im(funcs_t[0]), (t, gaps[0][0], gaps[0][1])),
                       (sp.re(funcs_t[1]), sp.im(funcs_t[1]), (t, gaps[1][0], gaps[1][1])),
                       (sp.re(funcs_t[2]), sp.im(funcs_t[2]), (t, gaps[2][0], gaps[2][1])),
                       (sp.re(funcs_t[3]), sp.im(funcs_t[3]), (t, gaps[3][0], gaps[3][1])),
                       (sp.re(G_N), sp.im(G_N), (t, gaps[0][0], gaps[-1][1])),
                        xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')
