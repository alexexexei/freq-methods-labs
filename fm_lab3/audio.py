import numpy as np
import librosa
from scipy.io.wavfile import write
from playsound import playsound

import filters as ft
import builder as bd


filter_all = True
build_U = True

title = 'High frequency filter audio'
title2 = 'Abs high frequency filter audio'
if filter_all:
    title = 'High and special frequency filter audio'
    title2 = 'Abs high and special frequency filter audio'

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

flt_u, flt_U = ft.filter_high(freq, audio, 300)
if filter_all:
    flt_u, flt_U = ft.filter_special_out(freq, flt_u, [[freq[0], -4500], [4500, freq[-1]]])
flt_u_float = flt_u.real.astype(np.float32)


if build_U:
    bd.build_u_or_U(time, audio, xlab='Time',
                    title='Noisy audio signal', fz1=12, fz2=6,
                    legend=False)
    bd.build_u_to_U(freq, audio, title='fft noisy audio signal',
                    legend=False, fz1=12, fz2=6,
                    xl1=0, yl1=0, yl2=20)

bd.build_u__flt_u(time, audio, flt_u,
                  title=title, fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, audio, flt_U,
                           title=title2, fz1=12, fz2=6,
                           xl1=0, yl1=0, yl2=20)

write(filename, rate, flt_u_float)
playsound(filename)
