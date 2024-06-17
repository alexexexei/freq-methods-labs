import help as hp


a = 2
t_1, t_2 = -1.5, 2.5

T, dt = 10, 0.01
V, dv = 1 / dt, 1 / T

time = hp.get_t(T, dt)
freq = hp.get_v(V, dv)
g_fs = hp.get_g_fs(time, t_1, t_2, a)