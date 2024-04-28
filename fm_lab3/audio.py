import numpy as np
import librosa
from scipy.io.wavfile import write

import filters as ft
import builder as bd

audio, rate = librosa.load('sound/MUHA.wav', sr=None)

dt = 1 / rate
T = len(audio) * dt
times = np.linspace(0, T, len(audio), endpoint=False)
freqs = np.linspace(-rate / 2, rate / 2, len(audio), endpoint=False)

flt_u, flt_U = ft.filter_low(freqs, audio, 300)

bd.build_u__flt_u(times, audio, flt_u, title='Low frequencies filter')
bd.build_abs_u_to_U__flt_U(times, audio, flt_U, title='Abs low frequencies filter')

flt_u_float = flt_u.real.astype(np.float32)

write('sound/filtered_MUHA.wav', rate, flt_u_float)
