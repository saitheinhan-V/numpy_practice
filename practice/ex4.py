import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
#view affected by changes in original array, but copy is not affected by changes in original array
x = arr.view()
arr[0] = 42
print(arr)
print(x)

x[0] = 31
print(arr)
print(x)