import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage.io as io


def z_scan_mask(C, N):
    mask = np.zeros((N, N))
    start = 0
    mask_m = start
    mask_n = start
    for i in range(C):
        if i == 0:
            mask[mask_m, mask_n] = 1
        else:
            if (mask_m + mask_n) % 2 == 0:
                mask_m -= 1
                mask_n += 1
                if mask_m < 0:
                    mask_m += 1
                if mask_n >= N:
                    mask_n -= 1
            else:
                mask_m += 1
                mask_n -= 1
                if mask_m >= N:
                    mask_m -= 1
                if mask_n < 0:
                    mask_n += 1
            mask[mask_m, mask_n] = 1
    return mask


def compress_channel(channel, mask, N):
    img_dct = np.zeros((channel.shape[0] // N * N, channel.shape[1] // N * N), dtype=np.float32)
    for m in range(0, img_dct.shape[0], N):
        for n in range(0, img_dct.shape[1], N):
            block = channel[m:m + N, n:n + N].astype(np.float32)
            coeff = cv2.dct(block)
            iblock = cv2.idct(coeff * mask)
            img_dct[m:m + N, n:n + N] = iblock
    return img_dct


def compress_image(img, mask, N):
    channels = cv2.split(img)
    compressed_channels = [compress_channel(ch, mask, N) for ch in channels]
    compressed_img = cv2.merge(compressed_channels)
    return compressed_img


def display_image(img_ycbcr):
    img_rgb = cv2.cvtColor(np.uint8(img_ycbcr), cv2.COLOR_YCrCb2RGB)
    return img_rgb


img = io.imread("project/src/cat.jpg")
img_ycbcr = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

N = 8
c1 = 1
c2 = 3
c3 = 10
compr_img1 = compress_image(img_ycbcr, z_scan_mask(c1, N), N)
compr_img2 = compress_image(img_ycbcr, z_scan_mask(c2, N), N)
compr_img3 = compress_image(img_ycbcr, z_scan_mask(c3, N), N)

plt.figure(figsize=(16, 4))
plt.axis('off')

plt.subplot(141)
plt.title('Original image')
plt.imshow(display_image(img_ycbcr))
plt.axis('off')

plt.subplot(142)
plt.title(f'Keep {c1} coefficient')
plt.imshow(display_image(compr_img1))
plt.axis('off')

plt.subplot(143)
plt.title(f'Keep {c2} coefficients')
plt.imshow(display_image(compr_img2))
plt.axis('off')

plt.subplot(144)
plt.title(f'Keep {c3} coefficients')
plt.imshow(display_image(compr_img3))
plt.axis('off')

plt.show()
