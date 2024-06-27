import numpy as np
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2D array
arr = np.array([[1, 2], [3, 4]])
print(arr)
#basic array operations
arr = np.array([1, 2, 3, 4, 5])

# Get the shape of the array
print(arr.shape)

# Get the data type of the array
print(arr.dtype)

# Get the number of elements in the array
print(arr.size)

# Get the first element of the array
print(arr[0])

# Get the last element of the array
print(arr[-1])
#Array indexing and slicing
arr = np.array([1, 2, 3, 4, 5])

# Get the second element of the array
print(arr[1])

# Get the elements from index 1 to 3
print(arr[1:3])

# Get the elements from index 1 to the end
print(arr[1:])

# Get the elements from the start to index 3
print(arr[:3])

#Basic mathematical operations
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Add two arrays element-wise
print(arr1 + arr2)

# Subtract two arrays element-wise
print(arr1 - arr2)

# Multiply two arrays element-wise
print(arr1 * arr2)

# Divide two arrays element-wise
print(arr1 / arr2)

#Array Reshaping
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array to 2D
arr = arr.reshape(2, 3)
print(arr)

# Reshape the array to 3D
arr = arr.reshape(2, 1, 3)
print(arr)

#Array Flattening
arr = np.array([[1, 2], [3, 4]])

# Flatten the array
arr = arr.flatten()
print(arr)

#Array Transpose
arr = np.array([[1, 2], [3, 4]])

# Transpose the array
arr = arr.T
print(arr)

#Array creation with 'arange' and 'linspace'
# Create an array with 5 elements from 0 to 10
arr = np.arange(0, 10, 2)
print(arr)

# Create an array with 5 elements from 0 to 10, spaced evenly
arr = np.linspace(0, 10, 5)
print(arr)

#Array Creation with zeros, ones, and full
# Create an array with 3x4 elements, all zeros
arr = np.zeros((3, 4))
print(arr)

# Create an array with 3x4 elements, all ones
arr = np.ones((3, 4))
print(arr)

# Create an array with 3x4 elements, all filled with 5
arr = np.full((3, 4), 5)
print(arr)

#Array Indexing with Boolean Arrays
arr = np.array([1, 2, 3, 4, 5])

# Create a boolean array
bool_arr = arr > 3

# Use the boolean array to index into the original array
print(arr[bool_arr])

#Array Manipulation with sort, argsort, and argmax
arr = np.array([5, 2, 8, 3, 1, 4])

# Sort the array in ascending order
arr.sort()
print(arr)

# Get the indices of the sorted array
indices = np.argsort(arr)
print(indices)

# Get the index of the maximum element
max_index = np.argmax(arr)
print(max_index)

#Array Manipulation with min, max, and mean'
arr = np.array([1, 2, 3, 4, 5])

# Get the minimum element
print(np.min(arr))

# Get the maximum element
print(np.max(arr))

# Get the mean of the array
print(np.mean(arr))

#Array Manipulation with std, var, and median
arr = np.array([1, 2, 3, 4, 5])

# Get the standard deviation of the array
print(np.std(arr))

# Get the variance of the array
print(np.var(arr))

# Get the median of the array
print(np.median(arr))

# Array Manipulation with concatenate and stack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate two arrays horizontally
arr = np.concatenate((arr1, arr2))
print(arr)

# Concatenate two arrays vertically
arr = np.stack((arr1, arr2))
print(arr)

# Array Manipulation with split and vsplit
arr = np.array([1, 2, 3, 4, 5, 6])

# Split the array into two parts
arr1, arr2 = np.split(arr, 2)
print(arr1)
print(arr2)

# Split the array into two parts vertically
arr1, arr2 = np.vsplit(arr.reshape(2, 3), 2)
print(arr1)
print(arr2)

#Matrix Operations with matmul and dot
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication using matmul
result = np.matmul(arr1, arr2)
print(result)

# Matrix multiplication using dot
result = np.dot(arr1, arr2)
print(result)

#Matrix Operations with inv and det
arr = np.array([[1, 2], [3, 4]])

# Calculate the inverse of the matrix
inv_arr = np.linalg.inv(arr)
print(inv_arr)

# Calculate the determinant of the matrix
det = np.linalg.det(arr)
print(det)