import help as hp


a = 2
t_1 = -1.5
t_2 = 2.5

T = 10
dt = 0.01

V = 1/dt
dv = 1/T

time = hp.get_t(T, dt)
freq = hp.get_v(V, dv)
g_fs = hp.get_g_fs(time, t_1, t_2, a)