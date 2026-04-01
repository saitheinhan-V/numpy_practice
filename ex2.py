import numpy as np

a = np.array(40)
b = np.array([1,2,3])
c = np.array([[1,2,3],[4,5,6]])
d = np.array(
    [
        [[1,2,3],
        [4,5,6]],
        [[7,8,9],
         [10,11,12]]
    ]
)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print("no of dimensions: ", arr.ndim)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) #from 2nd dim, last element

arr = np.array([1, 2, 3, 4, 5])
print(arr[0:3]) #from index 0 to 2
print(arr[1:4]) #from index 1 to 3
print(arr[2:]) #from index 2 to end
print(arr[:3]) #from start to index 2
print(arr[:]) #from start to end
print(arr[-3:-2]) #from index -3 to -2

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) #from index 1 to 4, with step 2
print(arr[::3]) #from start to end, with step 3

#slicing 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Slicing 2-D array:::")
print(arr[1, 1:4]) #from index 1 to 3 from the 2nd row
print(arr[0:2, 2]) #from index 0 to 1, from both rows, index 2
print(arr[0:2, 1:4]) #from index 0 to 1, from both rows, index 1 to 3