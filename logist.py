# loc - mean, where the peak is. Default 0.

# scale - standard deviation, the flatness of distribution. Default 1.

# size - The shape of the returned array.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot(random.logistic(size=1000), kind="kde") 
# plt.show()

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}

sns.displot(data, kind="kde")

plt.show()