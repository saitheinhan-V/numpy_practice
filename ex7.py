import numpy as np

arr = np.array([1, 2, 3, 4, 5])

s = np.where(arr %2 == 0)
print(s)

arr = np.array([6, 7, 8, 9])

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x) #prints 1 because 7 is at index 1 in the array

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)