import numpy as np
from scipy.integrate import quad


def Cn(n, V0, Vc):
    integrand = lambda x:V0(x)*np.sin(n*np.pi*x)
    Cn, _ = quad(integrand, 0, 1)
    return Cn / np.sinh(n*np.pi)

def Electric_potential(x, y, N, V0, Vc):
    V = np.zeros(len(x),len(y))

    for i in range(1, N+1):
        Cn_value = Cn(n, V0, Vc)
        Vn = Cn_value * np.sinh(i * np.pi * y) * np.sin(i * np.pi * x)
        V += Vn
    return V

def 