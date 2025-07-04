import numpy as np
import matplotlib.pyplot as plt

from solver import Electric_potential
from potentials import*
from plotting import plot_std_values


def calculate_std(V0_function, Vc, N_min, N_max, N_interval, resolution,sample_y=1):

    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    N_values = np.arrange(N_min, N_max + 1, N_interval)
    std_values = np.zeros(len(N_values))



    for i, N in enumerate(N_values):
        potential_N = Electric_potential(X, Y, N, V0_function, Vc)
        potential_N_slice = potential_N[-1, : ]
        potential_exact = V0_function(Vc, x)
        std_values[i] = np.std(potential_N_slice - potential_exact)
    plot_std_values(N_values, std_values, title=f'Standard Deviation for {V0_function}')



    