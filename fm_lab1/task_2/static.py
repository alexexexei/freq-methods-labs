import sympy as sp

R = 2
T = 2 * sp.pi

N = 3
N_1 = 1
N_2 = 2
N_3 = 3
N_4 = 10

t = sp.Symbol('t')

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

def real_func(t):
    res = None
    if (point_1 <= t < point_2):
        res = point_1__point_2_Rfunc(t)
    elif (point_2 <= t < point_3):
        res = point_2__point_3_Rfunc(t)
    elif (point_3 <= t < point_4):
        res = point_3__point_4_Rfunc(t)
    elif (point_4 <= t < point_5):
        res = point_4__point_5_Rfunc(t)
    return res

def complex_func(t):
    res = None
    if (point_1 <= t < point_2):
        res = point_1__point_2_Imfunc(t)
    elif (point_2 <= t < point_3):
        res = point_2__point_3_Imfunc(t)
    elif (point_3 <= t < point_4):
        res = point_3__point_4_Imfunc(t)
    elif (point_4 <= t < point_5):
        res = point_4__point_5_Imfunc(t)
    return res

# can not compare expressions with a
# variable like "t" so bad code here
# Rfunc - real func, Imfunc - imaginary func
def point_1__point_2_Rfunc(t):
    return R

def point_2__point_3_Rfunc(t):
    return 2 * R * (1 - (4 * t) / T) 

def point_3__point_4_Rfunc(t):
    return -R

def point_4__point_5_Rfunc(t):
    return 2 * R * (-3 + (4 * t) / T)

def point_1__point_2_Imfunc(t):
    return (8 * R * t) / T

def point_2__point_3_Imfunc(t):
    return R

def point_3__point_4_Imfunc(t):
    return 4 * R * (1 - (2 * t) / T)

def point_4__point_5_Imfunc(t):
    return -R
