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
    

def plot_electric_field(x, y, potential, Ex, Ey, title='Electric Field'):
    plt.figure(figsize=(6, 6))
    plt.quiver(x, y, Ex, Ey, color='black', scale=5)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid()
    