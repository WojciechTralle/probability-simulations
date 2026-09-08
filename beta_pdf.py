"""Visualizing Beta probability density functions in Python."""

import matplotlib.pyplot as plt
from scipy.stats import beta as beta_dist


def plot_beta(alpha, beta):
    """
    Plot the probability density function of a Beta(alpha, beta)
    distribution.
    """

    # The Beta distribution is supported on the interval (0, 1).
    x = [i / 1000 for i in range(1, 1000)]
    y = beta_dist.pdf(x, a=alpha, b=beta)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Beta pdf: α = {alpha}, β = {beta}")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    # Fix beta and vary alpha.
    for alpha in [0.5, 1, 2, 5, 10]:
        plot_beta(alpha, 2)

    # Fix alpha and vary beta.
    for beta in [0.5, 1, 2, 5, 10]:
        plot_beta(2, beta)

    # Symmetric Beta distributions.
    for value in [0.5, 1, 2, 5, 10]:
        plot_beta(value, value)