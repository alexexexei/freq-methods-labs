# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_1_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(task_1_dir)
from static import test_func, t, gaps, gap_start_val, gap_end_val

task_1_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(task_1_dir)
import calculations as calcs

import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_t = test_func(t)
N_0_1 = 15
N_0_2 = 50
N_0_3 = 60

def build_F_N__f_t(N):
    F_N = calcs.calc_F_N(N, gaps[0][0], gaps[-1][1], test_func)
    sp.plot((f_t, (t, gaps[0][0], gaps[-1][1])), (F_N, (t, gaps[0][0], gaps[-1][1])), 
            axis_center=(0, 0), xlim=(0, gap_start_val + gap_end_val), 
            ylim=(0, gap_end_val + 1), xlabel=r'$t$', ylabel=r'$f(t)$')

def build_G_N__f_t(N):
    G_N = calcs.calc_G_N(N, gaps[0][0], gaps[-1][1], test_func)
    sp.plot((f_t, (t, gaps[0][0], gaps[-1][1])), (G_N, (t, gaps[0][0], gaps[-1][1])), 
            axis_center=(0, 0), xlim=(0, gap_start_val + gap_end_val), 
            ylim=(0, gap_end_val + 1), xlabel=r'$t$', ylabel=r'$f(t)$')

build_F_N__f_t(N_0_1)
build_F_N__f_t(N_0_2)
build_F_N__f_t(N_0_3)
build_G_N__f_t(N_0_1)
build_G_N__f_t(N_0_2)
build_G_N__f_t(N_0_3)
