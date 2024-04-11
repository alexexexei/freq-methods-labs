from static import rectangular_function, shifted_rectangular_function, a_b_pars, consts, intervals, colors_strs
from help import get_fs, get_shfs, get_fimgs, get_parsevals, print_parsevals
from builder import build_f_t_rec, build_fimg2_rec, build_re_shfimg_rec, build_im_shfimg_rec, build_abs_shfimg_rec, build_re_im_shfimg_rec


a, b = a_b_pars[0][0], a_b_pars[0][1]
interval = intervals[1]

fs_color = colors_strs[0]
fimgs_color = colors_strs[1]
recol = colors_strs[2]
imcol = colors_strs[3]

fs = get_fs(rectangular_function, a_b_pars[:3])
fimgs = get_fimgs(fs, interval)

build_f_t_rec(fs, clr=fs_color)
build_fimg2_rec(fimgs, clr=fimgs_color)


shfs = get_shfs(shifted_rectangular_function, a, b, consts[:3])
shfimgs = get_fimgs(shfs, interval)

build_f_t_rec(shfs, clr=fs_color)
build_re_shfimg_rec(shfimgs, clr=fimgs_color)
build_im_shfimg_rec(shfimgs, clr=fimgs_color)
build_re_im_shfimg_rec(shfimgs, clr1=recol, clr2=imcol)
build_abs_shfimg_rec(shfimgs, clr=fimgs_color)


plpr = get_parsevals(fs, fimgs, interval)

print_parsevals(plpr)
