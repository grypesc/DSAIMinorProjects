import csv
import pandas as pd
import numpy as np

dataTrain = pd.read_csv('train.csv')
dataTest = pd.read_csv('test.csv')

feature_names = []
for i in range (1, 93):
    feature_names.append('feat_' + str(i))

xTrain = dataTrain[feature_names]
yTrain = dataTrain['target']

xTest = dataTest[feature_names]

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(xTrain, yTrain)
print('Accuracy of logistic regression classifier on training set: {:.2f}'.format(logreg.score(xTrain, yTrain)))
yTest = logreg.predict_proba(xTest)

prediction = pd.DataFrame(yTest, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9']).round(4)
prediction.index += 1
prediction.to_csv('predictionLogistic.csv')
