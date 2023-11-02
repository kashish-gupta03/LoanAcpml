# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

Loan Prediction Model
"""

# importing the dependencies

import numpy as np
import pandas as pd
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#Data collection and processing

from google.colab import drive
drive.mount('/content/drive')

path  = '/content/drive/MyDrive/loan prediction model ml/loan prediction dataset.csv.csv'

# loading the dataset to pandas dataframe 
loan_dataset = pd.read_csv(path)

type(loan_dataset)

# printing the first 5 rows of the dataframe 
loan_dataset.head()

loan_dataset.shape

# statistical measures
loan_dataset.describe()

# number of missing values in each column 
loan_dataset.isnull().sum()

# dropping the misses values 
loan_dataset = loan_dataset.dropna()

loan_dataset.isnull().sum()

# label encoding 
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}}, inplace=True)

loan_dataset.head()

# Dependent column values 
loan_dataset['Dependents'].value_counts()

# replacing the value of 3+ to 4 
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)

# dependent values 
loan_dataset['Dependents'].value_counts()

"""Data Visualization """

# educational and loan status 
 sns.countplot(x='Education' , hue='Loan_Status', data=loan_dataset)

# marital status and loan status
sns.countplot(x='Married' , hue='Loan_Status' , data=loan_dataset)

# convert categorical columns to numerical values 
loan_dataset.replace({'Married':{'No':0, 'Yes':1} , 'Gender':{'Male':1, 'Female':0} , 'Self_Employed':{'No':0,'Yes':1}}, inplace=True)

loan_dataset.replace( {'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2}, 'Education':{'Graduate':1,'Not Graduate':0 }}, inplace=True)

loan_dataset.replace({'Marries':{'No':0, 'Yes':1}}, inplace=True)
loan_dataset.head()

# separating the data and label 
X = loan_dataset.drop(columns=['Loan_ID' , 'Loan_Status'], axis=1)
Y = loan_dataset['Loan_Status']

print(X)
print(Y)

X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

print(X.shape ,X_train.shape, X_test.shape)

"""Trainig the model :

Support Vector Machine Model 
"""

classifier = svm.SVC(kernel = 'linear')

# trainig the support vector machine model 
classifier.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)

print('Accuracy on trainig the data :' , training_data_accuray)

# accuracy score on training data
X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data:' , test_data_accuray)
