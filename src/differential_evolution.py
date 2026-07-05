import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
import time

data = pd.read_csv("xy_data.csv")

actual_x = data.iloc[:, 0].values
actual_y = data.iloc[:, 1].values

n = len(actual_x)

t = np.linspace(6, 60, n)

def generate_curve(theta_deg, M, X):

    theta = np.deg2rad(theta_deg)

    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.cos(theta)
    )

    return x, y

history = []

def objective(params):

    theta, M, X = params

    pred_x, pred_y = generate_curve(theta, M, X)

    loss = np.mean(
        np.abs(actual_x - pred_x)
        + np.abs(actual_y - pred_y)
    )

    history.append(loss)

    return loss

bounds = [

    (0, 50),     

    (-0.05, 0.05),   

    (0, 100)        

]

start = time.time()

result = differential_evolution(

    objective,

    bounds,

    strategy="best1bin",

    maxiter=500,

    popsize=20,

    mutation=(0.5,1),

    recombination=0.7,

    tol=1e-8,

    polish=True,

    seed=42

)

elapsed = time.time() - start

best_theta, best_M, best_X = result.x

print("\n========= DIFFERENTIAL EVOLUTION =========\n")

print(f"Theta : {best_theta:.6f}")

print(f"M     : {best_M:.6f}")

print(f"X     : {best_X:.6f}")

print(f"\nBest L1 Distance : {result.fun:.8f}")

print(f"Execution Time : {elapsed:.4f} seconds")

pred_x, pred_y = generate_curve(
    best_theta,
    best_M,
    best_X
)

plt.figure(figsize=(8,6))

plt.scatter(
    actual_x,
    actual_y,
    color="blue",
    s=20,
    label="Observed Data"
)

plt.plot(
    pred_x,
    pred_y,
    color="red",
    linewidth=2,
    label="Predicted Curve"
)

plt.xlabel("X")

plt.ylabel("Y")

plt.title("Differential Evolution Parameter Estimation")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()

best_history = np.minimum.accumulate(history)

plt.figure(figsize=(8,5))

plt.plot(best_history)

plt.xlabel("Function Evaluations")

plt.ylabel("Best L1 Distance")

plt.title("Differential Evolution Convergence")

plt.grid(True)

plt.tight_layout()

plt.show()
