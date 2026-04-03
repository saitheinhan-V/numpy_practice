import numpy as np
arr = np.array([1, 2, 3, 4, 5,6,7])

x = np.array_split(arr,3)
# print(x[0])
# print(x[1])
# print(x[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1) #split the array into 3 parts along the columns (axis=1)
newarr1 = np.array_split(arr, 3, axis=0) #split the array into 3 parts along the rows (axis=0)

# print(newarr)
print(newarr1)