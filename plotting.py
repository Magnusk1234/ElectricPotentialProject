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
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(6, 6))
    plt.contourf(x, y, potential, levels=50, cmap='plasma')
    plt.colorbar(label='Potential')

    plt.streamplot(X, Y, Ex, Ey, color='white', linewidth=1)

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

