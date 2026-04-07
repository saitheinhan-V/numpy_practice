from numpy import random

x = random.randint(10)
y = random.rand() # random.rand() generates a random float between 0 and 1
z = random.randint(100,size=(3)) # random.randint(100,size=(3)) generates an array of 3 random integers between 0 and 100
a = random.randint(100,size=(3,4)) # random.randint(100,size=(3,4)) generates a 3x4 array of random integers between 0 and 100

b = random.choice([3, 5, 7, 9]) # random.choice() selects a random element from the given list
c = random.choice(['apple', 'banana', 'cherry']) # random.choice() can also select a random element from a list of strings
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) # random.choice() with probabilities. p=[0.1, 0.3, 0.6, 0.0] means that 3 has a 10% chance, 5 has a 30% chance, 7 has a 60% chance, and 9 has a 0% chance of being selected. size=(3, 5) generates a 3x5 array of random choices based on the given probabilities.
print(x)