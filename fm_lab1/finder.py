from calculations import calc_a_n, calc_b_n, calc_c_n, calc_parseval_coeffs, calc_parseval_square_func, calc_parseval_coeffs_generic, calc_parseval_square_func_generic


def find_a_b_c(N, f, gaps, gap_len):
    a_N = calc_a_n(N, gaps[0][0], gaps[-1][1], gap_len, f)
    if (not isinstance(a_N, int)):
        a_N = a_N.evalf()

    b_N = calc_b_n(N, gaps[0][0], gaps[-1][1], gap_len, f)
    if (not isinstance(b_N, int)):
        b_N = b_N.evalf()

    c_N = calc_c_n(N, gaps[0][0], gaps[-1][1], gap_len, f)
    if (not isinstance(c_N, int)):
        c_N = c_N.evalf()

    print(f'a_{N}={a_N}')
    print(f'b_{N}={b_N}')
    print(f'c_{N}={c_N}')


def sum_a_n(N, gaps, gap_len, funcs):
    a_n = sum(
        calc_a_n(N, gap[0], gap[1], gap_len, funcs[i])
        for i, gap in enumerate(gaps))

    if (isinstance(a_n, int)):
        return a_n
    return a_n.evalf()


def sum_b_n(N, gaps, gap_len, funcs):
    b_n = sum(
        calc_b_n(N, gap[0], gap[1], gap_len, funcs[i])
        for i, gap in enumerate(gaps))

    if (isinstance(b_n, int)):
        return b_n
    return b_n.evalf()


def sum_c_n(N, gaps, gap_len, funcs):
    c_n = sum(
        calc_c_n(N, gap[0], gap[1], gap_len, funcs[i])
        for i, gap in enumerate(gaps))

    if (isinstance(c_n, int)):
        return c_n
    return c_n.evalf()


def find_a_b_c_2(N, gaps, gap_len, funcs):
    a_0 = sum_a_n(0, gaps, gap_len, funcs)
    a_1 = sum_a_n(1, gaps, gap_len, funcs)
    a_2 = sum_a_n(2, gaps, gap_len, funcs)
    a_N = sum_a_n(N, gaps, gap_len, funcs)

    b_0 = sum_b_n(0, gaps, gap_len, funcs)
    b_1 = sum_b_n(1, gaps, gap_len, funcs)
    b_2 = sum_b_n(2, gaps, gap_len, funcs)
    b_N = sum_b_n(N, gaps, gap_len, funcs)

    c_0 = sum_c_n(0, gaps, gap_len, funcs)
    c_1 = sum_c_n(1, gaps, gap_len, funcs)
    c_2 = sum_c_n(2, gaps, gap_len, funcs)
    c_N = sum_c_n(N, gaps, gap_len, funcs)

    print(f'a_0={a_0}\na_1={a_1}\na_2={a_2}\na_{N}={a_N}\n')
    print(f'b_0={b_0}\nb_1={b_1}\nb_2={b_2}\nb_{N}={b_N}\n')
    print(f'c_0={c_0}\nc_1={c_1}\nc_2={c_2}\nc_{N}={c_N}\n')


def find_c_gen(N, gaps, gap_len, funcs):
    c_0 = sum_c_n(0, gaps, gap_len, funcs)
    c_1 = sum_c_n(1, gaps, gap_len, funcs)
    c_2 = sum_c_n(2, gaps, gap_len, funcs)
    c_N = sum_c_n(N, gaps, gap_len, funcs)

    print(f'c_0={c_0}\nc_1={c_1}\nc_2={c_2}\nc_{N}={c_N}\n')


def find_parseval(N, f, f_t, gaps):
    coeffs_sum = calc_parseval_coeffs(N, gaps[0][0], gaps[-1][1], f)
    sqf_res = calc_parseval_square_func(gaps[0][0], gaps[-1][1], f_t)

    print(f'coeffs_sum={coeffs_sum.evalf()}')
    print(f'sqf_res={sqf_res.evalf()}')


def find_parseval_gen(N, gaps, funcs, funcs_t):
    coeffs_sum = calc_parseval_coeffs_generic(N, gaps, funcs)
    sqf_res = calc_parseval_square_func_generic(gaps, funcs_t)

    print(f'coeffs_sum={coeffs_sum.evalf()}')
    print(f'sqf_res={sqf_res.evalf()}')
