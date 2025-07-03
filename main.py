import numpy as np
import matplotlib.pyplot as plt
from testing import test_potential
from testing import test_field

from potentials import (
    V0_constant,
    V0_sinus_2,
    V0_sinus_3,
    V0_heaviside,
    V0_gaussian,
    V0_polynomial_4th
)


def main():
    Vc = 1.0
    N = 100
    resolution = 10
    test_potential(V0_sinus_2, Vc, N, resolution)

    test_field(V0_sinus_2, Vc, N, resolution)




if __name__ == "__main__":
    main() 