import sympy as sp

t = sp.Symbol('t')
omega = sp.Symbol('omega')

intervals = [(-10000000, 10000000), (-sp.oo, sp.oo)]
a_b_pars = [(1, 2), (2, 3), (3, 4)]

def rectangular_function(a, b):
    return sp.Piecewise((a, sp.Abs(t) <= b), (0, sp.Abs(t) > b))

def triangular_function(a, b):
    return sp.Piecewise((a - sp.Abs(a * t / b), sp.Abs(t) <= b), (0, sp.Abs(t) > b))

def cardinal_sinus(a, b):
    return a * sp.sinc(b * t)

def gaussian_function(a, b):
    return a * sp.E ** (-b * t ** 2)

def double_attenuation(a, b):
    return a * sp.E ** (-b * sp.Abs(t))
