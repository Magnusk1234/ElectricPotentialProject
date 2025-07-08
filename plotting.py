import numpy as np
import matplotlib.pyplot as plt

def plot_electric_potential(x, y, potential, title='Electric Potential'):
    plt.figure(figsize=(6, 6))
    plt.contourf(x, y, potential, levels=50, cmap='plasma')
    plt.colorbar(label='Potential')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()
    

def plot_electric_field(x, y, potential, Ex, Ey, title='Electric Field'):
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
    plt.figure(figsize=(8, 6))
    plt.plot(N_values, std_values, marker='o')
    plt.yscale('log')
    plt.xlabel('Number of Terms (N)')
    plt.ylabel('Difference in Potential')
    plt.title('Convergence Test')
    plt.grid(True)
    plt.show()

def plot_potential_profile_test(x, V0_function, Vc, profiles):
    plt.figure(figsize=(8, 6))
    plt.plot(x, V0_function(x, Vc), label='Analytical Potential', color='black', linewidth=2)
    for N, potential in profiles.items():
        plt.plot(x, potential, label=f'N={N}')
    plt.title('Electric Potential Comparison')
    plt.xlabel('x')
    plt.ylabel('Potential')
    plt.grid(True)
    plt.legend()
    plt.show()