import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns
path=os.getcwd()
file_path = os.path.join( os.path.dirname(__file__),"../Interview/ABC Company.xlsx")

df=pd.read_excel(file_path ,sheet_name='Sheet1')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum()) #college and Salary column have null values
print(df.duplicated().sum()) #No duplicates
df['Height']=np.random.randint(150,180,size=len(df))
df.to_csv('ABC Company.csv',index=False)
df1=pd.read_csv('ABC Company.csv')
Team_Count=df1.groupby('Team').size()
Percentage=(Team_Count/Team_Count.sum())*100
print("percentage split relative to the total number of employees")
print(Percentage)
print("'ABC Company: Count of employees based on their positions")
print(df1.groupby('Position').size())
#print(df1['Age'].max())
#print(df1['Age'].min())
bins=[15,20,25,30,35,39,45]
labels=['15-20','21-25','26-30','31-35','36-40','41-45']
df1['Age_Group']=pd.cut(df1['Age'],bins=bins,labels=labels)
print("predominant age group among employees")
print(df1['Age_Group'].value_counts())
Team_Position=df1.groupby(['Team','Position'])['Salary'].sum()
print("Team and position have the highest salary expenditure:",Team_Position.idxmax())
print("highest salary expenditure",Team_Position.max())
corr=df1['Age'].corr(df1['Salary'])
print("correlation between age and salary is",corr)











