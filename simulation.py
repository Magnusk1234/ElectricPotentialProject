import numpy as np
import matplotlib.pyplot as plt


from solver import electric_potential, electric_field
from plotting import plot_3D_electric_potential_simulation, plot_2D_electric_potential_simulation, plot_electric_field_simulation


def electric_potential_simulation(V0_function, N, resolution):
    """
    Visual test of the electric potential given a boundary condition function V0(x).
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N (int): Number of Fourier terms to use.
        resolution (int): Resolution for the grid along x and y axes.
    """

    # Create a grid of points in the x and y directions
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    # Calculate the electric potential and plot the results
    potential = electric_potential(X_grid, Y_grid, N, V0_function)
    plot_3D_electric_potential_simulation(X_grid, Y_grid, potential, title=f'Potential: {V0_function.__name__}')
    

def electric_field_simulation(V0_function, N, resolution):
    """
    Visual test of the electric field derived from the electric potential given a boundary condition function V0(x).
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N (int): Number of Fourier terms to use.
        resolution (int): Resolution for the grid along x and y axes.
    """

    # Create a grid of points in the x and y directions
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    # Calculate the electric potential and field, and plot the results
    potential = electric_potential(X_grid, Y_grid, N, V0_function)
    Ex, Ey = electric_field(x, y, potential)
    plot_electric_field_simulation(x, y, potential, Ex, Ey, title=f'Electric Field: {V0_function.__name__}')
    

def electric_potential_and_field_simulation(V0_function, N, resolution):
    """
    Full test of the electric potential and field given a boundary condition function V0(x).
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N (int): Number of Fourier terms to use.
        resolution (int): Resolution for the grid along x and y axes.
    """
    
    # Run both potential and field simulation
    electric_potential_simulation(V0_function, N, resolution)
    electric_field_simulation(V0_function, N, resolution)