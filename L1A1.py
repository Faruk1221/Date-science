import numpy as np

#How to Create an Array in Numpy - Array Operation
#Array : Collection of Data

arr = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

#Arithmatic Operation
print(arr+arr2)
print(arr-arr2)
print(arr*arr2)
print(arr/arr2)

#Universal Operation
print(np.sin(arr))
print(np.cos(arr))
print(np.sqrt(arr2))

print(np.mean(arr))
print(np.min(arr2))
print(np.max(arr2))
