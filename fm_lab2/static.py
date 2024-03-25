from sympy import Symbol, Piecewise, Abs, sinc, E, oo


t = Symbol('t')
omega = Symbol('omega')

sym_dis = 10000000
intervals = [(-sym_dis, sym_dis), (-oo, oo)]

a_b_pars = [(1, 2), (2, 3), (3, 4)]
colors_strs = ['red', 'purple', 'blue'] 


def rectangular_function(a, b):
    return Piecewise((a, Abs(t) <= b), (0, Abs(t) > b))


def triangular_function(a, b):
    return Piecewise((a - Abs(a * t / b), Abs(t) <= b), (0, Abs(t) > b))


def cardinal_sinus(a, b):
    return a * sinc(b * t)


def gaussian_function(a, b):
    return a * E ** (-b * t ** 2)


def double_attenuation(a, b):
    return a * E ** (-b * Abs(t))

def shifted_rectangular_function(a, b, shift):
    if (shift == 0):
        return rectangular_function(a, b)
    return Piecewise((a, Abs(t + shift) <= b), (0, Abs(t + shift) > b))
