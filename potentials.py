import numpy as np


# constant potential function
def V0_constant(Vc, x):
    return Vc

# sinus 2 potential function
def V0_sinus_2(Vc,x):
    return Vc*np.sin(2*np.pi*x)

# sinus 3 potential function
def V0_sinus_3(Vc,x):
    return Vc*np.sin(3*np.pi*x)

#heaviside potential function
def V0_heaviside(Vc,x):
    return Vc*(np.heaviside(x-0.4, 1)-np.heaviside(x-0.6, 1))

# gaussian potential function
def V0_gaussian(Vc,x):
    return Vc*np.exp(-((x-0.5)**2)/(2*(0.1**2)))

# 4th order polynomial potential function
def V0_polynomial_4th(Vc,x):
    return Vc*(1-(x-0.5)**4)


