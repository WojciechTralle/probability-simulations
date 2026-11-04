
"""Visualizing contaminated normal distributions in Python."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def contaminated_normal_pdf(x, epsilon, sigma_c):
    """
    Calculate the pdf of a contaminated normal distribution.

    epsilon: contamination probability
    sigma_c: standard deviation of the contaminating normal
    """
    return (
        (1 - epsilon) * norm.pdf(x)
        + epsilon * norm.pdf(x, scale=sigma_c)
    )


def contaminated_normal_cdf(x, epsilon, sigma_c):
    """Calculate the cdf of a contaminated normal distribution."""
    return (
        (1 - epsilon) * norm.cdf(x)
        + epsilon * norm.cdf(x, scale=sigma_c)
    )


def plot_contaminated_normal(epsilon, sigma_c):
    """
    Plot the pdf of a contaminated normal distribution
    alongside the standard normal pdf.
    """

    # Choose a range containing essentially all
    # of the probability mass.
    max_x = 4 * max(1, sigma_c)
    x = np.linspace(-max_x, max_x, 1000)

    # Calculate the probability density functions.
    y = contaminated_normal_pdf(x, epsilon, sigma_c)
    y_standard = norm.pdf(x)

    plt.figure(figsize=(8, 5))

    plt.plot(
        x, y,
        label="Contaminated normal",
        linewidth=2
    )

    plt.plot(
        x, y_standard,
        linestyle="--",
        label="Standard normal"
    )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(
        f"Contaminated normal pdf: "
        f"epsilon = {epsilon}, sigma_c = {sigma_c}"
    )
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def outlier_probability(epsilon, sigma_c, threshold=2):
    """Calculate P(|W| >= threshold)."""
    return (
        contaminated_normal_cdf(-threshold, epsilon, sigma_c)
        + 1 - contaminated_normal_cdf(
            threshold, epsilon, sigma_c
        )
    )


if __name__ == "__main__":

    # Fix sigma_c and vary epsilon.
    for epsilon in [0.01, 0.05, 0.10, 0.20]:
        plot_contaminated_normal(epsilon, 3)

    # Fix epsilon and vary sigma_c.
    for sigma_c in [1.5, 2, 3, 5]:
        plot_contaminated_normal(0.05, sigma_c)

    # Example: calculate probabilities.
    epsilon = 0.05
    sigma_c = 3

    # P(W <= 2)
    print(
        "P(W <= 2) =",
        contaminated_normal_cdf(2, epsilon, sigma_c)
    )

    # P(|W| >= 2)
    print(
        "P(|W| >= 2) =",
        outlier_probability(epsilon, sigma_c)
    )

    # Compare with the standard normal distribution.
    print(
        "Standard normal P(|Z| >= 2) =",
        2 * norm.sf(2)
    )
