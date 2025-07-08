import numpy as np
import matplotlib.pyplot as plt

from analysis import convergence_test, potential_profile_test
from testing import test_potential, test_field
from potentials import*


def main():
    Vc = 1.0
    N = 100
    resolution = 100
    N_min = 1
    N_max = 50
    N_num = 5
    #test_potential(V0_sinus_2, Vc, N, resolution)

    #test_field(V0_sinus_2, Vc, N, resolution)
    #convergence_test(V0_constant, Vc, N_min, N_max, N_num, resolution)

    potential_profile_test(V0_heaviside, Vc, N_min, N_max, N_num, resolution)


if __name__ == "__main__":
    main() 