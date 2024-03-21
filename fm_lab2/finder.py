from sympy import sqrt, integrate, E, I, pi
from static import t, omega

coeff = 1 / (sqrt(2 * pi))

def find_fimg(f_t, lim1, lim2):
    integrand = f_t * E ** (-I * omega * t)

    result = integrate(integrand, (t, lim1, lim2))
    return coeff * result

def find_from_fimg(fimg_omega, lim1, lim2):
    integrand = fimg_omega * E ** (I * omega * t)

    result = integrate(integrand, (omega, lim1, lim2))
    return coeff * result

# TODO parseval
