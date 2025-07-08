import numpy as np
import matplotlib.pyplot as plt

from analysis import convergence_test, potential_profile_test
from testing import test_potential, test_field
from potentials import*


def main():
    Vc = 1.0
    N = 100
    resolution = 100
    N_min = 40
    N_max = 140
    N_interval = 20
    #test_potential(V0_sinus_2, Vc, N, resolution)

    #test_field(V0_sinus_2, Vc, N, resolution)
    convergence_test(V0_constant, Vc, N_min, N_max, N_interval, resolution)

    #potential_profile_test(V0_constant, Vc, N_min, N_max, N_interval, resolution)


if __name__ == "__main__":
    main() 