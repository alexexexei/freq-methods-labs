from static import not_even_or_odd_periodic_func, t, gaps, gap_end_val, gap_len, pN, N, N_1, N_2, N_3, N_4, N_5
from builder import build_f_t, build_F_N__f_t, build_G_N__f_t
from finder import find_a_b_c, find_parseval

f_t = not_even_or_odd_periodic_func(t)

find_a_b_c(N, not_even_or_odd_periodic_func, gaps, gap_len)
find_parseval(pN, not_even_or_odd_periodic_func, f_t, gaps)

build_f_t(f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_F_N__f_t(N_1, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_F_N__f_t(N_2, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_F_N__f_t(N_3, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_F_N__f_t(N_4, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_F_N__f_t(N_5, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_G_N__f_t(N_1, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_G_N__f_t(N_2, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_G_N__f_t(N_3, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_G_N__f_t(N_4, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
build_G_N__f_t(N_5, not_even_or_odd_periodic_func, f_t, gaps, 0, gap_end_val + 1, 0, gap_end_val + 2, 0, 0)
