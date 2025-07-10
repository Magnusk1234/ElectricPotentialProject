import numpy as np
import matplotlib.pyplot as plt

from solver import electric_potential
from plotting import plot_convergence_analysis, plot_potential_profile_analysis


def convergence_analysis(V0_function, N_min, N_max, N_num, resolution):
    """    
    Analyzes the convergence of the numeric solution of the electric potential by comparing it to the analytical solution.
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N_min (int): Minimum number of Fourier terms.
        N_max (int): Maximum number of Fourier terms.
        N_num (int): Number of different N values to test.
        resolution (int): Resolution for the grid along x and y axes.
    """ 

    # Create a grid of points in the x and y directions
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    # Generate a range of N values for the convergence test
    N_values = np.linspace(N_min, N_max + 1, N_num, dtype=int)
    std_values = np.zeros(len(N_values))

    # Calculate the analytical potential for comparison
    analytical_potential = V0_function(x)

    # Loop through each N value and calculate the numeric potential
    for i in range(len(N_values)):
        numeric_potential = electric_potential(X_grid, Y_grid, N_values[i], V0_function)[-1, :] # get the numeric potential at y=1
        difference = np.array(numeric_potential) - np.array(analytical_potential)   # Calculate the difference between numeric and analytical potential
        std_values[i] = np.std(difference)  # Calculate the standard deviation of the difference

    plot_convergence_analysis(N_values, std_values)     

        

def electric_potential_profile_analysis(V0_function, N_min, N_max, N_num, resolution):
    """
    Analyzes the potential profile at the border for different values of N.
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N_min (int): Minimum number of Fourier terms.
        N_max (int): Maximum number of Fourier terms.
        N_num (int): Number of different N values to test.
        resolution (int): Resolution for the grid along x and y axes.
    """

    # Create a grid of points in the x and y directions
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X_grid, Y_grid = np.meshgrid(x, y)

    # Generate a range of N values for the convergence test
    N_values = np.linspace(N_min, N_max + 1, N_num,dtype=int)
    profiles = {} 

    # Loop through each N value and calculate the numeric potential
    for i in range(len(N_values)):
        potential = electric_potential(X_grid, Y_grid, N_values[i], V0_function)[-1, :] # get the numeric potential at y=1
        profiles[N_values[i]] = potential   #store the potential profile for each N value
    plot_potential_profile_analysis(x, V0_function, profiles)



def fourier_accuracy_analysis(V0_function, N_min, N_max, N_num, resolution):
    """
    Perform full analysis including convergence and potential profile analysis.
    Parameters:
        V0_function (function): Boundary condition function V0(x).
        N_min (int): Minimum number of Fourier terms.
        N_max (int): Maximum number of Fourier terms.
        N_num (int): Number of different N values to test.
        resolution (int): Resolution for the grid along x and y axes.
    """

    # Perform convergence analysis and potential profile analysis
    convergence_analysis(V0_function, N_min, N_max, N_num, resolution)
    electric_potential_profile_analysis(V0_function, N_min, N_max, N_num, resolution)