import numpy as np

a = np.array([1,20,5,22,8,15])
b = np.array([12,9,3,42,6,33])
print(f"{'array a':-^40}")
print(a)
print(f"{'array b':-^40}")
print(b)

print(f"{'minimum array':-^40}")
print(np.minimum(a,b))

print(f"{'maximum array':-^40}")
print(np.maximum(a,b))

print(f"{'sum of array a':-^40}")
print(np.sum(a))

print(f"{'sum of array b':-^40}")
print(np.sum(b))

def cumsum(s):
    sm=0
    cum_list=[]
    for i in s:
        sm+=i
        cum_list.append(sm)
    return cum_list

print(f"{'cumulative sum of array a':-^40}")
print(cumsum(a))
print(f"{'cumulative sum of array b':-^40}")
print(cumsum(b))