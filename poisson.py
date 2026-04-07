from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# lam - rate or known number of occurrences e.g. 2 for above problem.

# size - The shape of the returned array.

sns.displot(random.poisson(lam=2, size=1000))

plt.show()