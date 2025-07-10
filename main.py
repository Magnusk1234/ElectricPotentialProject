import numpy as np
import matplotlib.pyplot as plt
import argparse


from potentials import*
from analysis import convergence_analysis, potential_profile_analysis, fourier_accuracy_analysis
from simulation import electric_potential_simulation, electric_field_simulation, electric_potential_and_field_simulation



def main():

    
    N = 100
    resolution = 100
    N_min = 1
    N_max = 50
    N_num = 10

    electric_potential_simulation(V0_constant, N, resolution)

    #electric_field_test(V0_sinusoidal_2, N, resolution)
    #convergence_analysis(V0_constant, N_min, N_max, N_num, resolution)

    #potential_profile_analysis(V0_heaviside, N_min, N_max, N_num, resolution)

    #more alternatives for actions in main + saving plots/data

    
    #test_field(V0_sinusoidal_2, N, resolution)




if __name__ == "__main__":
    main() 