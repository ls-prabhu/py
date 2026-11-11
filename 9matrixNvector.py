import numpy as np

x = np.array([1,4,0],float)
y = np.array([2,2,1],float)

print("matrices and vectors")

print("x : ",x)
print("y : ",y)

print("dot product of x and y : ",np.dot(x,y))

print("inner product of x and y : ",np.inner(x,y))

print("outter product of x and y : \n",np.outer(x,y))
      
print("cross product of x and y : ",np.cross(x,y))

matrix = np.array([[1,2],[4,5]])
print("matrix : \n",matrix)

power = np.linalg.matrix_power(matrix,3)
print("matrix to the power of 3 : \n",power)