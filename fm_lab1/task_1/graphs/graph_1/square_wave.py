# script for import
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_1_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(task_1_dir)

from static import square_wave_a, square_wave_b, t, gap_start, gap_mid, gap_end, gap_end_val, N, N_1, N_2, N_3, N_4, N_5
import calculations as calcs
import sympy as sp
import seaborn as sns

sns.set_theme()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

f_t_1 = square_wave_a(t)
f_t_2 = square_wave_b(t)

def build_f_t():
    sp.plot((f_t_1, (t, gap_start, gap_mid)), (f_t_2, (t, gap_mid, gap_end)), axis_center=(0, 0),
            xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel='t', ylabel='f(t)')

def build_F_N__f_t(N):
    F_N = calcs.calc_F_N_sys2(N, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
    sp.plot((f_t_1, (t, gap_start, gap_mid)), (f_t_2, (t, gap_mid, gap_end)), (F_N, (t, gap_start, gap_end)),
            axis_center=(0, 0), xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel='t', ylabel='f(t)')

def build_G_N__f_t(N):
    G_N = calcs.calc_G_N_sys2(N, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
    sp.plot((f_t_1, (t, gap_start, gap_mid)), (f_t_2, (t, gap_mid, gap_end)), (G_N, (t, gap_start, gap_end)),
            axis_center=(0, 0), xlim=(0, gap_end_val + 1), ylim=(0, gap_end_val + 1), xlabel='t', ylabel='f(t)')

# TODO do parseval equality

def sum_a_n(N, start_1, end_1, start_2, end_2, f_1, f_2):
    gap_length = end_2 - start_1
    a_n_1 = calcs.calc_a_n(N, start_1, end_1, gap_length, f_1)
    a_n_2 = calcs.calc_a_n(N, start_2, end_2, gap_length, f_2)
    a_n = a_n_1 + a_n_2

    if (isinstance(a_n, int)):
        return a_n
    return a_n.evalf()

def sum_b_n(N, start_1, end_1, start_2, end_2, f_1, f_2):
    gap_length = end_2 - start_1
    b_n_1 = calcs.calc_b_n(N, start_1, end_1, gap_length, f_1)
    b_n_2 = calcs.calc_b_n(N, start_2, end_2, gap_length, f_2)
    b_n = b_n_1 + b_n_2

    if (isinstance(b_n, int)):
        return b_n
    return b_n.evalf()

def sum_c_n(N, start_1, end_1, start_2, end_2, f_1, f_2):
    gap_length = end_2 - start_1
    c_n_1 = calcs.calc_c_n(N, start_1, end_1, gap_length, f_1)
    c_n_2 = calcs.calc_c_n(N, start_2, end_2, gap_length, f_2)
    c_n = c_n_1 + c_n_2
    
    if (isinstance(c_n, int)):
        return c_n
    return c_n.evalf()

a_0 = sum_a_n(0, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
a_1 = sum_a_n(1, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
a_2 = sum_a_n(2, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
a_N = sum_a_n(N, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)

b_0 = sum_b_n(0, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
b_1 = sum_b_n(1, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
b_2 = sum_b_n(2, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
b_N = sum_b_n(N, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)

c_0 = sum_c_n(0, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
c_1 = sum_c_n(1, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
c_2 = sum_c_n(2, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)
c_N = sum_c_n(N, gap_start, gap_mid, gap_mid, gap_end, square_wave_a, square_wave_b)

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
