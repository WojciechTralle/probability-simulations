# Probability Simulations

Python simulations and visualizations inspired by probability theory and mathematical statistics.

This repository contains numerical experiments, probability distributions, and statistical simulations implemented in Python. Many of the examples are motivated by exercises and concepts from Hogg, McKean, and Craig's *Introduction to Mathematical Statistics*.

## Current Contents

### Distributions

* Binomial distribution (`binomial.py`)

### Planned Additions

#### Distributions

* Poisson distribution
* Geometric distribution
* Negative binomial distribution
* Multinomial distribution

#### Simulations

* Law of Large Numbers
* Central Limit Theorem
* Monte Carlo estimation of π
* Random walks
* Markov chains

#### Statistical Methods

* Confidence intervals
* Bootstrap methods
* Maximum likelihood estimation
* Bayesian inference

## Requirements

* Python 3.x
* matplotlib

Install the required packages with

```bash
pip install matplotlib
```

## Example

```python
from binomial import plot_binom

plot_binom(15, 0.2)
```

## Motivation

This repository documents my transition from pure mathematics to computational probability and statistics. The goal is to explore probabilistic ideas through programming while developing practical Python skills.

## Author

**Wojciech Tralle**

* Ph.D. in Mathematics, University of Virginia
* Interests: probability, statistics, number theory, algebraic geometry, and scientific computing

---

Work in progress — new simulations and visualizations will be added over time.
