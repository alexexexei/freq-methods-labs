from static import rectangular_function, shifted_rectangular_function, a_b_pars, consts, intervals, colors_strs
from help import get_fs, get_shfs, get_fimgs, get_parsevals, print_parsevals
from builder import build_f_t_rec, build_fimg2_rec, build_re_shfimg_rec, build_im_shfimg_rec, build_abs_shfimg_rec, build_re_im_shfimg_rec


a, b = a_b_pars[0][0], a_b_pars[0][1]
interval = intervals[1]

fs_color = colors_strs[0]
fimgs_color = colors_strs[1]
jclr1 = colors_strs[2]
jclr2 = colors_strs[3]

fs = get_fs(rectangular_function, a_b_pars[:3])
fimgs = get_fimgs(fs, interval)
plpr = get_parsevals(fs, fimgs, interval)

shfs = get_shfs(shifted_rectangular_function, a, b, consts[:3])
shfimgs = get_fimgs(shfs, interval)

print_parsevals(plpr)
build_f_t_rec(fs, fs_color, [None] * len(fs))
build_fimg2_rec(fimgs, fimgs_color, [None] * len(fimgs))

build_f_t_rec(shfs, fs_color, [None] * len(shfs))
build_re_shfimg_rec(shfimgs, fimgs_color, [None] * len(shfimgs))
build_im_shfimg_rec(shfimgs, fimgs_color, [None] * len(shfimgs))
build_re_im_shfimg_rec(shfimgs, jclr1, jclr2, [None] * len(shfimgs))
build_abs_shfimg_rec(shfimgs, fimgs_color, [None] * len(shfimgs))
