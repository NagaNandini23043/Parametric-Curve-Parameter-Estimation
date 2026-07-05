import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("xy_data.csv")

actual_x = data.iloc[:, 0].values
actual_y = data.iloc[:, 1].values

n = len(actual_x)

t = np.linspace(6, 60, n)


theta_deg = 30
M = 0.03
X = 55

theta = np.deg2rad(theta_deg)


pred_x = (
    t * np.cos(theta)
    - np.exp(M * np.abs(t))
    * np.sin(0.3 * t)
    * np.sin(theta)
    + X
)

pred_y = (
    42
    + t * np.sin(theta)
    + np.exp(M * np.abs(t))
    * np.sin(0.3 * t)
    * np.cos(theta)
)

l1_distance = np.mean(
    np.abs(actual_x - pred_x)
    + np.abs(actual_y - pred_y)
)

print("=" * 50)
print("Known Parameters")
print("=" * 50)
print(f"Theta : {theta_deg}")
print(f"M     : {M}")
print(f"X     : {X}")
print(f"\nMean L1 Distance : {l1_distance:.10f}")


plt.figure(figsize=(8,6))

plt.scatter(
    actual_x,
    actual_y,
    color="blue",
    s=18,
    label="Observed Points"
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
plt.title("Observed vs Predicted Curve")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()
