from static import test_func, t, gaps, gap_start_val, gap_end_val
from builder import build_F_N__f_t, build_G_N__f_t

f_t = test_func(t)
N_0_1 = 15
N_0_2 = 50
N_0_3 = 60

build_F_N__f_t(N_0_1, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t(N_0_2, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
build_F_N__f_t(N_0_3, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t(N_0_1, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t(N_0_2, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
build_G_N__f_t(N_0_3, test_func, f_t, gaps, 0, gap_start_val + gap_end_val, 0, gap_end_val + 1, 0, 0)
