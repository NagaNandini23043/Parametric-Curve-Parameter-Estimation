import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("xy_data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

plt.figure(figsize=(8, 6))

plt.scatter(
    x,
    y,
    color="blue",
    s=20,
    label="Given Data Points"
)

plt.plot(
    x,
    y,
    color="red",
    linewidth=1,
    alpha=0.7
)

plt.title("Given Parametric Curve Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

plt.show()
