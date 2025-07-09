import numpy as np
import matplotlib.pyplot as plt

from solver import electric_potential
from plotting import plot_convergence_test, plot_potential_profile_test


def convergence_test(V0_function, N_min, N_max, N_num, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    N_values = np.linspace(N_min, N_max + 1, N_num, dtype=int)
    std_values = np.zeros(len(N_values))
    analytical_potential = V0_function(x)

    for i in range(len(N_values)):
        numeric_potential = electric_potential(X_grid, Y_grid, N_values[i], V0_function)[-1, :]
        difference = np.array(numeric_potential) - np.array(analytical_potential)
        std_values[i] = np.std(difference)

    plot_convergence_test(N_values, std_values)

        

def potential_profile_test(V0_function, N_min, N_max, N_num, resolution):

    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    N_values = np.linspace(N_min, N_max + 1, N_num,dtype=int)
    profiles = {}

    for N in N_values:
        potential = electric_potential(X_grid, Y_grid, N, V0_function)[-1, :]
        profiles[N] = potential
        plt.plot(x, potential, label=f'N={N}')
    plot_potential_profile_test(x, V0_function, profiles)