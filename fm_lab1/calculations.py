import sympy as sp

t = sp.Symbol('t')

def calc_coeff(complex: bool, gap_len):
    if complex:
        return 1 / gap_len
    return 2 / gap_len

def calc_omega_n(n, gap_len):
    return 2 * sp.pi * n / gap_len

def calc_a_n(n, start, end, gap_len, f):
    integrand = f(t)
    if n != 0:
        omega_n = calc_omega_n(n, gap_len)
        integrand *= sp.cos(omega_n * t)
    
    result = sp.integrate(integrand, (t, start, end))

    coeff = calc_coeff(False, gap_len)
    return coeff * result

def calc_b_n(n, start, end, gap_len, f):
    if (n == 0):
        return 0

    omega_n = calc_omega_n(n, gap_len)
    integrand = f(t) * sp.sin(omega_n * t)
    
    result = sp.integrate(integrand, (t, start, end))

    coeff = calc_coeff(False, gap_len)
    return coeff * result

def calc_c_n(n, start, end, gap_len, f):
    omega_n = calc_omega_n(n, gap_len)
    integrand = f(t) * sp.exp(-1j * omega_n * t)

    result = sp.integrate(integrand, (t, start, end))

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
        F_N += a_n * sp.cos(omega_n * t) + b_n * sp.sin(omega_n * t)

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
        F_N += a_n * sp.cos(omega_n * t) + b_n * sp.sin(omega_n * t)

    return F_N

def calc_G_N(N, start, end, f):
    G_N = 0
    gap_len = end - start
    for n in range(-N, N + 1):
        c_n = calc_c_n(n, start, end, gap_len, f)

        omega_n = calc_omega_n(n, gap_len)
        G_N += c_n * sp.exp(1j * omega_n * t)

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
        G_N += c_n * sp.exp(1j * omega_n * t)

    return G_N

def calc_parseval_coeffs(N, start, end, f):
    coeffs = 0
    gap_len = end - start
    for n in range(-N, N + 1):
        c_n = calc_c_n(n, start, end, gap_len, f)

        coeffs += sp.re(c_n) ** 2 + sp.im(c_n) ** 2

    return coeffs

def calc_parseval_square_func(start, end, f):
    integrand = f * sp.conjugate(f)

    result = sp.integrate(integrand, (t, start, end))

    gap_len = end - start
    return (1 / gap_len) * result
