import numpy as np
import matplotlib.pyplot as plt
import argparse


from potentials import*
from analysis import convergence_analysis, electric_potential_profile_analysis, fourier_accuracy_analysis
from simulation import electric_potential_simulation, electric_field_simulation, electric_potential_and_field_simulation

potential_functions = {
    "zero": V0_zero,
    "constant": V0_constant,
    "sin": V0_sinusoidal,
    "step": V0_step,
    "gaussian": V0_gaussian
}

def main():
    parser = argparse.ArgumentParser(description="Electric potential and field Simulation and Analysis")


    parser.add_argument("--simulate",action="store_true", help="Run electric potential and field simulation")
    parser.add_argument("--analyze", action="store_true", help="Run convergence and potential profile analysis")

    #common
    parser.add_argument("--potential", type=str,default="constant", choices = potential_functions.keys(),
                        help="Choose boundary condition potential function: zero, constant, sin, step, gaussian")

    parser.add_argument("--resolution", type=int, default=100, help = "Grid resolution for the simulation and analysis")

    #simulation
    parser.add_argument("--N", type=int, default=100, help="Number of Fourier terms for the simulation")

    #analysis
    parser.add_argument("--N_min", type=int, default=1, help="Minimum number of Fourier terms for analysis")
    parser.add_argument("--N_max", type=int, default=50, help="Maximum number of Fourier terms for analysis")
    parser.add_argument("--N_num", type=int, default=10, help="Number of different N values to test in analysis")

    
    args = parser.parse_args()

    
    V0_function = potential_functions[args.potential]

    if not (args.simulate or args.analyze):
        print("No action specified. Use --simulate or --analyze.")
        return
    
    if args.simulate:
        print(f"Running simulation with potential: {args.potential}, N: {args.N}, resolution: {args.resolution}")
        electric_potential_and_field_simulation(V0_function, args.N, args.resolution)

    if args.analyze:
        print(f"Running analysis with potential: {args.potential}, N_min: {args.N_min}, N_max: {args.N_max}, N_num: {args.N_num}, resolution: {args.resolution}")
        fourier_accuracy_analysis(V0_function, args.N_min, args.N_max, args.N_num, args.resolution)




#electric_potential_simulation(V0_constant, N, resolution)

#electric_field_test(V0_sinusoidal_2, N, resolution)
#convergence_analysis(V0_constant, N_min, N_max, N_num, resolution)

#potential_profile_analysis(V0_heaviside, N_min, N_max, N_num, resolution)

#more alternatives for actions in main + saving plots/data


#test_field(V0_sinusoidal_2, N, resolution)




if __name__ == "__main__":
    main() 