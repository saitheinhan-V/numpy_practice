#binomial distribution
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# n - number of trials.

# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).

# size - The shape of the returned array.

x = random.binomial(n=5, p=0.5, size=10)

print(x)

sns.displot(random.binomial(n=10, p=0.5, size=100)) # sns.displot() creates a histogram of the data
plt.show()