import numpy as np

def calculate_std(V0_function, Vc, N_range, resolution):

    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    N_vals = np.array(N_range)
    std_values = np.zeros(len(N_vals))

    