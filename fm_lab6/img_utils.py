from PIL import Image

import numpy as np
import scipy.signal as sps


def read_img(path: str):
    return Image.open(path)


def save_img(img: Image, path: str):
    img.save(path)


def convert_arr_to_img(arr):
    return Image.fromarray(arr)


def normalize(data):
    min_ = np.min(data)
    max_ = np.max(data)
    nz = (data - min_) / (max_ - min_)
    return nz, min_, max_


def denormalize(nz, min_, max_):
    return nz * (max_ - min_) + min_


def rgb_channels(img: Image):
    img_arr = np.array(img)
    r = img_arr[:, :, 0]
    g = img_arr[:, :, 1]
    b = img_arr[:, :, 2]
    return r, g, b


def rgb_angles(angles):
    ar = angles[:, :, 0]
    ag = angles[:, :, 1]
    ab = angles[:, :, 2]
    return ar, ag, ab


def fft2_channel(channel):
    channel = channel.astype(np.float64) / 255
    fft_ = np.fft.fftshift(np.fft.fft2(channel))
    abs_ = np.abs(fft_)
    angle = np.angle(fft_)
    log = np.log1p(abs_)
    nz, min_, max_ = normalize(log)
    return nz, min_, max_, angle


def ifft2_channel(channel, angle, min_, max_):
    channel = channel.astype(np.float64) / 255
    denor = denormalize(channel, min_, max_)
    abs_ = np.expm1(denor)
    col_res = abs_ * np.exp(1j * angle)
    ifft_ = np.fft.ifft2(np.fft.ifftshift(col_res))
    return np.real(ifft_)


def fft2(img: Image):
    r, g, b = rgb_channels(img)

    nzr, min_r, max_r, ar = fft2_channel(r)
    nzg, min_g, max_g, ag = fft2_channel(g)
    nzb, min_b, max_b, ab = fft2_channel(b)

    res = np.zeros((np.array(img).shape[0], np.array(img).shape[1], 3))
    res[:, :, 0] = nzr
    res[:, :, 1] = nzg
    res[:, :, 2] = nzb
    res = (res * 255).astype(np.uint8)

    ang = np.zeros((np.array(img).shape[0], np.array(img).shape[1], 3))
    ang[:, :, 0] = ar
    ang[:, :, 1] = ag
    ang[:, :, 2] = ab

    nz_min_max = [(min_r, max_r), (min_g, max_g), (min_b, max_b)]

    return res, ang, nz_min_max


def ifft2(img: Image, angles, nz_min_max):
    r, g, b = rgb_channels(img)
    ar, ag, ab = rgb_angles(angles)

    nz_r_min, nz_r_max = nz_min_max[0][0], nz_min_max[0][1]
    nz_g_min, nz_g_max = nz_min_max[1][0], nz_min_max[1][1]
    nz_b_min, nz_b_max = nz_min_max[2][0], nz_min_max[2][1]

    new_r = ifft2_channel(r, ar, nz_r_min, nz_r_max)
    new_g = ifft2_channel(g, ag, nz_g_min, nz_g_max)
    new_b = ifft2_channel(b, ab, nz_b_min, nz_b_max)

    res = np.zeros((np.array(img).shape[0], np.array(img).shape[1], 3))
    res[:, :, 0] = new_r
    res[:, :, 1] = new_g
    res[:, :, 2] = new_b
    res = normalize(res)[0] * 255
    
    return res.astype(np.uint8)


def raw_fft2(img: Image):
    r, g, b = rgb_channels(img)

    new_r = np.fft.fftshift(np.fft.fft2(r))
    new_g = np.fft.fftshift(np.fft.fft2(g))
    new_b = np.fft.fftshift(np.fft.fft2(b))

    res = np.zeros((np.array(img).shape[0], np.array(img).shape[1], 3))
    res[:, :, 0] = new_r.real
    res[:, :, 1] = new_g.real
    res[:, :, 2] = new_b.real

    return res


def raw_ifft2(arr):
    r, g, b = rgb_channels(arr)

    new_r = np.fft.ifft2(np.fft.ifftshift(r))
    new_g = np.fft.ifft2(np.fft.ifftshift(g))
    new_b = np.fft.ifft2(np.fft.ifftshift(b))

    res = np.zeros((arr.shape[0], arr.shape[1], 3))
    res[:, :, 0] = new_r.real
    res[:, :, 1] = new_g.real
    res[:, :, 2] = new_b.real

    return res


def fft2_2img(img: Image):
    res, ang, nz_min_max = fft2(img)
    return convert_arr_to_img(res), ang, nz_min_max


def ifft2_2img(img: Image, angles, nz_min_max):
    return convert_arr_to_img(ifft2(img, angles, nz_min_max))


def convolve2d(a, r, g, b, h, w, mode='same'):
    c2r = sps.convolve2d(r, a, mode)
    c2g = sps.convolve2d(g, a, mode)
    c2b = sps.convolve2d(b, a, mode)

    res = np.zeros((h, w, 3), dtype=np.uint8)
    res[:, :, 0] = np.clip(c2r, 0, 255)
    res[:, :, 1] = np.clip(c2g, 0, 255)
    res[:, :, 2] = np.clip(c2b, 0, 255)

    return res


def block_kernel(n: int):
    return np.ones((n, n)) / (n**2)


def gaussian_kernel(n: int):
    a = np.zeros((n, n), dtype=np.float32)
    sum_ = 0
    for x in range(n):
        for y in range(n):
            pow_ = -9 / (n**2) * ((x - (n + 1) / 2)**2+(y - (n + 1) / 2)**2)
            res = np.exp(pow_)
            a[x][y] = res
            sum_ += res
    a /= sum_
    return a


def block_blur_conv2(img: Image, n: int, mode='same'):
    a = block_kernel(n)
    r, g, b = rgb_channels(img)
    w, h = img.size
    return convolve2d(a, r, g, b, h, w, mode)


def gaussian_blur_conv2(img: Image, n: int, mode='same'):
    a = gaussian_kernel(n)
    r, g, b = rgb_channels(img)
    w, h = img.size
    return convolve2d(a, r, g, b, h, w, mode)


def block_blur_conv2_2img(img: Image, n: int, mode='same'):
    return convert_arr_to_img(block_blur_conv2(img, n, mode))


def gaussian_blur_conv2_2img(img: Image, n: int, mode='same'):
    return convert_arr_to_img(gaussian_blur_conv2(img, n, mode))


def apply_kernel(arr3, ker):
    r, g, b = rgb_channels(arr3)

    new_r = r * ker
    new_g = g * ker
    new_b = b * ker

    res = np.zeros((np.array(arr3).shape[0], np.array(arr3).shape[1], 3))
    res[:, :, 0] = new_r.real
    res[:, :, 1] = new_g.real
    res[:, :, 2] = new_b.real

    return res


def fft2_blur(img: Image, kernel, n):
    a = kernel(n)
    w, h = img.size
    k, l = a.shape

    fft2_img = raw_fft2(img)
    fft2_ker = np.fft.fftshift(np.fft.fft2(a, s=(h, w)))
    img_ker = apply_kernel(fft2_img, fft2_ker)

    res = np.real(raw_ifft2(img_ker)) / 255

    return res.astype(np.uint8)


def block_blur_fft2(img: Image, n: int):
    return fft2_blur(img, block_kernel, n)


def gaussian_blur_fft2(img: Image, n: int):
    return fft2_blur(img, gaussian_kernel, n)


def block_blur_fft2_2img(img: Image, n: int):
    return convert_arr_to_img(block_blur_fft2(img, n))


def gaussian_blur_fft2_2img(img: Image, n: int):
    return convert_arr_to_img(gaussian_blur_fft2(img, n))
