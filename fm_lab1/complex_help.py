from numpy import sin, cos, pi, exp


def res(n):
    if n == 0:
        return 0
    return 1 / (2 * pi) *\
          (4 / n * sin(n * pi / 4) - 4 / n * cos(n * pi / 4) + 16 / (pi * n ** 2) * sin(n * pi / 4)\
           - 2 / n * (1j * (exp(-1j * n * 3 * pi / 4) + exp(-1j * n * pi / 4)) + (4 / (pi * n) + 1 ) * (exp(-1j * n * 3 * pi / 4) - exp(-1j * n * pi / 4)))\
           - 2j / n * (1j * (exp(-1j * n * 5 * pi / 4) + exp(-1j * n * 3 * pi / 4)) + (4 / (pi * n) + 1) * (exp(-1j * n * 5 * pi / 4) - exp(-1j * n * 3 * pi / 4)))\
           + 2 / n * (1j * (exp(-1j * n * 7 * pi / 4) + exp(-1j * n * 5 * pi / 4)) + (4 / (pi * n) + 1) * (exp(-1j * n * 7 * pi / 4) - exp(-1j * n * 5 * pi / 4))))


n = 1
print(res(n))