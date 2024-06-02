from static2 import gap_1_cfunc, gap_2_cfunc, gap_3_cfunc, gap_4_cfunc, t, gaps, gap_len, pN, N, N_1, N_2, N_3, N_4
from builder import build_par_cf_t, build_par_G_N__par_cf_t, build_re_f_t, build_im_f_t, build_re_G_N, build_im_G_N
from finder import find_c_gen, find_parseval_gen


funcs = [gap_1_cfunc, gap_2_cfunc, gap_3_cfunc, gap_4_cfunc]
funcs_t = [gap_1_cfunc(t), gap_2_cfunc(t), gap_3_cfunc(t), gap_4_cfunc(t)]

find_c_gen(N, gaps, gap_len, funcs)
find_parseval_gen(pN, gaps, funcs, funcs_t)

build_par_cf_t(funcs_t, gaps)
build_par_G_N__par_cf_t(N_1, funcs, funcs_t, gaps)
build_par_G_N__par_cf_t(N_2, funcs, funcs_t, gaps)
build_par_G_N__par_cf_t(N_3, funcs, funcs_t, gaps)
build_par_G_N__par_cf_t(N_4, funcs, funcs_t, gaps)
build_re_f_t(funcs_t, gaps)
build_im_f_t(funcs_t, gaps)
build_re_G_N(N_1, funcs, gaps)
build_re_G_N(N_2, funcs, gaps)
build_re_G_N(N_3, funcs, gaps)
build_re_G_N(N_4, funcs, gaps)
build_im_G_N(N_1, funcs, gaps)
build_im_G_N(N_2, funcs, gaps)
build_im_G_N(N_3, funcs, gaps)
build_im_G_N(N_4, funcs, gaps)
