from sympy import Symbol, cos, sin, pi

a = 1
b = 2

pN = 25
N = 3
N_1 = 10
N_2 = 20
N_3 = 30
N_4 = 40
N_5 = 50

t = Symbol('t')

gap_start = 0.5 * pi
gap_start_val = float(gap_start.evalf())

gap_mid = 1.5 * pi
gap_mid_val = float(gap_mid.evalf())

gap_end = 2 * pi
gap_end_val = float(gap_end.evalf())

gap_len = gap_end - gap_start
gap_len_val = float(gap_len.evalf())

gap_1 = [gap_start, gap_mid]
gap_2 = [gap_mid, gap_end]
gaps = [gap_1, gap_2]

# can not check if "t" is in [gap_start, gap_mid)
# and etc. because "t" is a symbol so bad code here
def square_wave_a(t):
    return a

def square_wave_b(t):
    return b

def even_periodic_func(t):
    return cos(t)

def odd_periodic_func(t):
    return sin(t)

def not_even_or_odd_periodic_func(t):
    return cos(t) + t

def test_func(t):
    return t
