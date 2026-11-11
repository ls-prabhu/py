import pandas as pd

index=['Sno1','Sno2','Sno3','Sno4']
book_no=pd.Series([210,211,114,178], index=index)
age=pd.Series([21,21,24,23],index=index)
dict1 = {
    'Author_name': pd.Series(['jitender','purinima','arpit','jothi'],index=index),
    'book_no': book_no,
    'age': age,
}

df=pd.DataFrame(dict1,index=index)

print(df)