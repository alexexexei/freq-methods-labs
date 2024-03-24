from static import gaussian_function, a_b_pars, intervals, colors_strs
from help import get_fs, get_fimgs, get_parsevals, print_parsevals
from builder import build_f_t_rec, build_fimg2_rec


interval = intervals[1]
fs_color = colors_strs[0]
fimgs_color = colors_strs[1]

fs = get_fs(gaussian_function, a_b_pars)
fimgs = get_fimgs(fs, interval)
plpr = get_parsevals(fs, fimgs, interval)

print_parsevals(plpr)
build_f_t_rec(fs, fs_color, [None] * len(fs))
build_fimg2_rec(fimgs, fimgs_color, [None] * len(fimgs))