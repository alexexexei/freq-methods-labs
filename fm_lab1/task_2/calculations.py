import sympy as sp
from static import t

def calc_complex_coeff(gap_len):
    return 1 / gap_len

def calc_omega_n(n, gap_len):
    return (2 * sp.pi * n) / gap_len

def calc_c_n(n, start, end, gap_len, f):
    coeff = calc_complex_coeff(gap_len)
    omega_n = calc_omega_n(n, gap_len)
    integrand = coeff * f(t) * sp.exp(-1j * omega_n * t)

    result = sp.integrate(integrand, (t, start, end))
    return result

def calc_G_N_csys4(N, gap_1: list, gap_2: list, gap_3: list,
                    gap_4: list, f_c_1, f_c_2, f_c_3, f_c_4):
    G_N = 0
    gap_len = gap_4[1] - gap_1[0]
    for n in range(-N, N + 1):
        c_n_1 = calc_c_n(n, gap_1[0], gap_1[1], gap_len, f_c_1)
        c_n_2 = calc_c_n(n, gap_2[0], gap_2[1], gap_len, f_c_2)
        c_n_3 = calc_c_n(n, gap_3[0], gap_3[1], gap_len, f_c_3)
        c_n_4 = calc_c_n(n, gap_4[0], gap_4[1], gap_len, f_c_4)
        c_n = c_n_1 + c_n_2 + c_n_3 + c_n_4

        omega_n = calc_omega_n(n, gap_len)
        G_N += c_n * sp.exp(1j * omega_n * t)

    return G_N
