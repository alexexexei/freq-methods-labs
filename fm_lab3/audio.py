import numpy as np
import librosa
from scipy.io.wavfile import write

import filters as ft
import builder as bd


audio, rate = librosa.load('fm_lab3/sound/MUHA.wav', sr=None)

dt = 1 / rate
T = len(audio) * dt

time = np.linspace(0, T, len(audio), endpoint=False)
freq = np.linspace(-rate / 2, rate / 2, len(audio), endpoint=False)

flt_u, flt_U = ft.filter_special(freq, audio, [[-306, 301]])
flt_u_float = flt_u.real.astype(np.float32)


bd.build_u_or_U(time, audio, xlab='Time', label='Noisy signal', fz1=10, fz2=6)
bd.build_u_to_U(freq, audio, label='fft noisy signal', fz1=10, fz2=6, xl1=-1000, xl2=1000)

bd.build_u__flt_u(time, audio, flt_u, title='Low frequencies filter')
bd.build_abs_u_to_U__flt_U(freq, audio, flt_U, title='Abs low frequencies filter', xl1=-1600, xl2=1600)

write('fm_lab3/sound/filtered_MUHA.wav', rate, flt_u_float)
