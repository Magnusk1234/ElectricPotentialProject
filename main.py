import numpy as np
import matplotlib.pyplot as plt

from analysis import convergense_test
from testing import test_potential, test_field
from potentials import*


def main():
    Vc = 1.0
    N = 100
    resolution = 100
    N_min = 50
    N_max = 150
    N_interval = 10
    #test_potential(V0_sinus_2, Vc, N, resolution)

    #test_field(V0_sinus_2, Vc, N, resolution)
    convergense_test(V0_heaviside, Vc, N_min, N_max, N_interval, resolution)




if __name__ == "__main__":
    main() 