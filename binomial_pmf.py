"""Visualizing the binomial probability mass function in Python."""

import math
import matplotlib.pyplot as plt


def plot_binomial(n, p):
    """Plot the probability mass function of a Binomial(n, p) distribution."""
    x = list(range(n + 1))
    y = [
        math.comb(n, k) * p**k * (1 - p)**(n - k)
        for k in x
    ]

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.title(f"Binomial distribution: n = {n}, p = {p}")
    plt.grid(alpha=0.3)
    plt.show()


if __name__ == "__main__":
    plot_binomial(n=15, p=0.2)

    # Experiments

    # Fix n and vary p.
    plot_binomial(n=20, p=0.1)
    plot_binomial(n=20, p=0.3)
    plot_binomial(n=20, p=0.5)
    plot_binomial(n=20, p=0.7)
    plot_binomial(n=20, p=0.9)

    # Fix p and vary n.
    plot_binomial(n=10, p=0.2)
    plot_binomial(n=50, p=0.2)
    plot_binomial(n=200, p=0.2)

    # Keep the mean np = 40 fixed.
    plot_binomial(n=100, p=0.4)
    plot_binomial(n=200, p=0.2)
    plot_binomial(n=400, p=0.1)