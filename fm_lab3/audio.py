import numpy as np
import librosa
from scipy.io.wavfile import write
from playsound import playsound

import filters as ft
import builder as bd


title = 'High frequency filter audio'
title2 = 'Abs high frequency filter audio'

src = 'fm_lab3/sound/MUHA.wav'
filename = 'fm_lab3/sound/filtered_MUHA.wav'
audio, rate = librosa.load(src, sr=None)

dt = 1 / rate
T = len(audio) * dt

time = np.linspace(0, T, len(audio), endpoint=False)
freq = np.linspace(-rate / 2, rate / 2, len(audio), endpoint=False)

flt_u, flt_U = ft.filter_high(freq, audio, 300)
flt_u, flt_U = ft.filter_special_out(freq, flt_u, [[freq[0], -4500], [4500, freq[-1]]])
flt_u_float = flt_u.real.astype(np.float32)

bd.build_u_or_U(time,
                audio.real,
                xlab='Time',
                title='Noisy audio signal',
                fz1=12,
                fz2=6,
                legend=False)
bd.build_u_to_U(freq,
                audio,
                title='fft noisy audio signal',
                legend=False,
                fz1=12,
                fz2=6,
                xl1=0,
                xl2=500)
bd.build_u_to_U(freq,
                audio,
                title='fft noisy audio signal',
                legend=False,
                fz1=12,
                fz2=6,
                xl1=3000,
                yl1=0.25,
                yl2=5)

bd.build_u__flt_u(time, audio.real, flt_u, title=title, fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq,
                           audio,
                           flt_U,
                           title=title2,
                           fz1=12,
                           fz2=6,
                           xl1=0,
                           xl2=500,
                           yl2=2000)
bd.build_abs_u_to_U__flt_U(freq,
                           audio,
                           flt_U,
                           title=title2,
                           fz1=12,
                           fz2=6,
                           xl1=3000,
                           yl1=-0.25,
                           yl2=5)

write(filename, rate, flt_u_float)
playsound(filename)
