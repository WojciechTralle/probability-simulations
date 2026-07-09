# Visualizing Poisson probability mass functions in Python.
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math



# Examples
# mu = 2
# P(X = k)
# print(poisson.pmf(0, mu))

# P(X <= k)
# print(poisson.cdf(0, mu))

# P(X >= 1)
# print(1 - poisson.cdf(0, mu))





def plot_poisson(mu):
    """Plot the probability mass function of a Poisson(mu) distribution with mean mu."""
    # Choose a plotting range that contains essentially all of the probability mass.
    max_x = int(mu + 5 * math.sqrt(mu) + 10)

    x = range(max_x + 1)
    y = poisson.pmf(x, mu)

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.title(f"Poisson pmf: μ = {mu}")
    plt.grid(True, alpha=0.3)
    plt.show()
    
if __name__ == "__main__":
    for mu in [1, 2, 5, 10, 20, 50, 100]:
        plot_poisson(mu)
        
        
