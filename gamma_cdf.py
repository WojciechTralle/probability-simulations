"""Visualizing Gamma cumulative distribution functions in Python."""

import matplotlib.pyplot as plt
from scipy.stats import gamma


def plot_gamma(alpha, beta):
    """
    Plot the cumulative distribution function of a Gamma(alpha, beta)
    distribution, where alpha is the shape parameter and beta is
    the scale parameter.
    """

    # Use the 99.9th percentile as the upper plotting limit.
    max_x = gamma.ppf(0.999, a=alpha, scale=beta)

    x = [max_x * i / 1000 for i in range(1, 1001)]
    y = gamma.cdf(x, a=alpha, scale=beta)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.title(f"Gamma cdf: α = {alpha}, β = {beta}")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    # Fix beta and vary alpha.
    for alpha in [0.5, 1, 2, 5, 10]:
        plot_gamma(alpha, 1)

    # Fix alpha and vary beta.
    for beta in [0.5, 1, 2, 5]:
        plot_gamma(2, beta)

# Exercise 3.3.12 (Hogg): plot the cdf of Gamma(5,4) and find the median m, i.e.
# find m such that F(m) = P(X <= m) = 0.5
# plot_gamma(5, 4)

# Confirm the median.
# print(gamma.ppf(0.5, a=5, scale=4))



