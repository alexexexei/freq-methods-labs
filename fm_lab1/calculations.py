from sympy import integrate, conjugate, cos, sin, re, im, E, I, pi

from static import t


def calc_coeff(complex: bool, gap_len):
    if complex:
        return 1 / gap_len
    return 2 / gap_len


def calc_omega_n(n, gap_len):
    return 2 * pi * n / gap_len


def calc_a_n(n, start, end, gap_len, f):
    integrand = f(t)
    if n != 0:
        omega_n = calc_omega_n(n, gap_len)
        integrand *= cos(omega_n * t)
    
    result = integrate(integrand, (t, start, end))

    coeff = calc_coeff(False, gap_len)
    return coeff * result


def calc_b_n(n, start, end, gap_len, f):
    if (n == 0):
        return 0

    omega_n = calc_omega_n(n, gap_len)
    integrand = f(t) * sin(omega_n * t)
    
    result = integrate(integrand, (t, start, end))

    coeff = calc_coeff(False, gap_len)
    return coeff * result


def calc_c_n(n, start, end, gap_len, f):
    omega_n = calc_omega_n(n, gap_len)
    integrand = f(t) * E ** (-I * omega_n * t)

    result = integrate(integrand, (t, start, end))

    coeff = calc_coeff(True, gap_len)
    return coeff * result


def calc_F_N(N, start, end, f):
    gap_len = end - start

    a_0 = calc_a_n(0, start, end, gap_len, f)

    F_N = a_0 / 2
    for n in range(1, N + 1):
        a_n = calc_a_n(n, start, end, gap_len, f)
        b_n = calc_b_n(n, start, end, gap_len, f)

        omega_n = calc_omega_n(n, gap_len)
        F_N += a_n * cos(omega_n * t) + b_n * sin(omega_n * t)

    return F_N


def calc_F_N_generic(N, gaps: list, functions: list):
    if (len(gaps) != len(functions) 
        or len(gaps) <= 0 
        or len(functions) <= 0):
        return None

    gap_len = gaps[-1][1] - gaps[0][0]

    a_0 = sum(calc_a_n(0, gap[0], gap[1], gap_len, functions[i]) 
              for i, gap in enumerate(gaps))

    F_N = a_0 / 2
    for n in range(1, N + 1):
        a_n = sum(calc_a_n(n, gap[0], gap[1], gap_len, functions[i]) 
                  for i, gap in enumerate(gaps))
        b_n = sum(calc_b_n(n, gap[0], gap[1], gap_len, functions[i]) 
                  for i, gap in enumerate(gaps))

        omega_n = calc_omega_n(n, gap_len)
        F_N += a_n * cos(omega_n * t) + b_n * sin(omega_n * t)

    return F_N


def calc_G_N(N, start, end, f):
    G_N = 0
    gap_len = end - start
    for n in range(-N, N + 1):
        c_n = calc_c_n(n, start, end, gap_len, f)

        omega_n = calc_omega_n(n, gap_len)
        G_N += c_n * E ** (I * omega_n * t)

    return G_N


def calc_G_N_generic(N, gaps: list, functions: list):
    if (len(gaps) != len(functions) 
        or len(gaps) <= 0 
        or len(functions) <= 0):
        return None

    G_N = 0
    gap_len = gaps[-1][1] - gaps[0][0]
    for n in range(-N, N + 1):
        c_n = sum(calc_c_n(n, gap[0], gap[1], gap_len, functions[i]) 
                  for i, gap in enumerate(gaps))
        
        omega_n = calc_omega_n(n, gap_len)
        G_N += c_n * E ** (I * omega_n * t)

    return G_N


def calc_parseval_coeffs(N, start, end, f):
    coeffs = 0
    gap_len = end - start
    for n in range(-N, N + 1):
        c_n = calc_c_n(n, start, end, gap_len, f)

        coeffs += re(c_n) ** 2 + im(c_n) ** 2

    return coeffs


def calc_parseval_coeffs_generic(N, gaps: list, functions: list):
    if (len(gaps) != len(functions) 
        or len(gaps) <= 0 
        or len(functions) <= 0):
        return None
    
    coeffs = 0
    gap_len = gaps[-1][1] - gaps[0][0]
    for n in range(-N, N + 1):
        c_n = sum(calc_c_n(n, gap[0], gap[1], gap_len, functions[i]) 
                  for i, gap in enumerate(gaps))
        
        coeffs += re(c_n) ** 2 + im(c_n) ** 2

    return coeffs


def calc_parseval_square_func(start, end, f):
    integrand = f * conjugate(f)

    result = integrate(integrand, (t, start, end))

    gap_len = end - start
    return (1 / gap_len) * result


def calc_parseval_square_func_generic(gaps: list, functions: list):
    result = 0
    for i in range(len(gaps)):
        integrand = functions[i] * conjugate(functions[i])
        result += integrate(integrand, (t, gaps[i][0], gaps[i][1]))
    
    gap_len = gaps[-1][1] - gaps[0][0]
    return (1 / gap_len) * result
