import pandas as pd

d = {'one':pd.Series([1,2,3,],index=['a','b','c']),
     'two':pd.Series([1,2,3],index=['a','b','c'])}

df = pd.DataFrame(d)
print(df)

print("adding new column to existing dataframe")

df['three'] = pd.Series([10,20,30],index=['a','b','c'])
print(df)

print("adding new row to existing dataframe")
df['four'] = df['one'] + df['three']

print(df)

print("deleting column from existing dataframe")
del df['one']
print(df)