# Module1-End-Project
Preprocessing the dataset, analyzing the data, and presenting findings graphically.
			Module1: End Project

Preprocessing: 
● Correct the data in the "height" column by replacing it with random numbers between 150 and 180. Ensure data consistency and integrity before proceeding with analysis. (1 mark)

import numpy as np
import pandas as pd
df=pd.read_excel(r"C:\Users\nkanhirathin\PycharmProjects\sample1\Interview\ABC Company.xlsx",sheet_name='Sheet1')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum()) #college and Salary column have null values
print(df.duplicated().sum()) #No duplicates df['Height']=np.random.randint(150,180,size=len(df))


Analysis Tasks: 
● Determine the distribution of employees across each team and calculate the percentage split relative to the total number of employees. (2 marks) 

Team_Count=df1.groupby('Team').size()
Percentage=(Team_Count/Team_Count.sum())*100
Team_Count.index=Team_Count.index.str.replace(' ','').str[:3]
#print(Team_Count)
plt.figure(figsize=(10,5))
sns.barplot(x=Team_Count.index,y=Team_Count.values)
plt.show()
 



**Here we can use the count plot as well using df1[Team] as x value.
The majority of teams consist of 15 members. However, the Meme and New have a higher number of teammates compared to the other teams.**




● Segregate employees based on their positions within the company. (2 marks) 

print(df1.groupby('Position').size())
plt.title('ABC Company: Count of employees based on their positions')
sns.countplot(x=df1['Position'],order=df1['Position'].value_counts().index)
plt.show()
 

**SG has the highest employee count, while PF has the second-highest number of employees.**



● Identify the predominant age group among employees. (2 marks) 

print(df1['Age'].max())
print(df1['Age'].min())
bins=[15,20,25,30,35,39,45]
labels=['15-20','21-25','26-30','31-35','36-40','41-45']
df1['Age_Group']=pd.cut(df1['Age'],bins=bins,labels=labels)
#print(df1['Age_Group'])
print(df1['Age_Group'].value_counts())
sns.histplot(df1['Age_Group'])
plt.show()



 

**The 21–25 age group has the highest number of employees, indicating that they are the most active worplace. The 26–30 age group is also actively working. In comparison, the 15–20 and above 40 age groups have fewer employees and are less represented in the workplace.**


● Discover which team and position have the highest salary expenditure. (2 marks)

df1=pd.read_csv('ABC Company.csv')
Team_Position=df1.groupby(['Team','Position'])['Salary'].sum()
print(Team_Position.idxmax())
print(Team_Position.max())

**('Los Angeles Lakers', 'SF')  Is having highest salary expenditure of 31866445.0**


Top5=Team_Position.sort_values('Salary',ascending=False).head(5)
print(Top5)
plt.figure(figsize=(8,6))
plt.xlabel('Team_Position')
plt.ylabel('Salary')
plt.title('Top 5 Salaries by Team')
sns.barplot(x='Team',y='Salary',hue='Position',data=Top5)
plt.show()


 


****SF position in the Los Angeles Lakers has the highest total salary expenditure among all team position .PF under Miami groups comes second
SF position under Denver Nuggets   Team is having 5th position, indicating that it is the most expensive position.
.
SF position under Denver Nuggets   Team is having 5th position..SF position is having most expense****



 ● Investigate if there's any correlation between age and salary, and represent it visually. (2 marks)


corr=df1['Age'].corr(df1['Salary'])
print(corr)
plt.title('Salary vs Age')
plt.xlabel('Age')
plt.ylabel('Salary')
sns.scatterplot(x=df1['Age'],y=df1['Salary'])
plt.show()

**Corr value is 0.2140094122657097 showing weak +ve correlation between nage and salary**
 
