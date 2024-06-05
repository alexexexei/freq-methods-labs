import img_utils as iu


src = 'fm_lab6/src'
img_path = f'{src}/4.png'

render_to = 'fm_lab6/renders/task1'
rimg_path = f'{render_to}/fft2.png'
reimg_path = f'{render_to}/new4.png'

corr_im_path = f'{src}/corr_fft2.png'
corrected = True

img = iu.read_img(img_path)
res, ang, nzmm = iu.fft2(img)
ans = iu.convert_arr_to_img(res)
iu.save_img(ans, rimg_path)

if corrected:
    img2 = iu.read_img(corr_im_path)
    ans_ = iu.ifft2(img2, ang, nzmm)
    ans_ = iu.convert_arr_to_img(ans_)
    iu.save_img(ans_, reimg_path)