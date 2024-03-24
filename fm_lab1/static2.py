from sympy import Symbol, pi


R = 2
T = 2 * pi

pN = 25
N = 3
N_1 = 1
N_2 = 2
N_3 = 3
N_4 = 10

t = Symbol('t')

point_common = T / 8

point_1 = -point_common
point_1_val = float(point_1.evalf())

point_2 = point_common
point_2_val = float(point_2.evalf())

point_3 = 3 * point_common
point_3_val = float(point_3.evalf())

point_4 = 5 * point_common
point_4_val = float(point_4.evalf())

point_5 = 7 * point_common
point_5_val = float(point_5.evalf())

gap_1 = [point_1, point_2]
gap_2 = [point_2, point_3]
gap_3 = [point_3, point_4]
gap_4 = [point_4, point_5]
gaps = [gap_1, gap_2, gap_3, gap_4]

gap_len = gap_4[1] - gap_1[0]
gap_len_val = float(gap_len.evalf())


def gap_1_cfunc(t):
    return R + (8 * R * t / T) * 1j


def gap_2_cfunc(t):
    return 2 * R - (8 * R * t / T) + R * 1j


def gap_3_cfunc(t):
    return -R + (4 * R - (8 * R * t / T)) * 1j


def gap_4_cfunc(t):
    return -6 * R + (8 * R * t / T) - R * 1j
