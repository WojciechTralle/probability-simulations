<<<<<<< HEAD
"""
Solution to Exercise 3.2.7 from Hogg.

Obtain an overlay plot of the pmfs of:

    (a) A Poisson distribution with mean mu = 2.
    (b) A Binomial distribution with n = 100 and p = 0.02.

Explain why these distributions are approximately the same.
"""

from scipy.stats import poisson, binom
import matplotlib.pyplot as plt
import math


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
            n * p + 5 * binomial_sd
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
        label=f"Poisson: μ = {mu}"
    )

    plt.plot(
        x,
        binomial_probabilities,
        marker="x",
        linestyle="--",
        label=f"Binomial: n = {n}, p = {p}"
    )

    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.title("Poisson and Binomial Probability Mass Functions")
    plt.xticks(list(x))
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_poisson_binomial_overlay(mu=2, n=100, p=0.02)
    
#plt.savefig("images/poisson_vs_binomial.png", dpi=300, bbox_inches="tight")    

    
    
=======
# Poisson Approximation to the Binomial Distribution

This program overlays the probability mass functions of

- Poisson(2),
- Binomial(100, 0.02).

## Why are they nearly identical?

The Poisson distribution is an approximation to the Binomial distribution
when

- the number of trials n is large,
- the probability of success p is small,
- the product np remains fixed.

Here

n = 100,
p = 0.02,

so

np = 2.

Therefore,

Binomial(100, 0.02) ≈ Poisson(2).

The two distributions also have almost identical variances:

- Var(Binomial) = np(1-p) = 1.96,
- Var(Poisson) = λ = 2.

Consequently, the overlay plot shows that the pmfs nearly coincide.
>>>>>>> 978ced7b4bd3cdbda3d0718bb40027db638cb559
