import numpy as np

# 0 potential function
def V0_zero(x):
    return np.zeros_like(x)

# Constant potential function
def V0_constant(x):
    return 1

# Sinusoidal potential with 2π frequency
def V0_sinusoidal(x):
    return np.sin(2*np.pi*x)

# Step potential (1 between x=0.4 and x=0.6)
def V0_step(x):
    return np.heaviside(x-0.4, 1)-np.heaviside(x-0.6, 1)

# Gaussian potential centered at x=0.5 with standard deviation 0.1
def V0_gaussian(x):
    return np.exp(-((x-0.5)**2)/(2*(0.1**2)))


