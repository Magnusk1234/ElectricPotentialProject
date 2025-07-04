import numpy as np
import matplotlib.pyplot as plt

from analysis import calculate_std
from testing import test_potential, test_field
from potentials import*


def main():
    Vc = 1.0
    N = 100
    resolution = 10
    test_potential(V0_sinus_2, Vc, N, resolution)

    test_field(V0_sinus_2, Vc, N, resolution)




if __name__ == "__main__":
    main() 