# ElectricPotentialProject

## Description
This project solves the **Laplace equation** to simulate the electric potential in a square, hollow 2D tube. A numerical solution will be obtained using a fourier sine series

## Theory
The dimensionless Laplace equation is given by:
-figure laplace

and for this project the boundrary conditions will be:
-figure boundrary


The solution to the equation is derived using seperation of variables
given by fourier sine series
- solution

with fourier coefficents \( C_n \) are computed using:
- C_n formula

numerical approximation 

## How to run



## Structure
the project consists of 6 python files:

- `main.py`: running simulation
- `solver.py`: Contains functions for solving the 2D Laplace equation using Fourier series to compute the potential and electric field.
- `potentials.py`: Defines different possible boundrary conditions \(V_0(x)\) used in the simulation.
- `analysis.py`: 
- `plotting.py`: Generates various plots for electric potential and electric field tests. Along with plots for analysis of convergence and potential profiles for different N values.
- `simulation.py`: Functions to simulate the potential and electric field.
- `testing.py`: 


## Refrences
