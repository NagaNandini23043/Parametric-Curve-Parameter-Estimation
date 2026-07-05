# Parametric-Curve-Parameter-Estimation
Parameter estimation of a parametric curve using optimization techniques to recover unknown variables (theta, M, X) by minimizing the L1 distance between observed and predicted points.
----
## Objective:
The objective of this assignment is to estimate the unknown parameters θ (Theta), M and X of a given parametric curve using a set of observed data points provided in the “xy_data.csv” file. The goal is to determine the parameter values that generate a curve that best fits the given data by minimizing the L1 (Manhattan) distance between the observed and predicted points.
----------------------------------------------------------------------------------
## Problem Statement:
Given parametric equations are:
\[x=t\cos{\theta}-e^{M\left|t\right|}\sin{(0.3t)}\sin{(\theta)+X}\]
\]y=42+t\sin{(\theta)}+\ e^{M\left|t\right|}\sin{(0.3t)}\cos{(\theta)}\]

The unknown parameters to be estimated are:

- **θ (Theta)**
- **M**
- **X**

### Parameter Constraints

| Parameter | Range |
|------------|-------|
| θ | 0° to 50° |
| M | -0.05 to 0.05 |
| X | 0 to 100 |
| t | 6 to 60 |

The dataset only contains the coordinate values of (x,y), while the values of θ, M, and X are unknown and must be estimated.
------
# Approach:
The whole problem is treated as a parameter estimation and global optimization problem. Instead of solving the equations analytically, an optimization-based approach is used. The optimization algorithm repeatedly generates candidate values of θ, M and X, constructs the corresponding curve using the parametric equations. Compares it with the observed dataset and updates the parameters until the overall error is minimized.

## Project Structure

```
Parametric-Curve-Parameter-Estimation/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── xy_data.csv
│
├── src/
│   ├── curve_model.py
│   ├── parameter_estimation.py
│   ├── optimization.py
│   ├── l1_distance.py
│   └── visualization.py
│
├── results/
└── Architectural Diagrams
'''



