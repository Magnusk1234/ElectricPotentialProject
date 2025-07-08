import numpy as np


# constant potential function
def V0_constant(x, Vc):
    return Vc

# sinus 2 potential function
def V0_sinus_2(x, Vc):
    return Vc*np.sin(2*np.pi*x)

# sinus 3 potential function
def V0_sinus_3(x, Vc):
    
    return Vc*np.sin(3*np.pi*x)

#heaviside potential function
def V0_heaviside(x, Vc):
    
    return Vc*(np.heaviside(x-0.4, 1)-np.heaviside(x-0.6, 1))

# gaussian potential function
def V0_gaussian(x, Vc):
    return Vc*np.exp(-((x-0.5)**2)/(2*(0.1**2)))

# 4th order polynomial potential function
def V0_polynomial_4th(x, Vc):
    return Vc*(1-(x-0.5)**4)

