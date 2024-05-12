def W_1f(w, T):
    p = 1j * w
    return 1 / (T * p + 1)


def W_2f(w, T_1, T_2, T_3):
    p = 1j * w
    return (T_1 * p + 1) ** 2 / ((T_2 * p + 1) * (T_3 * p + 1))