from static import colors_strs
from help import get_y_sr_t
from builder import build_audio_f_t, build_audio_f_v
from finder import find_freqs_ampls


audio_file = 'fm_lab2/chord/chord26.mp3'
select_channel = 0
y, sr, t = get_y_sr_t(audio_file, select_channel)

y = y[:3 * sr]
t = t[:3 * sr]

freqs, ampls = find_freqs_ampls(t, y, sr)

r_start = 200
r_end = 500

start_idx = next(idx for idx, freq in enumerate(freqs) if freq >= r_start)
end_idx = next(idx for idx, freq in enumerate(freqs) if freq > r_end)

r_ampls = ampls[start_idx:end_idx]
r_freqs = freqs[start_idx:end_idx]

start = 0
stop = 10001
step = 1000
r_step = 20

figsize1 = 10
figsize2 = 6
f_t_clr = colors_strs[0]
f_v_clr = colors_strs[1]

build_audio_f_t(t, y, f_t_clr)
build_audio_f_v(freqs,
                ampls,
                start=start,
                stop=stop,
                step=step,
                fz1=figsize1,
                fz2=figsize2,
                clr=f_v_clr)
build_audio_f_v(r_freqs,
                r_ampls,
                start=r_start,
                stop=r_end,
                step=r_step,
                fz1=figsize1,
                fz2=figsize2,
                clr=f_v_clr)
