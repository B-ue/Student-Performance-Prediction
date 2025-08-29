from h11 import Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

Data_path = r'C:\Users\soluw\Desktop\VSCode\datasets\Intern_student_performance.csv'
#load data
data = pd.read_csv(Data_path)
print(data.head())
#describe data
print(data.describe())
#shape of data
print(data.shape)
#check for null values
print(data.isnull().sum())
#check the data types of the columns
print(data.dtypes)
#check for duplicate values
print(data.duplicated().sum())
#drop duplicate values
data = data.drop_duplicates()
print(data.duplicated().sum())
#check the shape of the data after dropping duplicates
print(data.shape)
# change the data type of the column "Shool" to integer
new_data = data['school'] = data['school'].map({'GP': 0, 'MS': 1})
print(new_data)
# #change the data type of the column "Gender" to integer
new_change_data = data['sex'] = data['sex'].map({'F': 0, 'M': 1})
print(new_change_data)

#check for relationship between columns
G3_and_sex = data.groupby(['G3', 'sex']).mean()
print(G3_and_sex)
#visualize the relationship between columns
# sns.barplot(x='G3', y='sex', data=data)
# plt.show()
#use boxplot to check relationship between G3 and sex
box =  data.boxplot(column='G3', by='sex',grid=False)
plt.show()
# #use boxplot to check relationship between G3 and studytime

# #check for unique values in each column
# for column in data.columns:
#     print(f'{column}: {data[column].nunique()}')
# #create histogram for each column
# hist1 = data.hist(figsize=(20,20))
# plt.show()
# print(hist1)    
#check for correlation between columns
correlation = data.corr()
print(correlation)
