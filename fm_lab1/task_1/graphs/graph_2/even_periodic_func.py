# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_1_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(task_1_dir)

from static import even_periodic_func, t, gap_start, gap_end, gap_end_val, gap_length, N, N_1, N_2, N_3, N_4, N_5
import calculations as calcs
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_t = sp.cos(t)

def build_f_t():
    sp.plot((f_t, (t, gap_start, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_end_val + 1), ylim=(-1.5, 1.5), xlabel='t', ylabel='f(t)')

def build_F_N__f_t(N):
    F_N = calcs.calc_F_N(N, gap_start, gap_end, even_periodic_func)
    sp.plot((f_t, (t, gap_start, gap_end)), (F_N, (t, gap_start, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_end_val + 1), ylim=(-1.5, 1.5), xlabel='t', ylabel='f(t)')

def build_G_N__f_t(N):
    G_N = calcs.calc_G_N(N, gap_start, gap_end, even_periodic_func)
    sp.plot((f_t, (t, gap_start, gap_end)), (G_N, (t, gap_start, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_end_val + 1), ylim=(-1.5, 1.5), xlabel='t', ylabel='f(t)')
    
# TODO do parseval equality

a_N = calcs.calc_a_n(N, gap_start, gap_end, gap_length, even_periodic_func)
if (not isinstance(a_N, int)):
    a_N = a_N.evalf()

b_N = calcs.calc_b_n(N, gap_start, gap_end, gap_length, even_periodic_func)
if (not isinstance(b_N, int)):
    b_N = b_N.evalf()

c_N = calcs.calc_c_n(N, gap_start, gap_end, gap_length, even_periodic_func)
if (not isinstance(c_N, int)):
    c_N = c_N.evalf()

print(f'a_{N}={a_N}')
print(f'b_{N}={b_N}')
print(f'c_{N}={c_N}')

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
