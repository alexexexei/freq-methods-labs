import sympy as sp
from static import t

def calc_not_complex_coeff(gap_length):
    return 2 / gap_length

def calc_complex_coeff(gap_length):
    return 1 / gap_length

def calc_omega_n(n, gap_length):
    return (2 * sp.pi * n) / gap_length

def calc_a_n(n, start, end, gap_length, f):
    coeff = calc_not_complex_coeff(gap_length)
    integrand = coeff * f(t)
    if n != 0:
        omega_n = calc_omega_n(n, gap_length)
        integrand = integrand * sp.cos(omega_n * t)
    
    result = sp.integrate(integrand, (t, start, end))
    return result

def calc_b_n(n, start, end, gap_length, f):
    if (n == 0):
        return 0

    coeff = calc_not_complex_coeff(gap_length)
    omega_n = calc_omega_n(n, gap_length)
    integrand = coeff * f(t) * sp.sin(omega_n * t)
    
    result = sp.integrate(integrand, (t, start, end))
    return result

def calc_c_n(n, start, end, gap_length, f):
    coeff = calc_complex_coeff(gap_length)
    omega_n = calc_omega_n(n, gap_length)
    integrand = coeff * f(t) * sp.exp(-1j * omega_n * t)

    result = sp.integrate(integrand, (t, start, end))
    return result

def calc_F_N(N, start, end, f):
    gap_length = end - start

    a_0 = calc_a_n(0, start, end, gap_length, f)

    F_N = a_0 / 2
    for n in range(1, N + 1):
        a_n = calc_a_n(n, start, end, gap_length, f)
        b_n = calc_b_n(n, start, end, gap_length, f)
        omega_n = calc_omega_n(n, gap_length)
        F_N += a_n * sp.cos(omega_n * t) + b_n * sp.sin(omega_n * t)

    return F_N

def calc_F_N_sys2(N, start_1, end_1, start_2, end_2, f_1, f_2):
    gap_length = end_2 - start_1

    a_0_1 = calc_a_n(0, start_1, end_1, gap_length, f_1)
    a_0_2 = calc_a_n(0, start_2, end_2, gap_length, f_2)
    a_0 = a_0_1 + a_0_2

    F_N = a_0 / 2
    for n in range(1, N + 1):
        a_n_1 = calc_a_n(n, start_1, end_1, gap_length, f_1)
        a_n_2 = calc_a_n(n, start_2, end_2, gap_length, f_2)
        a_n = a_n_1 + a_n_2

        b_n_1 = calc_b_n(n, start_1, end_1, gap_length, f_1)
        b_n_2 = calc_b_n(n, start_2, end_2, gap_length, f_2)
        b_n = b_n_1 + b_n_2

        omega_n = calc_omega_n(n, gap_length)
        F_N += a_n * sp.cos(omega_n * t) + b_n * sp.sin(omega_n * t)
    
    return F_N

def calc_G_N(N, start, end, f):
    G_N = 0
    gap_length = end - start
    for n in range(-N, N + 1):
        c_n = calc_c_n(n, start, end, gap_length, f)
        omega_n = calc_omega_n(n, gap_length)
        G_N += c_n * sp.exp(1j * omega_n * t)

    return G_N

def calc_G_N_sys2(N, start_1, end_1, start_2, end_2, f_1, f_2):
    G_N = 0
    gap_length = end_2 - start_1
    for n in range(-N, N + 1):
        c_n_1 = calc_c_n(n, start_1, end_1, gap_length, f_1)
        c_n_2 = calc_c_n(n, start_2, end_2, gap_length, f_2)
        c_n = c_n_1 + c_n_2

        omega_n = calc_omega_n(n, gap_length)
        G_N += c_n * sp.exp(1j * omega_n * t)

    return G_N

# TODO do parseval equality
