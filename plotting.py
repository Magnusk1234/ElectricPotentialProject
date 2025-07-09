import numpy as np
import matplotlib.pyplot as plt


def plot_electric_potential_3D_test(X_grid, Y_grid, potential, title='Electric Potential in 3D'):
    """
    Plot the electric potential in 3D.
    Parameters:
        X_grid (np.ndarray): 2D array of x-coordinates.
        Y_grid (np.ndarray): 2D array of y-coordinates.
        potential (np.ndarray): 2D array of electric potential values.
        title (str): Title of the plot.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X_grid, Y_grid, potential, cmap='plasma', edgecolor='none')
    ax.set_title(title)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Potential')
    plt.colorbar(ax.plot_surface(X_grid, Y_grid, potential, cmap='plasma', edgecolor='none'), label='Potential')
    plt.show()


def plot_electric_potential_test(x, y, potential, title='Electric Potential'):
    """
    Plot the electric potential as a contour plot.
    Parameters:
        x (np.ndarray): 1D array of x-coordinates.
        y (np.ndarray): 1D array of y-coordinates.
        potential (np.ndarray): 2D array of electric potential values.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(6, 6))
    plt.contourf(x, y, potential, levels=50, cmap='plasma')
    plt.colorbar(label='Potential')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()
    

def plot_electric_field_test(x, y, potential, Ex, Ey, title='Electric Field'):
    """
    Plot the electric field as a contour plot with streamlines.     
    Parameters:
        x (np.ndarray): 1D array of x-coordinates.
        y (np.ndarray): 1D array of y-coordinates.
        potential (np.ndarray): 2D array of electric potential values.
        Ex (np.ndarray): 2D array of electric field component in the x-direction.
        Ey (np.ndarray): 2D array of electric field component in the y-direction.
        title (str): Title of the plot.
    """ 
    X_grid, Y_grid = np.meshgrid(x, y)

    plt.figure(figsize=(6, 6))
    plt.contourf(x, y, potential, levels=50, cmap='plasma')
    plt.colorbar(label='Potential')
    plt.streamplot(X_grid, Y_grid, Ex, Ey, color='white', linewidth=1)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()
    plt.tight_layout()
    

def plot_convergence_test(N_values, std_values):
    """
    Plot the convergence test results.  
    Parameters:
        N_values (np.ndarray): Array of number of terms used in the Fourier series.
        std_values (np.ndarray): Array of standard deviations of potentials with different N values.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(N_values, std_values, marker='o')
    plt.yscale('log')
    plt.xlabel('Number of Terms (N)')
    plt.ylabel('Difference in Potential')
    plt.title('Convergence Test')
    plt.grid(True)
    plt.show()


def plot_potential_profile_test(x, V0_function, profiles):
    """    
    Plot the potential profiles at the border for different N values.
    Parameters:     
        x (np.ndarray): 1D array of x-coordinates.
        V0_function (function): Function representing the potential at the boundary V0(x).
        profiles (dict): Dictionary containing potential profiles for different N values.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(x, V0_function(x), label='Analytical Potential', color='black', linewidth=2)   #plot analytical potential
    for N, potential in profiles.items():   
        plt.plot(x, potential, label=f'N={N}')      # plot numerical potential for each N value
    plt.title('Electric Potential Comparison')
    plt.xlabel('x')
    plt.ylabel('Potential')
    plt.grid(True)
    plt.legend()
    plt.show()