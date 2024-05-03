import numpy as np
import matplotlib.pyplot as plt


def buildFunc(func, fz1, fz2, clr='b', ttl=None, grid=True):
    plt.plot(func, color=clr)
    plt.title(ttl)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.grid(grid)
    plt.show()


def getNoise(a, t):
    return a*(np.random.rand(len(t))-0.5)


def numericalDiff(y, dt):
    shtrih = []
    for i in range(len(y) - 1):
        shtrih_i = (y[i+1]-y[i])/dt
        shtrih.append(shtrih_i)

    return shtrih


def spectralDiff():
    ...


dt = 0.1
t = np.arange(-100, 100 + dt, dt)
y = np.sin(t)
buildFunc(y, 12, 6, ttl='Clear sine')

a = 2
sh = getNoise(a, t)
buildFunc(sh, 12, 6, ttl=f'Noise, a={a}')

y += sh
buildFunc(y, 12, 6, ttl='Noisy sine')

ns = numericalDiff(y, dt)
buildFunc(ns, 12, 6, ttl='Numerical derivative of sine')