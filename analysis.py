import numpy as np
import matplotlib.pyplot as plt

from potentials import*
from solver import Electric_potential
from plotting import plot_convergence_test


def convergence_test(V0_function, Vc, N_min, N_max, N_interval, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    N_values = np.arange(N_min, N_max + 1, N_interval)
    std_values = np.zeros(len(N_values))

    analytical_potential = V0_function(x, Vc)

    for i in range(len(N_values)):

        numeric_potential = Electric_potential(X, Y, N_values[i], V0_function, Vc)[-1, :]
        diff = np.array(numeric_potential) - np.array(analytical_potential)
        
        std_values[i] = np.std(diff)

    plot_convergence_test(N_values, std_values)

        
