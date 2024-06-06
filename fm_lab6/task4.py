import img_utils as iu


src = 'fm_lab6/src'
img_path = f'{src}/pa.png'
render_to = 'fm_lab6/renders/task4'

img = iu.read_img(img_path)
gray = iu.img2gray(img)
iu.save_img(gray, f'{render_to}/img2gray.png')

ans = iu.edgen_conv2_2img(img)
iu.save_img(ans, f'{render_to}/edgen_conv2.png')

ans2 = iu.edgen_fft2_2img(img)
iu.save_img(ans2, f'{render_to}/edgen_fft2.png')
