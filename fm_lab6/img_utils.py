from PIL import Image
import numpy as np


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
