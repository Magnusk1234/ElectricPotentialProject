import numpy as np
import matplotlib.pyplot as plt

from solver import Electric_potential, Electric_field
from plotting import plot_electric_potential, plot_electric_field


def test_potential(V0_function, Vc, N, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    potential = Electric_potential(X, Y, N, V0_function, Vc)
    plot_electric_potential(X, Y, potential, title=f'Potential: {V0_function.__name__}')
    

def test_field(V0_function, Vc, N, resolution):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    potential = Electric_potential(X, Y, N, V0_function, Vc)
    Ex, Ey = Electric_field(x, y, N, potential)

    plot_electric_field(x, y, potential, Ex, Ey, title=f'Field: {V0_function.__name__}')
    