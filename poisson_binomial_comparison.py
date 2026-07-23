"""
Solution to Exercise 3.2.7 from Hogg.

Obtain an overlay plot of the pmfs of:

    (a) A Poisson distribution with mean mu = 2.
    (b) A Binomial distribution with n = 100 and p = 0.02.

Explain why these distributions are approximately the same.
"""
from pathlib import Path

import math

import matplotlib.pyplot as plt
from scipy.stats import binom, poisson


def plot_poisson_binomial_overlay(mu, n, p):
    """
    Plot the pmfs of a Poisson(mu) distribution and a Binomial(n, p)
    distribution on the same set of axes.
    """
    poisson_sd = math.sqrt(mu)
    binomial_sd = math.sqrt(n * p * (1 - p))

    # Choose a range containing essentially all of the probability mass
    # of both distributions.
    max_x = int(
        max(
            mu + 5 * poisson_sd,
            n * p + 5 * binomial_sd,
        )
        + 5
    )

    x = range(max_x + 1)

    poisson_probabilities = poisson.pmf(x, mu)
    binomial_probabilities = binom.pmf(x, n, p)

    plt.figure()

    plt.plot(
        x,
        poisson_probabilities,
        marker="o",
        label=f"Poisson: μ = {mu}",
    )

    plt.plot(
        x,
        binomial_probabilities,
        marker="x",
        linestyle="--",
        label=f"Binomial: n = {n}, p = {p}",
    )

    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.title("Poisson and Binomial Probability Mass Functions")
    plt.xticks(list(x))
    plt.grid(True, alpha=0.3)
    plt.legend()

        # Save the figure in the same folder as this Python script.
    output_file = (
        Path(__file__).resolve().parent
        / "poisson_vs_binomial.png"
    )

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
    )

    print(f"Saved to: {output_file}")

    plt.show()


if __name__ == "__main__":
    plot_poisson_binomial_overlay(mu=2, n=100, p=0.02)