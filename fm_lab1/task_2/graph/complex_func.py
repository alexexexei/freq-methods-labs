# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_2_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(task_2_dir)

from static import gap_1_cfunc, gap_2_cfunc, gap_3_cfunc, gap_4_cfunc, t, gap_1, gap_2, gap_3, gap_4, gap_len, N, N_1, N_2, N_3, N_4
import calculations as calcs
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_c_1 = gap_1_cfunc(t)
f_c_2 = gap_2_cfunc(t)
f_c_3 = gap_3_cfunc(t)
f_c_4 = gap_4_cfunc(t)

