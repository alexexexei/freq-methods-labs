import numpy as np
import librosa
from scipy.io.wavfile import write
from playsound import playsound

import filters as ft
import builder as bd


filter_all = True
build_U = False

title = 'Low frequency filter audio'
title2 = 'Abs low frequency filter audio'
if filter_all:
    title = 'Low and special frequency filter audio'
    title2 = 'Abs low and special frequency filter audio'

src = 'sound/MUHA.wav'
filename = 'sound/filtered_MUHA_2.wav'
try:
    audio, rate = librosa.load(src, sr=None)
except:
    lab = 'fm_lab3/'
    src = lab + src
    filename = lab + filename
    audio, rate = librosa.load(src, sr=None)

dt = 1 / rate
T = len(audio) * dt

time = np.linspace(0, T, len(audio), endpoint=False)
freq = np.linspace(-rate / 2, rate / 2, len(audio), endpoint=False)

flt_u, flt_U = ft.filter_low(freq, audio, 300)
if filter_all:
    flt_u, flt_U = ft.filter_special(freq, flt_u, [[freq[0], -1000], [1000, freq[-1]]])
flt_u_float = flt_u.real.astype(np.float32)


if build_U:
    bd.build_u_or_U(time, audio, xlab='Time',
                    title='Noisy audio signal', fz1=12, fz2=6,
                    legend=False)
    bd.build_u_to_U(freq, audio, title='fft noisy audio signal',
                    legend=False, fz1=12, fz2=6,
                    xl1=-875, xl2=875, yl1=-4000,
                    yl2=4000)

bd.build_u__flt_u(time, audio, flt_u,
                  title=title, fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, audio, flt_U,
                           title=title2, xl1=-1500, xl2=1500,
                           yl1=0, yl2=2000, fz1=12, fz2=6)

write(filename, rate, flt_u_float)
playsound(filename)
