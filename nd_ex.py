import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

#normal distribution
# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

# x = random.normal(loc=1.0, scale=2, size=(2,3)) 
# print(x)

y = random.normal(loc=2,scale=(10),size=(2,3))
print(y)
sns.displot(y, kind="kde")
plt.show()