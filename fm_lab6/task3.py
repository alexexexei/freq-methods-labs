import img_utils as iu


src = 'fm_lab6/src'
img_path = f'{src}/4.png'
render_to = 'fm_lab6/renders/task3'

img = iu.read_img(img_path)
n = [1]
for i in n:
    ans = iu.sharpen_conv2_2img(img, i)
    iu.save_img(ans, f'{render_to}/sharp_conv2_n={i}.png')
    
    ans2 = iu.sharpen_fft2_2img(img, i)
    iu.save_img(ans2, f'{render_to}/sharp_fft2_n={i}.png')
