import numpy as np
import matplotlib.pyplot as plt

from solver import electric_potential, electric_field
from plotting import plot_electric_potential_test, plot_electric_field_test, plot_electric_potential_3D_test


def electric_potential_test(V0_function, N, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    potential = electric_potential(X_grid, Y_grid, N, V0_function)
    plot_electric_potential_3D_test(X_grid, Y_grid, potential, title=f'Potential: {V0_function.__name__}')
    

def electric_field_test(V0_function, N, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    potential = electric_potential(X_grid, Y_grid, N, V0_function)
    Ex, Ey = electric_field(x, y, potential)
    plot_electric_field_test(x, y, potential, Ex, Ey, title=f'Field: {V0_function.__name__}')
    