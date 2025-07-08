import numpy as np
from scipy.integrate import quad


def Cn(n, V0_function, Vc):
    Cn, _ = quad(lambda x:2*V0_function(x, Vc)*np.sin(n*np.pi*x), 0, 1)
    return Cn / np.sinh(n*np.pi)

def Electric_potential(X, Y, N, V0_function, Vc):
    potential = np.zeros((len(X),len(Y)))

    for i in range(1, N+1):
        Cn_value = Cn(i, V0_function, Vc)
        Vn = Cn_value * np.sinh(i * np.pi * Y) * np.sin(i * np.pi * X)
        potential += Vn 
    return potential

def Electric_field(x, y, N, potential):
    Ey, Ex = np.gradient(-potential, y, x)
    return Ex, Ey

