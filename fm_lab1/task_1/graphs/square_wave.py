# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_1_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(task_1_dir)
from static import square_wave_a, square_wave_b, t, gaps, gap_end_val, gap_len, N, N_1, N_2, N_3, N_4, N_5

task_1_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(task_1_dir)
import calculations as calcs

import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_t_1 = square_wave_a(t)
f_t_2 = square_wave_b(t)
funcs = [square_wave_a, square_wave_b]

def build_f_t():
    sp.plot((f_t_1, (t, gaps[0][0], gaps[0][1])), (f_t_2, (t, gaps[1][0], gaps[1][1])), axis_center=(0, 0),
            xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel=r'$t$', ylabel=r'$f(t)$')

def build_F_N__f_t(N):
    F_N = calcs.calc_F_N_generic(N, gaps, funcs)
    sp.plot((f_t_1, (t, gaps[0][0], gaps[0][1])), (f_t_2, (t, gaps[1][0], gaps[1][1])), (F_N, (t, gaps[0][0], gaps[-1][1])),
            axis_center=(0, 0), xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel=r'$t$', ylabel=r'$f(t)$')

def build_G_N__f_t(N):
    G_N = calcs.calc_G_N_generic(N, gaps, funcs)
    sp.plot((f_t_1, (t, gaps[0][0], gaps[0][1])), (f_t_2, (t, gaps[1][0], gaps[1][1])), (G_N, (t, gaps[0][0], gaps[-1][1])),
            axis_center=(0, 0), xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel=r'$t$', ylabel=r'$f(t)$')

def sum_a_n(N, gaps, gap_len, funcs):
    a_n = sum(calcs.calc_a_n(N, gap[0], gap[1], gap_len, funcs[i]) for i, gap in enumerate(gaps))
    if (isinstance(a_n, int)):
        return a_n
    return a_n.evalf()

def sum_b_n(N, gaps, gap_len, funcs):
    b_n = sum(calcs.calc_b_n(N, gap[0], gap[1], gap_len, funcs[i]) for i, gap in enumerate(gaps))
    if (isinstance(b_n, int)):
        return b_n
    return b_n.evalf()

def sum_c_n(N, gaps, gap_len, funcs):
    c_n = sum(calcs.calc_c_n(N, gap[0], gap[1], gap_len, funcs[i]) for i, gap in enumerate(gaps))
    if (isinstance(c_n, int)):
        return c_n
    return c_n.evalf()

a_0 = sum_a_n(0, gaps, gap_len, funcs)
a_1 = sum_a_n(1, gaps, gap_len, funcs)
a_2 = sum_a_n(2, gaps, gap_len, funcs)
a_N = sum_a_n(N, gaps, gap_len, funcs)

b_0 = sum_b_n(0, gaps, gap_len, funcs)
b_1 = sum_b_n(1, gaps, gap_len, funcs)
b_2 = sum_b_n(2, gaps, gap_len, funcs)
b_N = sum_b_n(N, gaps, gap_len, funcs)

c_0 = sum_c_n(0, gaps, gap_len, funcs)
c_1 = sum_c_n(1, gaps, gap_len, funcs)
c_2 = sum_c_n(2, gaps, gap_len, funcs)
c_N = sum_c_n(N, gaps, gap_len, funcs)

print(f'a_0={a_0}\na_1={a_1}\na_2={a_2}\na_{N}={a_N}\n')
print(f'b_0={b_0}\nb_1={b_1}\nb_2={b_2}\nb_{N}={b_N}\n')
print(f'c_0={c_0}\nc_1={c_1}\nc_2={c_2}\nc_{N}={c_N}\n')

build_f_t()
build_F_N__f_t(N_1)
build_F_N__f_t(N_2)
build_F_N__f_t(N_3)
build_F_N__f_t(N_4)
build_F_N__f_t(N_5)
build_G_N__f_t(N_1)
build_G_N__f_t(N_2)
build_G_N__f_t(N_3)
build_G_N__f_t(N_4)
build_G_N__f_t(N_5)
