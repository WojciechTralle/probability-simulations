"""Visualizing Gamma probability density functions in Python."""

import math

import matplotlib.pyplot as plt
from scipy.stats import gamma


def plot_gamma(alpha, beta):
    """
    Plot the probability density function of a Gamma(alpha, beta)
    distribution, where alpha is the shape parameter and beta is
    the scale parameter.
    """

    # Use the 99.9th percentile as the upper plotting limit.
    max_x = gamma.ppf(0.999, a=alpha, scale=beta)

    x = [max_x * i / 1000 for i in range(1, 1001)]
    y = gamma.pdf(x, a=alpha, scale=beta)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Gamma pdf: α = {alpha}, β = {beta}")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    # Fix beta and vary alpha.
    for alpha in [0.5, 1, 2, 5, 10]:
        plot_gamma(alpha, 1)

    # Fix alpha and vary beta.
    for beta in [0.5, 1, 2, 5]:
        plot_gamma(2, beta)

    # Experiment: keep the mean alpha * beta = 1000 fixed
    # while increasing alpha and decreasing beta.

    alpha = 100000
    beta = 0.01

    mean = alpha * beta
    std = math.sqrt(alpha) * beta

    # plot_gamma(1, 1000)
    # plot_gamma(2, 500)
    # plot_gamma(4, 250)
    # plot_gamma(8, 125)
    # plot_gamma(16, 62.5)
    # plot_gamma(32, 31.25)
    # plot_gamma(64, 15.625)
    # plot_gamma(100, 10)
    # plot_gamma(500, 2)
    # plot_gamma(1000, 1)
    # plot_gamma(2000, 0.5)
    # plot_gamma(10000, 0.1)
    # plot_gamma(100000, 0.01)

    plot_gamma(alpha, beta)

    print("mean =", mean)
    print("standard deviation =", std)