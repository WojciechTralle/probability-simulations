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

![Poisson vs Binomial](../images/poisson_vs_binomial.png)

The two distributions also have almost identical variances:

- Var(Binomial) = np(1-p) = 1.96,
- Var(Poisson) = λ = 2.

Consequently, the overlay plot shows that the pmfs nearly coincide.
