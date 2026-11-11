import pandas as pd
import openpyxl

df1 = pd.read_csv("student.csv")
print("dataframe from csv file")
print(df1)

df2 = pd.read_excel("student.xlsx")
print("dataframe from excel file")
print(df2)