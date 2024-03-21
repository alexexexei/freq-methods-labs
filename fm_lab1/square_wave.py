from static import square_wave_a, square_wave_b, t, gaps, gap_end_val, gap_len, pN, N, N_1, N_2, N_3, N_4, N_5
from builder import build_f_t_2, build_F_N__f_t_2, build_G_N__f_t_2
from finder import find_a_b_c_2, find_parseval_gen

f_t_1 = square_wave_a(t)
f_t_2 = square_wave_b(t)
funcs = [square_wave_a, square_wave_b]
funcs_t = [f_t_1, f_t_2]

find_a_b_c_2(N, gaps, gap_len, funcs)
find_parseval_gen(pN, gaps, funcs, funcs_t)

build_f_t_2(f_t_1, f_t_2, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t_2(N_1, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t_2(N_2, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t_2(N_3, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t_2(N_4, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t_2(N_5, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t_2(N_1, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t_2(N_2, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t_2(N_3, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t_2(N_4, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t_2(N_5, funcs, funcs_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 1, 0, 0)
