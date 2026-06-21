# Exercise 3.1.8 from Hogg's Introduction to Mathematical Statistics.
# Visualizing binomial probability mass functions in Python.

import math
import matplotlib.pyplot as plt


def plot_binom(n, p):
    """Plot the probability mass function of a Binomial(n, p) distribution."""
    x = list(range(n + 1))
    y = [math.comb(n, k) * p**k * (1 - p)**(n - k) for k in x]

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.title(f"Binomial pmf: n = {n}, p = {p}")
    plt.show()


if __name__ == "__main__":
    # Part (a)
    plot_binom(15, 0.2)

    # Part (b)
    p_values = [0, 0.01] + [i / 10 for i in range(1, 10)] + [1]

    for p in p_values:
        plot_binom(15, p)

    # Part (c)
    for n in [12, 20, 50, 200, 300]:
        plot_binom(n, 0.05)