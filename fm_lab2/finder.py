import sympy as sp
from static import t, omega

coeff = 1 / (sp.sqrt(2 * sp.pi))

def find_fimg(f_t, lim1, lim2):
    integrand = f_t * sp.E ** (-sp.I * omega * t)

    result = sp.integrate(integrand, (t, lim1, lim2))
    return coeff * result

def find_from_fimg(fimg_omega, lim1, lim2):
    integrand = fimg_omega * sp.E ** (sp.I * omega * t)

    result = sp.integrate(integrand, (omega, lim1, lim2))
    return coeff * result
