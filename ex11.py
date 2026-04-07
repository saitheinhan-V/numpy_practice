import numpy as np
from numpy import random

x = np.array([1, 2, 3, 4, 5])
#shuffling the array x using random.shuffle() will modify the original array
y = random.shuffle(x) # random.shuffle() shuffles the elements of the array in place
print(x)

#permutation does not shuffle the original array, it returns a new array with the elements shuffled
z = random.permutation(x) # random.permutation() returns a new array with the elements shuffled
print(z)