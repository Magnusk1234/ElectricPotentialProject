import numpy as np
import matplotlib.pyplot as plt

from analysis import convergence_analysis, potential_profile_analysis, full_analysis
from testing import electric_potential_test, electric_field_test
from potentials import*


def main():
    
    N = 100
    resolution = 100
    N_min = 1
    N_max = 50
    N_num = 5
    #electric_potential_test(V0_sinusoidal_2, N, resolution)

    electric_field_test(V0_sinusoidal_2, N, resolution)
    #convergence_test(V0_constant, N_min, N_max, N_num, resolution)

    #potential_profile_test(V0_heaviside, N_min, N_max, N_num, resolution)

    #more alternatives for actions in main + saving plots/data

    
    #test_field(V0_sinusoidal_2, N, resolution)
if __name__ == "__main__":
    main() 