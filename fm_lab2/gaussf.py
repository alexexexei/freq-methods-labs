from static import gaussian_function, a_b_pars, intervals, colors_strs
from help import get_fs, get_fimgs, get_parsevals, print_parsevals
from builder import build_f_t_rec, build_fimg2_rec


interval = intervals[1]
fs_color = colors_strs[0]
fimgs_color = colors_strs[1]

fs = get_fs(gaussian_function, a_b_pars[:3])
fimgs = get_fimgs(fs, interval)

build_f_t_rec(fs, clr=fs_color)
build_fimg2_rec(fimgs, clr=fimgs_color)

fseq = get_fs(gaussian_function, a_b_pars[3:])
fimgseq = get_fimgs(fseq, interval)

build_f_t_rec(fseq, clr=fs_color)
build_fimg2_rec(fimgseq, clr=fimgs_color)

plpr = get_parsevals(fs, fimgs, interval)

print_parsevals(plpr)
