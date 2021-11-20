# -*- coding: utf-8 -*-
"""M200722CA_SOURAV_DECISIONTREE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mk1Qkzb1Nu9ZnU_vRKFcFD6o7Qj10xaz
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import seaborn as sns
import sklearn.datasets as datasets
# %matplotlib inline

# Commented out IPython magic to ensure Python compatibility.
import matplotlib
# %matplotlib inline
from google.colab import files
uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name = fn,length = len(uploaded[fn])))

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('iris.data')
df.head()

# to display stats about data
df.describe()

# to basic info about datatype
df.info()

# to display no. of samples on each class
df['classlabel\t'].value_counts()

# check for null values
df.isnull().sum()

# histograms
df['sepallength'].hist()

df['sepalwidth'].hist()

df['petallength'].hist()

df['petalwidth'].hist()

# scatterplot
colors = ['red', 'orange', 'blue']
species = ['Iris-virginica','Iris-versicolor','Iris-setosa']

for i in range(3):
    x = df[df['classlabel\t'] == species[i]]
    plt.scatter(x['sepallength'], x['sepalwidth'], c = colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()

for i in range(3):
    x = df[df['classlabel\t'] == species[i]]
    plt.scatter(x['petallength'], x['petalwidth'], c = colors[i], label=species[i])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()

for i in range(3):
    x = df[df['classlabel\t'] == species[i]]
    plt.scatter(x['sepallength'], x['petallength'], c = colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()

for i in range(3):
    x = df[df['classlabel\t'] == species[i]]
    plt.scatter(x['sepalwidth'], x['petalwidth'], c = colors[i], label=species[i])
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.legend()

#Coorelation Matrix
corr = df.corr()
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax, cmap = 'coolwarm')

#Label Encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['classlabel\t'] = le.fit_transform(df['classlabel\t'])
df.head()

#Model Training

from sklearn.model_selection import train_test_split
# train - 70
# test - 30
X = df.drop(columns=['classlabel\t'])
Y = df['classlabel\t']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

# logistic regression 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# model training
model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# knn - k-nearest neighbours
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

# decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

model.fit(x_train, y_train)

# print metric to get performance
print("Accuracy: ",model.score(x_test, y_test) * 100)

