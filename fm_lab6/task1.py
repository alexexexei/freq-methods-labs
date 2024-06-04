import cv2 as cv
import numpy as np


image = cv.imread("fm_lab6/src/4.png")

image = image.astype(np.float64) / 255.0

fft_ = np.fft.fftshift(np.fft.fft2(image))

fft_abs = np.abs(fft_)
fft_angle = np.angle(fft_)

fft_log = np.log1p(fft_abs)
fft_norm = cv.normalize(fft_log, None, 0, 1, cv.NORM_MINMAX)

magnitude_image = (fft_norm * 255).astype(np.uint8)

cv.imwrite("fm_lab6/renders/ans.png", magnitude_image)