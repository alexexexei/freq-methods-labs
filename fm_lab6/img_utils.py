from PIL import Image

import numpy as np
import scipy.signal as sps


def read_img(path: str):
    return Image.open(path)


def save_img(img: Image, path: str):
    img.save(path)


def convert_arr_to_img(arr):
    return Image.fromarray(arr)


def img2gray(img: Image):
    return img.convert('L')


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


def raw_fft2(img: Image):
    r, g, b = rgb_channels(img)

    new_r = np.fft.fftshift(np.fft.fft2(r))
    new_g = np.fft.fftshift(np.fft.fft2(g))
    new_b = np.fft.fftshift(np.fft.fft2(b))

    return np.stack((new_r, new_g, new_b), axis=2)


def raw_ifft2(arr):
    r, g, b = rgb_channels(arr)

    new_r = np.fft.ifft2(np.fft.ifftshift(r))
    new_g = np.fft.ifft2(np.fft.ifftshift(g))
    new_b = np.fft.ifft2(np.fft.ifftshift(b))

    return np.stack((np.clip(new_r.real, 0, 255), np.clip(
        new_g.real, 0, 255), np.clip(new_b.real, 0, 255)),
                    axis=2).astype(np.uint8)


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

    res = np.stack((nzr, nzg, nzb), axis=2)
    res = (res * 255).astype(np.uint8)

    ang = np.stack((ar, ag, ab), axis=2)

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

    res = np.stack((new_r, new_g, new_b), axis=2)
    res = normalize(res)[0] * 255

    return res.astype(np.uint8)


def convolve2d(img: Image, a, mode='same'):
    r, g, b = rgb_channels(img)
    c2r = sps.convolve2d(r, a, mode)
    c2g = sps.convolve2d(g, a, mode)
    c2b = sps.convolve2d(b, a, mode)
    return (np.stack(
        (np.clip(c2r, 0, 255), np.clip(c2g, 0, 255), np.clip(c2b, 0, 255)),
        axis=2)).astype(np.uint8)


def block_kernel(n: int):
    return np.ones((n, n)) / (n**2)


def gaussian_kernel(n: int):
    a = np.zeros((n, n), dtype=np.float32)
    sum_ = 0
    for x in range(n):
        for y in range(n):
            pow_ = -9 / (n**2) * ((x - (n + 1) / 2)**2 + (y - (n + 1) / 2)**2)
            res = np.exp(pow_)
            a[x][y] = res
            sum_ += res
    a /= sum_
    return a


def block_blur_conv2(img: Image, n: int, mode='same'):
    a = block_kernel(n)
    return convolve2d(img, a, mode)


def gaussian_blur_conv2(img: Image, n: int, mode='same'):
    a = gaussian_kernel(n)
    return convolve2d(img, a, mode)


def apply_kernel(arr3, ker):
    r, g, b = rgb_channels(arr3)

    new_r = r * ker
    new_g = g * ker
    new_b = b * ker

    return np.stack((new_r, new_g, new_b), axis=2)


def fft2_blur(img: Image, kernel, n):
    a = kernel(n)
    w, h = img.size

    fft2_img = raw_fft2(img)
    fft2_ker = np.fft.fftshift(np.fft.fft2(a, s=(h, w)))
    img_ker = apply_kernel(fft2_img, fft2_ker)

    return raw_ifft2(img_ker)


def block_blur_fft2(img: Image, n: int):
    return fft2_blur(img, block_kernel, n)


def gaussian_blur_fft2(img: Image, n: int):
    return fft2_blur(img, gaussian_kernel, n)


def sharpen_conv2(img: Image, n: int = 1, K=None):
    if n <= 0:
        return img

    if K is None:
        K = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

    ans = convolve2d(img, K)
    for i in range(n - 1):
        ans = convolve2d(ans, K)

    return ans


def sharpen_fft2(img: Image, n: int = 1, K=None):
    if n <= 0:
        return img

    if K is None:
        K = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]

    w, h = img.size
    fft2_img = raw_fft2(img)
    fft2_ker = np.fft.fftshift(np.fft.fft2(K, s=(h, w)))
    img_ker = apply_kernel(fft2_img, fft2_ker)
    for i in range(n - 1):
        img_ker = apply_kernel(img_ker, fft2_ker)

    return raw_ifft2(img_ker)


def edgen_conv2(img: Image, K = None):
    img2gray_ = img2gray(img)

    if K is None:
        K = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    c2d = sps.convolve2d(img2gray_, K, mode='same')
    nc2d = (normalize(c2d)[0] * 255).astype(np.uint8)

    return nc2d


def edgen_fft2(img: Image, K = None):
    img2gray_ = img2gray(img)

    if K is None:
        K = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    w, h = img.size
    fft2_img = np.fft.fftshift(np.fft.fft2(img2gray_))
    fft2_ker = np.fft.fftshift(np.fft.fft2(K, s=(h, w)))
    img_ker = fft2_img * fft2_ker
    res = np.fft.ifft2(np.fft.ifftshift(img_ker)).real
    res = (normalize(res)[0] * 255).astype(np.uint8)

    return res


def fft2_2img(img: Image):
    res, ang, nz_min_max = fft2(img)
    return convert_arr_to_img(res), ang, nz_min_max


def ifft2_2img(img: Image, angles, nz_min_max):
    return convert_arr_to_img(ifft2(img, angles, nz_min_max))


def block_blur_conv2_2img(img: Image, n: int, mode='same'):
    return convert_arr_to_img(block_blur_conv2(img, n, mode))


def gaussian_blur_conv2_2img(img: Image, n: int, mode='same'):
    return convert_arr_to_img(gaussian_blur_conv2(img, n, mode))


def block_blur_fft2_2img(img: Image, n: int):
    return convert_arr_to_img(block_blur_fft2(img, n))


def gaussian_blur_fft2_2img(img: Image, n: int):
    return convert_arr_to_img(gaussian_blur_fft2(img, n))


def sharpen_conv2_2img(img: Image, n: int = 1, K=None):
    return convert_arr_to_img(sharpen_conv2(img, n, K))


def sharpen_fft2_2img(img: Image, n: int = 1, K=None):
    return convert_arr_to_img(sharpen_fft2(img, n, K))


def edgen_conv2_2img(img: Image, K = None):
    return convert_arr_to_img(edgen_conv2(img, K))


def edgen_fft2_2img(img: Image, K = None):
    return convert_arr_to_img(edgen_fft2(img, K))
