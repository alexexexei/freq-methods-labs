# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_2_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(task_2_dir)

from static import R, T, t, gap_1, gap_2, gap_3, gap_4, gap_len
import calculations as calcs
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_c_1 = R + (8 * R * t / T) * 1j
f_c_2 = 2 * R - (8 * R * t / T) + R * 1j
f_c_3 = -R + (4 * R - (8 * R * t / T)) * 1j
f_c_4 = -6 * R + (8 * R * t / T) - R * 1j

