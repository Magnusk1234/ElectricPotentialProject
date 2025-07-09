import numpy as np

# Constant potential function
def V0_constant(x):
    return 1

# Sinusoidal potential with 2π frequency
def V0_sinusoidal_2(x):
    return np.sin(2*np.pi*x)

# Sinusoidal potential with 3π frequency
def V0_sinusoidal_3(x):
    return np.sin(3*np.pi*x)

# Step potential (1 between x=0.4 and x=0.6)
def V0_step(x):
    return np.heaviside(x-0.4, 1)-np.heaviside(x-0.6, 1)

# Gaussian potential centered at x=0.5 with standard deviation 0.1
def V0_gaussian(x):
    return np.exp(-((x-0.5)**2)/(2*(0.1**2)))

# Polynomial (4th degree) potential centered at x=0.5
def V0_polynomial(x):
    return 1-(x-0.5)**4

