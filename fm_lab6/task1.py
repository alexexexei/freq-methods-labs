import img_utils as iu


src = 'fm_lab6/src'
curr_img = '2'
img_path = f'{src}/{curr_img}.png'

render_to = 'fm_lab6/renders/task1'
rimg_path = f'{render_to}/fft2_{curr_img}.png'
reimg_path = f'{render_to}/new_{curr_img}.png'

corr_im_path = f'{src}/corr_fft2_{curr_img}.png'
corrected = True

img = iu.read_img(img_path)
ans, ang, nzmm = iu.fft2_2img(img)
iu.save_img(ans, rimg_path)

if corrected:
    img2 = iu.read_img(corr_im_path)
    ans2 = iu.ifft2_2img(img2, ang, nzmm)
    iu.save_img(ans2, reimg_path)
