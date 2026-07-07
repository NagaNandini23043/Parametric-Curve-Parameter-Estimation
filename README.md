# Parametric Curve Parameter Estimation

Parameter estimation of a parametric curve using optimization techniques to recover the unknown variables **θ (Theta), M, and X** by minimizing the **L1 (Manhattan) distance** between the observed dataset and the predicted curve.

---

# Objective

The objective of this project is to estimate the unknown parameters **θ**, **M**, and **X** of a parametric curve using the observed data points provided in `xy_data.csv`.

Instead of solving the equations analytically, the problem is formulated as a global optimization task. Multiple optimization techniques are implemented and compared to identify the parameter values that produce the minimum L1 distance.

---

# Problem Statement

The parametric curve is defined as


$$
x(t) = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
$$

$$
y(t) = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
$$

where the unknown parameters are

- θ (Theta)
- M
- X

### Parameter Constraints

| Parameter | Range |
|-----------|--------|
| θ | 0° – 50° |
| M | -0.05 – 0.05 |
| X | 0 – 100 |
| t | 6 – 60 |

The provided dataset contains only the observed **(x, y)** coordinates. The unknown parameters must be estimated such that the generated curve best fits the observed data.

---

# Methodology

The problem is solved using optimization-based parameter estimation.

The workflow consists of:

1. Load the observed dataset.
2. Generate a predicted curve using candidate values of θ, M and X.
3. Compute the Mean L1 Distance between the observed and predicted curves.
4. Update the parameters using optimization algorithms.
5. Select the parameter combination that minimizes the objective function.
6. Compare the performance of different optimization techniques.

---

# Optimization Models

Two optimization approaches were implemented and compared.

## 1. Random Search

- Randomly samples the parameter space.
- Evaluates the L1 distance for each sample.
- Retains the best parameter combination.

### Advantages

- Simple to implement
- No gradient required

### Limitations

- Slow convergence
- May require many iterations

---

## 2. Differential Evolution

- Population-based global optimization algorithm.
- Uses mutation, crossover and selection.
- Efficiently searches the parameter space.

### Advantages

- Faster convergence
- Better global search capability
- Produces lower L1 distance than Random Search

---

# Project Structure

```
Parametric-Curve-Parameter-Estimation
│
├── README.md
│
├── data
│   └── xy_data.csv
│
├── src
│   ├── plot_dataset.py
│   ├── random_search.py
│   ├── differential_evolution.py
│   └── direct_values.py
│
└── results
    ├── original_curve.png
    ├── random_search_curve.png
    ├── differential_evolution_curve.png
    ├── convergence_plot.png
    └── comparison_table.csv
```


---

# Workflow

```
Input Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Generate Parametric Curve
      │
      ▼
Random Search
      │
      ├─────────────┐
      ▼             │
Differential Evolution
      │             │
      └──────┬──────┘
             ▼
Compute L1 Distance
             ▼
Best Parameters
             ▼
Result Visualization
```

---

# Results

The optimization algorithms estimate the unknown parameters that minimize the L1 distance between the observed and predicted curves.

The following outputs are generated:

- Original Dataset Plot
- Predicted Curve
- Curve Comparison
- Convergence Plot
- Estimated Parameters
- Minimum L1 Distance
- Execution Time

---

# Model Comparison

| Metric | Random Search | Differential Evolution |
|---------|---------------|-------------------------|
| Theta | 28.309299 | 28.118 |
| M | 0.011215 | 0.02138 |
| X | 54.925127 | 54.900 |
| L1 Distance | 25.265734 | 25.24339 |
| Execution Time | 1.6000 sec | 1.5000 sec |



---

# Future Improvements

- Recover the unknown parameter **t** automatically instead of assuming uniformly sampled values.
- Compare additional optimization techniques such as Grid Search and Particle Swarm Optimization.
- Improve robustness for noisy datasets.
- Parallelize optimization to reduce execution time.

---

# Author

**J. Naga Nandini**
