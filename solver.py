import numpy as np
from scipy.integrate import quad


def Cn(n, V0_function): 
    """
    Calculate the n-th Fourier coefficient Cn for the potential function.
    Parameters:
        n (int): The term index in the Fourier series.
        V0_function (function): Function representing the potential at the boundary V0(x).
    Returns:
        float: The n-th Fourier coefficient.
    """

    # Integrate to find the Fourier coefficient Cn using quad
    Cn, _ = quad(lambda x: 2 * V0_function(x) * np.sin(n*np.pi*x), 0, 1)
    return Cn / np.sinh(n*np.pi)


def electric_potential(X_grid, Y_grid, N, V0_function):
    """
    Calculate the electric potential V(x, y) using Fourier sine series expansion.
    Parameters:
        X_grid (np.ndarray): 2D array of x-coordinates.
        Y_grid (np.ndarray): 2D array of y-coordinates.
        N (int): Number of terms used in the Fourier series.
        V0_function (function): Function defining the potential at the boundaries.
    Returns:
        np.ndarray: 2D array of electric potential values.
    """

    
    potential = np.zeros((len(X_grid),len(Y_grid)))

    # Sum over the Fourier terms
    for i in range(1, N+1):
        Cn_value = Cn(i, V0_function)   # i-th Fourier coefficient
        Vn = Cn_value * np.sinh(i * np.pi * Y_grid) * np.sin(i * np.pi * X_grid)    # i-th term
        potential += Vn
    return potential


def electric_field(x, y, potential):
    """
    Calculate the electric field components from the potential.
    Parameters:
        x (np.ndarray): 1D array of x-coordinates.
        y (np.ndarray): 1D array of y-coordinates.
        N (int): Number of terms in the Fourier series.
        potential (np.ndarray): 2D array of electric potential values.  
    Returns:
        tuple: (Ex, Ey) where Ex and Ey are 2D arrays of electric field components in x and y directions.
    """

    # Use np.gradient to compute negative gradient of the potential (electric field)
    Ey, Ex = np.gradient(-potential, y, x) 
    return Ex, Ey

