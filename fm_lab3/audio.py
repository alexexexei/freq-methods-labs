import numpy as np
import librosa
from scipy.io.wavfile import write
from playsound import playsound

import filters as ft
import builder as bd


src = 'sound/MUHA.wav'
audio, rate = librosa.load(src, sr=None)

dt = 1 / rate
T = len(audio) * dt

time = np.linspace(0, T, len(audio), endpoint=False)
freq = np.linspace(-rate / 2, rate / 2, len(audio), endpoint=False)

flt_u, flt_U = ft.filter_low(freq, audio, 300)
flt_u_float = flt_u.real.astype(np.float32)


bd.build_u_or_U(time, audio, xlab='Time',
                title='Noisy audio signal', fz1=12, fz2=6,
                legend=False)
bd.build_u_to_U(freq, audio, title='fft noisy audio signal',
                legend=False, fz1=12, fz2=6,
                xl1=-875, xl2=875, yl1=-4000,
                yl2=4000)

bd.build_u__flt_u(time, audio, flt_u,
                  title='Low frequency filter audio', fz1=12, fz2=6)
bd.build_abs_u_to_U__flt_U(freq, audio, flt_U,
                           title='Abs low frequency filter audio', xl1=-750, xl2=750,
                           yl1=0, yl2=2000, fz1=12, fz2=6)

filename = 'sound/filtered_MUHA.wav'
write(filename, rate, flt_u_float)
playsound(filename)
