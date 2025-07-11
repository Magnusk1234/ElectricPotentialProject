import pytest
import numpy as np
import subprocess

from potentials import*
from solver import Cn, electric_potential, electric_field


def test_Cn_zero_function():
    # Test for the zero potential function
    for n in range(1, 6):
        Cn_value = Cn(n, V0_zero)
        assert abs(Cn_value) < 1e-10, f"Expected C_{n} = 0, got {Cn_value}"



def test_Cn_sine_function_match():
    # Test for the sine potential function
    for k in range(1, 10):
        V0_sinusoidal = lambda x: np.sin(k * np.pi * x)
        for n in range(1, 10):
            Cn_value = Cn(n, V0_sinusoidal)
            expected_value = 1/(np.sinh(k * np.pi)) if n == k else 0
            if n == k:
                assert abs(Cn_value - expected_value) < 1e-4, f"Expected C_{n} = {expected_value}, got {Cn_value}"
            else:
                assert abs(Cn_value) < 1e-4, f"Expected C_{n} = 0 for n≠k, got {Cn_value}"



def test_electric_potential_shape():
    # Test for the electric potential function shape
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X_grid, Y_grid = np.meshgrid(x, y)

    N = 10
    potential = electric_potential(X_grid, Y_grid, N, V0_constant)
    
    assert potential.shape == (100, 100), "Electric potential shape mismatch"


def test_electric_field_shape():
    # Test for the electric field function shape
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X_grid, Y_grid = np.meshgrid(x, y)
    
    N = 10
    potential = electric_potential(X_grid, Y_grid, N, V0_constant)
    
    Ex, Ey = electric_field(x, y, potential)
    
    assert Ex.shape == (100, 100), "Electric field Ex shape mismatch"
    assert Ey.shape == (100, 100), "Electric field Ey shape mismatch"


def test_electric_potential_zero():
    # Test for the electric potential function with zero potential
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X_grid, Y_grid = np.meshgrid(x, y)
    
    N = 10
    potential = electric_potential(X_grid, Y_grid, N, V0_zero)
    
    assert np.allclose(potential, 0), "Electric potential should be zero everywhere for V0_zero"

def test_electric_field_zero_gradient():
    # Test for the electric field function with zero potential
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X_grid, Y_grid = np.meshgrid(x, y)
    
    N = 10
    potential = electric_potential(X_grid, Y_grid, N, V0_zero)
    
    Ex, Ey = electric_field(x, y, potential)
    
    assert np.allclose(Ex, 0, atol=1e-10), "Electric field Ex should be zero everywhere for V0_zero"
    assert np.allclose(Ey, 0, atol=1e-10), "Electric field Ey should be zero everywhere for V0_zero"


