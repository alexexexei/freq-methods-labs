import img_utils as iu


src = 'fm_lab6/src'
img_path = f'{src}/4.png'
render_to = 'fm_lab6/renders/task2'
r1 = f'{render_to}/block_blur'
r2 = f'{render_to}/gaussian_blur'

img = iu.read_img(img_path)
n = [9, 13, 21]
for i in n:
    conv2_i = iu.block_blur_conv2_2img(img, i)
    rimg_path1 = f'{r1}/bl_c2_n={i}.png'
    iu.save_img(conv2_i, rimg_path1)

    conv2_i2 = iu.gaussian_blur_conv2_2img(img, i)
    rimg_path3 = f'{r2}/g_c2_n={i}.png'
    iu.save_img(conv2_i2, rimg_path3)

    fft2_i = iu.block_blur_fft2_2img(img, i)
    rimg_path2 = f'{r1}/bl_fft2_n={i}.png'
    iu.save_img(fft2_i, rimg_path2)

    fft2_i2 = iu.gaussian_blur_fft2_2img(img, i)
    rimg_path4 = f'{r2}/g_fft2_n={i}.png'
    iu.save_img(fft2_i2, rimg_path4)
