import numpy as np

list1 = [1.1, 2.2, 3.3]
print(type(list1),end=" :")
print( list1)

print()
# Convert list to numpy array
arr1 = np.array(list1)
print(type(arr1),end=" :")
print(arr1)

print()

tuple1 = (1.1, 2.2, 3.3)
print(type(tuple1),end=" :")
print(tuple1)

array2 = np.array(tuple1)
print(type(array2),end=" :")
print(array2)

print()

array3 = np.array([tuple1,list1,array2])
print(type(array3),end=" :")
print(array3)