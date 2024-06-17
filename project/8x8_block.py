'@author Dmitrii Chebanenko'


from PIL import Image
import numpy as np
from scipy.fftpack import dct, idct


matrix_8x8_rgb = [
    [[255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [255, 0, 255], [192, 192, 192],
     [128, 128, 128]],
    [[128, 0, 0], [128, 128, 0], [0, 128, 0], [0, 128, 128], [0, 0, 128], [128, 0, 128], [64, 64, 64], [255, 255, 255]],
    [[255, 0, 0], [255, 128, 0], [255, 255, 0], [128, 255, 0], [0, 255, 0], [0, 255, 128], [0, 255, 255],
     [0, 128, 255]],
    [[0, 0, 255], [128, 0, 255], [255, 0, 255], [255, 0, 128], [128, 0, 128], [255, 255, 255], [0, 0, 0], [64, 0, 0]],
    [[64, 128, 128], [128, 128, 64], [64, 64, 128], [128, 64, 128], [64, 128, 64], [128, 64, 64], [64, 64, 64],
     [192, 192, 192]],
    [[192, 0, 0], [192, 192, 0], [0, 192, 0], [0, 192, 192], [0, 0, 192], [192, 0, 192], [96, 96, 96], [255, 128, 128]],
    [[128, 255, 255], [255, 128, 255], [255, 255, 128], [128, 128, 255], [255, 128, 128], [128, 255, 128],
     [255, 255, 255], [64, 128, 255]],
    [[0, 0, 64], [64, 64, 0], [0, 64, 64], [64, 0, 64], [0, 64, 0], [0, 64, 128], [64, 0, 128], [128, 128, 128]]
]

quantization_y = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

quantization_color = np.array([
    [17, 28, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 99, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99]
])

image_rgb = Image.fromarray(np.array(matrix_8x8_rgb, dtype=np.uint8))

new_size = (400, 400)
# image_rgb_resized = image_rgb.resize(new_size, Image.NEAREST)
# image_rgb_resized.save("rgb_image.png")

image_ycrcb = image_rgb.convert("YCbCr")
y, cb, cr = image_ycrcb.split()

y_arr = np.array(y).astype(int)
cb_arr = np.array(cb).astype(int)
cr_arr = np.array(cr).astype(int)

y_minus_128 = y_arr - 128
cb_minus_128 = cb_arr - 128
cr_minus_128 = cr_arr - 128

y_dct = dct(dct(y_minus_128.T, type=2, norm='ortho').T, type=2, norm='ortho')
np.set_printoptions(precision=2, suppress=True)
cb_dct = dct(dct(cb_minus_128.T, type=2, norm='ortho').T, type=2, norm='ortho')
cr_dct = dct(dct(cr_minus_128.T, type=2, norm='ortho').T, type=2, norm='ortho')

q_y = np.round(y_dct / quantization_y).astype(int)
q_cb = np.round(cb_dct / quantization_color).astype(int)
q_cr = np.round(cr_dct / quantization_color).astype(int)

print(q_y)

r_y = np.array([[-8, -4, 3, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])

r_cb = np.array([[1, -4, 0, 0, 0, 0, 0, 0],
                 [-3, -4, 0, 0, 0, 0, 0, 0],
                 [-1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]])

r_cr = np.array([[0, 3, 4, 2, 0, 0, 0, 0],
                 [0, 3, 0, 0, 0, 0, 0, 0],
                 [-2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]])

ans_y = r_y * quantization_y
ans_cb = r_cb * quantization_color
ans_cr = r_cr * quantization_color

inverse_dct_y = (idct(idct(ans_y, type=2, norm='ortho').T, type=2, norm='ortho').T + 128).astype(np.uint8)
inverse_dct_cb = (idct(idct(ans_cb, type=2, norm='ortho').T, type=2, norm='ortho').T + 128).astype(np.uint8)
inverse_dct_cr = (idct(idct(ans_cr, type=2, norm='ortho').T, type=2, norm='ortho').T + 128).astype(np.uint8)

image_arr = np.stack((inverse_dct_y, inverse_dct_cb, inverse_dct_cr), axis=2)
image = Image.fromarray(image_arr, 'YCbCr').convert('RGB')
image_resized = image.resize(new_size, Image.NEAREST)
image_resized.save("project/renders/compress_jpeg/8x8_block_k=5.png")
