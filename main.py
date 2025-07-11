import numpy as np
import matplotlib.pyplot as plt
import sys

from potentials import*
from analysis import convergence_analysis, electric_potential_profile_analysis, fourier_accuracy_analysis
from simulation import electric_potential_simulation, electric_field_simulation, electric_potential_and_field_simulation

# Define the potential functions
potential_functions = {
    "zero": V0_zero,
    "constant": V0_constant,
    "sin": V0_sinusoidal,
    "step": V0_step,
    "gaussian": V0_gaussian
}

def main():
    print("Chose simulation, or analysis")
    mode = input("Enter 's' for simulation or 'a' for analysis: ").strip().lower()

    # Simulation mode
    if mode == "s":
        # Run simulation
        potential = input("Enter potential function (zero, constant, sin, step, gaussian): ").strip().lower() or "constant"
        if potential not in potential_functions:
            print(f"Invalid potential function '{potential}'. Using default 'constant'.")
            potential = "constant"

        try:
            N = int(input("Enter number of Fourier terms (N): ")) or 10
            resolution = int(input("Enter grid resolution: ")) or 100
            electric_potential_and_field_simulation(potential_functions[potential], N, resolution)
        except ValueError:
            print("Invalid input for N or resolution. Using default values (N=10, resolution=100).")
            electric_potential_and_field_simulation(potential_functions["constant"], 10, 100)

    # Analysis mode
    elif mode == "a":
        potential = input("Enter potential function (zero, constant, sin, step=default, gaussian): ").strip().lower() or "step"
        if potential not in potential_functions:
            print(f"Invalid potential function '{potential}'. Using default 'step'.")
            potential = "step"

        try:
            N_min = int(input("Enter minimum number of Fourier terms (N_min): ")) or 1
            N_max = int(input("Enter maximum number of Fourier terms (N_max): ")) or 50
            N_num = int(input("Enter number of different N values to test (N_num): ")) or 10
            resolution = int(input("Enter grid resolution: ")) or 100
            fourier_accuracy_analysis(potential_functions[potential], N_min, N_max, N_num, resolution)
        except ValueError:
            print("Invalid input for N_min, N_max, N_num, or resolution. Using default values.")
            fourier_accuracy_analysis(potential_functions["step"], 1, 50, 10, 100)

if __name__ == "__main__":
    main() 