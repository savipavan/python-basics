


# plot

import pandas as pd

path = r"C:\Users\varri\IdeaProjects\python-basics\python_basics_22July_2024\python_advanced_01082024\Day2\iris.csv"

#iris is dataframe
iris = pd.read_csv(path)
# print(type(iris))
#
# print(len(iris))
#
# print(iris.columns)
#
# # datatypes of each cols
# print(iris.dtypes)
# # each row have the id called as index
#
# # row_id is alled as index
print(iris.index)

print(iris.head())

#columns are VIP(column level apis are default) pandas are meant for 2D and in 2D columns are important
#in machine learning columns called as features and rows call it is example of features
# How do we access columns
# way 1:
print(iris.SepalLength)  # Object attr access
print(type['SepalLength'])
print(type(iris[['SepalLength', 'SepalWidth']]))
print(iris.head())

print(iris.loc[0:2, ['SepalLength', 'SepalWidth']])

print(iris.loc[0:2, ['SepalLength', 'SepalWidth']])
print(iris.loc[0:2, :])

#loc - start:end row_id, end row_id is included
#.iloc - start:end index, end index is not included
print(iris.iloc[0:3, [0, 1]])
print(iris.loc[0:3, :])
print(iris.iloc[0:3, :])

## Element wise operation
print(iris.head())
# print(iris['dummy'] = iris.SepalLength + 2* iris.PetalLength - 2)
# print(iris.dummy)

### Creating sum of of the columns is called 'Aggregation'
# IRIS is use for classification

print(iris.Name.unique())

## groupy
## biggested statitis are finding factors if factors are there aggregate the based on factors is right approach

gr = iris.groupby('Name')
print(gr.mean())
print(type(gr))
print(dir(gr))
print(gr.agg({'SepalLength': ['min', 'max', 'mean', 'count']}))
############
import matplotlib.pyplot as plt

iris.iloc[:, 0.4].plot(kind='line')
plt.savefig("p.png")

#DB API
iris.iloc[:,0:4].plot(kind='line')
#https://pandas.pydata.org/docs/user_guide/visualization.html
iris.iloc[:,0.4].plot(kind='line')

#####
#DBAPI - based on sql OR orm
# sql stmt and execute - sql db api
#orm - table is mapped into a class
#oracle/mysql/sql.....
#mysql - 7 libs/modules
# most popular api for database is sqlalchemy
from sqlalchemy import create_engine
#https://docs.sqlalchemy.org/en/14/core/engines.html
# Pandas also connect to database and work
# pandas is more memory as it keeps in memory, other dask , single host lazy DF - Dask, Multi host cluster DF - pySpark
# pandas reads entire data frame and process which keeps your machine low


