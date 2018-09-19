# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 19:33:25 2018

@author: Teno
"""

from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score

#1
clf = ensemble.RandomForestClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf.fit(X, Y)

prediction1 = clf.predict([[190, 70, 43]])

print(prediction1)

#2

clt = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clt.fit(X, Y)

prediction2 = clt.predict([[190, 70, 43]])

# Compare results 

print(prediction2)

#3
clg = naive_bayes.GaussianNB()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']       

clg.fit(X, Y)

prediction3 = clg.predict([[190, 70, 43]])

print(prediction3)

#COMPARE

y_pred = [prediction1]
y_true = [prediction1]
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize= False))


