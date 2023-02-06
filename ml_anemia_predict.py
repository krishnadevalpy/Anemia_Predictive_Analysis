# -*- coding: utf-8 -*-
"""ML_anemia_predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XxA7z8xgzIrgzrXYPscHkYm0PIWX0ttU

# Imports Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("anemia.csv")

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

data.head()

"""# Analysis"""

data.isnull().sum()

new_data = data.drop(["Result","Gender"],axis = 1)
new_data.head()

new_data.describe() #description of the data in the Dataset

"""Visualize"""

import seaborn as sns

plt.figure(figsize=(10,5))
sns.histplot(data= data, x="Hemoglobin", hue="Result", multiple="stack")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(data=data, x="MCH", hue="Result", multiple="stack")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(data=data, x="MCHC", hue="Result", multiple="stack")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(data=data, x="MCV", hue="Result", multiple="stack")
plt.show()

plt.figure(figsize=(5,10))
plot =sns.countplot('Gender',hue='Result',data = data)
plot.set_title("Gender : Anemia Count")
plt.show()

Dataset = data.groupby(['Gender','Result'])
Dataset.count()

"""# Prediction with Models"""

from sklearn import model_selection

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
l = LogisticRegression()
r = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
k = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
s = SVC(kernel = 'rbf', random_state = 0)

classifier = [l,r,k,s]
for cl in classifier:
    cl.fit(X_train,y_train)

for cl in classifier:
    pred = cl.predict(X_test)
    print(cl," accuracy is : ",accuracy_score(y_test,pred))
    print()

for cl in classifier:
    pred = cl.predict(X_test)
    print(cl,"confusion matrix-")
    print(confusion_matrix(y_test,pred))
    print()

"""# K fold cross Validation score"""

for cl in classifier:
    accuracies = cross_val_score(estimator = cl, X = X_train, y = y_train, cv = 10)
    print(cl, " K fold cross validation score-")
    print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
    print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
    print()

"""# Creating a anemia predictor"""

def anemia_predictor(Gender,Hemoglobin, MCH, MHCH,MCV ):
    a = r.predict(sc.transform([[Gender,Hemoglobin, MCH, MHCH,MCV]]))
    if a == 0:
        print("No anemia.")
    else:
        print("Anemia present.")

Gender = input("Gender:")
Hemoglobin = input("Hemoglobin:")
MCH = input("MCH:")
MHCH = input("MHCH:")
MCV = input("MCV:")
anemia_predictor(Gender,Hemoglobin, MCH, MHCH,MCV )