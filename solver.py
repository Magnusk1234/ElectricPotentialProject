import numpy as np
from scipy.integrate import quad


def Cn(n, V0, Vc):
    integrand = lambda x:V0(Vc,x)*np.sin(n*np.pi*x)
    Cn, _ = quad(integrand, 0, 1)
    return Cn / np.sinh(n*np.pi)

def Electric_potential(X, Y, N, V0, Vc):
    potential = np.zeros((len(X),len(Y)))

    for i in range(1, N+1):
        Cn_value = Cn(i, V0, Vc)
        Vn = Cn_value * np.sinh(i * np.pi * Y) * np.sin(i * np.pi * X)
        potential += Vn 
    return potential

def Electric_field(x, y, N, potential):
    Ey, Ex = np.gradient(-potential, y, x)
    return Ex, Ey

