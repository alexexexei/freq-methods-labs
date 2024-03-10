# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_2_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(task_2_dir)
import calculations as calcs

from static import gap_1_cfunc, gap_2_cfunc, gap_3_cfunc, gap_4_cfunc, t, gaps, gap_len, N, N_1, N_2, N_3, N_4
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_c_1 = gap_1_cfunc(t)
f_c_2 = gap_2_cfunc(t)
f_c_3 = gap_3_cfunc(t)
f_c_4 = gap_4_cfunc(t)
funcs = [gap_1_cfunc, gap_2_cfunc, gap_3_cfunc, gap_4_cfunc]

def build_f_t():
    sp.plot_parametric((sp.re(f_c_1), sp.im(f_c_1), (t, gaps[0][0], gaps[0][1])),
                       (sp.re(f_c_2), sp.im(f_c_2), (t, gaps[1][0], gaps[1][1])),
                       (sp.re(f_c_3), sp.im(f_c_3), (t, gaps[2][0], gaps[2][1])),
                       (sp.re(f_c_4), sp.im(f_c_4), (t, gaps[3][0], gaps[3][1])), 
                       xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')
    
def build_G_N__f_t(N):
    G_N = calcs.calc_G_N_generic(N, gaps, funcs)
    sp.plot_parametric((sp.re(f_c_1), sp.im(f_c_1), (t, gaps[0][0], gaps[0][1])),
                       (sp.re(f_c_2), sp.im(f_c_2), (t, gaps[1][0], gaps[1][1])),
                       (sp.re(f_c_3), sp.im(f_c_3), (t, gaps[2][0], gaps[2][1])),
                       (sp.re(f_c_4), sp.im(f_c_4), (t, gaps[3][0], gaps[3][1])),
                       (sp.re(G_N), sp.im(G_N), (t, gaps[0][0], gaps[-1][1])),
                        xlabel=r'Re$(t)$', ylabel=r'Im$(t)$')
    
def build_Re_f_t():
    sp.plot((sp.re(f_c_1), (t, gaps[0][0], gaps[0][1])),
            (sp.re(f_c_2), (t, gaps[1][0], gaps[1][1])),
            (sp.re(f_c_3), (t, gaps[2][0], gaps[2][1])),
            (sp.re(f_c_4), (t, gaps[3][0], gaps[3][1])),
            xlabel=r'$t$', ylabel=r'Re$(f(t))$')

def build_Im_f_t():
    sp.plot((sp.im(f_c_1), (t, gaps[0][0], gaps[0][1])),
            (sp.im(f_c_2), (t, gaps[1][0], gaps[1][1])),
            (sp.im(f_c_3), (t, gaps[2][0], gaps[2][1])),
            (sp.im(f_c_4), (t, gaps[3][0], gaps[3][1])),
            xlabel=r'$t$', ylabel=r'Im$(f(t))$')

def build_Re_G_N(N):
    G_N = calcs.calc_G_N_generic(N, gaps, funcs)
    sp.plot((sp.re(G_N), (t, gaps[0][0], gaps[-1][1])),
            xlabel=r'$t$', ylabel=r'Re$(G_{N}(t))$')

def build_Im_G_N(N):
    G_N = calcs.calc_G_N_generic(N, gaps, funcs)
    sp.plot((sp.im(G_N), (t, gaps[0][0], gaps[-1][1])),
            xlabel=r'$t$', ylabel=r'Im$(G_{N}(t))$')

def sum_c_n(N, gaps, gap_len, funcs):
    c_n = sum(calcs.calc_c_n(N, gap[0], gap[1], gap_len, funcs[i]) for i, gap in enumerate(gaps))
    return c_n.evalf()

c_0 = sum_c_n(0, gaps, gap_len, funcs)
c_1 = sum_c_n(1, gaps, gap_len, funcs)
c_2 = sum_c_n(2, gaps, gap_len, funcs)
c_N = sum_c_n(N, gaps, gap_len, funcs)

print(f'c_0={c_0}\nc_1={c_1}\nc_2={c_2}\nc_{N}={c_N}\n')

build_f_t()
build_G_N__f_t(N_1)
build_G_N__f_t(N_2)
build_G_N__f_t(N_3)
build_G_N__f_t(N_4)
build_Re_f_t()
build_Im_f_t()
build_Re_G_N(N_1)
build_Re_G_N(N_2)
build_Re_G_N(N_3)
build_Re_G_N(N_4)
build_Im_G_N(N_1)
build_Im_G_N(N_2)
build_Im_G_N(N_3)
build_Im_G_N(N_4)
