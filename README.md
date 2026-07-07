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

# Overall Workflow

```
Observed Dataset (xy_data.csv)
      │
      ▼
Load Dataset using Pandas
      │
      ▼
Generate Parameter t
      │
      ▼
Generate Parametric Curve
      │
      ▼
Compute Mean L1 Distance
      │
      ├─────────────┐
      ▼             ▼  
Random Search   Differential Evolution
      │             │
      └──────┬──────┘
             ▼
Estimate Best $\theta$, M and X
             │
             ▼
Visualize Curve Comparison
             │
             ▼
Evaluate Results
```
---

# Explanation of Complete Process and Steps Followed
## Step 1: Understanding the Problem
The objective of this project is to estimate the unknown parameters **θ (Theta), M, and X** of a parametric curve using the observed data points provided in `xy_data.csv`.

The mathematical model of the curve is defined as

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The values of **θ**, **M**, and **X** are unknown and must be estimated such that the generated curve closely matches the observed dataset.

The quality of the estimated parameters is measured using the **Mean L1 (Manhattan) Distance** between the observed and predicted coordinates.

---

## Step 2: Loading the Dataset

The observed dataset is stored in `xy_data.csv`.

The program reads the dataset using the Pandas library and extracts the x and y coordinates.

```python
data = pd.read_csv("xy_data.csv")

actual_x = data.iloc[:,0].values
actual_y = data.iloc[:,1].values
```

The number of observed points is then calculated, and a uniformly spaced parameter vector `t` is generated in the interval **6 to 60**.

```python
t = np.linspace(6,60,n)
```

This parameter is used to generate the predicted parametric curve.

---

## Step 3: Visualizing the Dataset

Before performing optimization, the dataset is visualized using Matplotlib.

The file `plot_dataset.py` plots

- observed data points
- connected curve

This helps verify that the dataset has been loaded correctly and provides an initial understanding of the curve shape.

---

## Step 4: Generating the Parametric Curve

A reusable function named `generate_curve()` is implemented.

The function accepts

- Theta (degrees)
- M
- X

and computes the predicted coordinates using the given mathematical equations.

The angle is first converted from degrees to radians.

```python
theta = np.deg2rad(theta_deg)
```

The predicted x and y coordinates are then computed using NumPy operations.

The function returns

- predicted x coordinates
- predicted y coordinates

for the current parameter values.

---

## Step 5: Defining the Objective Function

The optimization problem is converted into a minimization problem.

For every candidate solution, the predicted curve is generated and compared with the observed dataset.

The Mean L1 Distance is calculated as

$$
L_1=\frac{1}{n}\sum_{i=1}^{n}
\left(
|x_i-\hat{x}_i|
+
|y_i-\hat{y}_i|
\right)
$$

where

- $(x_i,y_i)$ are the observed points
- $(\hat{x}_i,\hat{y}_i)$ are the predicted points.

A smaller L1 distance indicates a better fit between the generated curve and the observed data.

---

## Step 6: Parameter Search using Random Search

The first optimization technique implemented is **Random Search**.

The algorithm performs the following steps:

1. Randomly generate values of θ, M and X within the allowed ranges.
2. Generate the corresponding parametric curve.
3. Compute the Mean L1 Distance.
4. Store the parameter combination if it produces a lower error than the current best solution.
5. Repeat the process for 10,000 iterations.

Parameter ranges used are

| Parameter | Range |
|-----------|-------|
| θ | 0° – 50° |
| M | -0.05 – 0.05 |
| X | 0 – 100 |

During execution, the best L1 distance from every iteration is stored to visualize the convergence behaviour.

---

## Step 7: Parameter Estimation using Differential Evolution

The second optimization method is **Differential Evolution**, which is a population-based global optimization algorithm.

Unlike Random Search, Differential Evolution improves candidate solutions through

- mutation
- crossover
- selection

instead of selecting parameters completely at random.

The implementation uses the following configuration:

- Strategy: **best1bin**
- Population Size: **20**
- Maximum Iterations: **500**
- Mutation Factor: **0.5–1.0**
- Recombination Rate: **0.7**
- Tolerance: **1e-8**
- Random Seed: **42**

The optimizer continuously updates the population until the minimum Mean L1 Distance is obtained.

---

## Step 8: Tracking Convergence

Both optimization algorithms record the objective function value after every evaluation.

The best value obtained so far is stored using

```python
np.minimum.accumulate(history)
```

This information is used to generate convergence plots, showing how quickly each optimization algorithm approaches the optimal solution.

---

## Step 9: Comparing the Generated Curve

After estimating the optimal parameters, the predicted curve is generated again.

The observed dataset and predicted curve are plotted together to visually verify the fitting accuracy.

A close overlap between both curves indicates successful parameter estimation.

---

## Step 10: Performance Comparison

Finally, both optimization algorithms are compared using

- Estimated θ
- Estimated M
- Estimated X
- Mean L1 Distance
- Execution Time

The comparison shows that Differential Evolution achieves a slightly smaller L1 distance while converging more efficiently than Random Search.

---

## Step 11: Final Output

The project generates the following outputs:

- Dataset visualization
- Predicted curve
- Observed vs Predicted comparison
- Random Search convergence plot
- Differential Evolution convergence plot
- Estimated parameter values
- Minimum Mean L1 Distance
- Execution time of each optimization algorithm

These outputs allow both numerical and visual evaluation of the parameter estimation process.

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
