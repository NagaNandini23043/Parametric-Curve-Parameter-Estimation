import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(csv_path):
    data = pd.read_csv(csv_path)

    x_actual = data.iloc[:, 0].values
    y_actual = data.iloc[:, 1].values

    return x_actual, y_actual


def generate_curve(theta_deg, M, X, t):

    theta = np.deg2rad(theta_deg)

    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y


def l1_distance(actual_x, actual_y, pred_x, pred_y):

    return np.mean(np.abs(actual_x - pred_x) + np.abs(actual_y - pred_y))


def random_search(
        actual_x,
        actual_y,
        iterations=10000,
        random_seed=42
):

    np.random.seed(random_seed)

    n = len(actual_x)

    t = np.linspace(6, 60, n)

    best_loss = np.inf
    best_params = None

    history = []

    for i in range(iterations):

        theta = np.random.uniform(0, 50)
        M = np.random.uniform(-0.05, 0.05)
        X = np.random.uniform(0, 100)

        pred_x, pred_y = generate_curve(theta, M, X, t)

        loss = l1_distance(actual_x, actual_y, pred_x, pred_y)

        history.append(loss)

        if loss < best_loss:

            best_loss = loss
            best_params = (theta, M, X)

    return best_params, best_loss, history


def plot_curve(actual_x, actual_y, theta, M, X):

    t = np.linspace(6, 60, len(actual_x))

    pred_x, pred_y = generate_curve(theta, M, X, t)

    plt.figure(figsize=(8,6))

    plt.scatter(
        actual_x,
        actual_y,
        color="blue",
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
    plt.title("Random Search Curve Fitting")

    plt.legend()
    plt.grid(True)

    plt.show()

def plot_convergence(history):

    best = np.minimum.accumulate(history)

    plt.figure(figsize=(8,5))

    plt.plot(best)

    plt.xlabel("Iterations")
    plt.ylabel("Best L1 Distance")
    plt.title("Random Search Convergence")

    plt.grid(True)

    plt.show()

if __name__ == "__main__":

    x_actual, y_actual = load_data("xy_data.csv")

    params, loss, history = random_search(
        x_actual,
        y_actual,
        iterations=10000
    )

    theta, M, X = params

    print("\n========= RANDOM SEARCH =========")

    print(f"Theta : {theta:.6f}")
    print(f"M     : {M:.6f}")
    print(f"X     : {X:.6f}")

    print(f"L1 Distance : {loss:.6f}")

    plot_curve(
        x_actual,
        y_actual,
        theta,
        M,
        X
    )

    plot_convergence(history)
