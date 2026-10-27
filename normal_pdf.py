"""Visualizing normal probability density functions in Python."""

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


# Examples

# mu = 0
# sigma = 1

# P(X <= x)
# print(norm.cdf(1, loc=mu, scale=sigma))

# P(X >= x)
# print(norm.sf(1, loc=mu, scale=sigma))

# P(a <= X <= b)
# print(norm.cdf(1, loc=mu, scale=sigma)
#       - norm.cdf(-1, loc=mu, scale=sigma))

# Probability density at x
# print(norm.pdf(0, loc=mu, scale=sigma))


def plot_normal(mu, sigma):
    """Plot the probability density function of a N(mu, sigma^2) distribution."""

    # Choose a plotting range containing essentially
    # all of the probability mass.
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

    # Calculate the probability density function.
    y = norm.pdf(x, loc=mu, scale=sigma)

    # Plot the pdf.
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, linewidth=2)

    # Mark the mean and the inflection points.
    plt.axvline(mu, color="gray", linestyle="--", label="Mean")
    plt.axvline(mu - sigma, color="red", linestyle=":",
                label="Inflection points")
    plt.axvline(mu + sigma, color="red", linestyle=":")

    plt.title(f"Normal pdf: mu = {mu}, sigma = {sigma}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


# Examples

plot_normal(0, 1)
plot_normal(2, 1)
plot_normal(0, 2)