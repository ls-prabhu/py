import numpy as np

arr = np.array([10,5,20,5,30,10,40])
print("array : ",arr)

print("sorted array : ",np.sort(arr))

print("positon of 10:",np.where(arr==10)[0])

print("count of 5 in array : ",np.count_nonzero(arr==5))

print("total number of elements in array : ",arr.size)