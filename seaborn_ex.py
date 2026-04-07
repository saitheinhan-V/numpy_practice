#seaborn
#seaborn is a powerful data visualization library in Python that is built on top of Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics. Seaborn is particularly useful for visualizing complex datasets and making it easier to understand the relationships between variables.
#pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
import numpy as np

choice_arr = random.randint(1,100,size=(5))
# choice_arr = random.choice(random_arr,p=[0.1,0.3,0.5,0.1,0.0],size=(5)) # generates an array of 100 random integers between 1 and 100
sns.histplot(choice_arr, kde=True) # sns.histplot() creates a histogram of the data

# sns.displot(choice_arr, kind="kde")
print(choice_arr)
plt.show()

