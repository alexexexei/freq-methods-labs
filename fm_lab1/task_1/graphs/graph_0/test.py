# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_1_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(task_1_dir)

from static import test_func, t, gap_start, gap_start_val, gap_end, gap_end_val
import calculations as calcs
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_t = test_func(t)
N = 15

def build_F_N__f_t(N):
    F_N = calcs.calc_F_N(N, gap_start, gap_end, test_func)
    sp.plot((f_t, (t, gap_start, gap_end)), (F_N, (t, gap_start, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_start_val + gap_end_val), ylim=(0, gap_end_val + 1), xlabel='t', ylabel='f(t)')

def build_G_N__f_t(N):
    G_N = calcs.calc_G_N(N, gap_start, gap_end, test_func)
    sp.plot((f_t, (t, gap_start, gap_end)), (G_N, (t, gap_start, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_start_val + gap_end_val), ylim=(0, gap_end_val + 1), xlabel='t', ylabel='f(t)')
    
build_F_N__f_t(N)
build_G_N__f_t(N)
