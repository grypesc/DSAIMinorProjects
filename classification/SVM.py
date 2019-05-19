import csv
import pandas as pd
import numpy as np

dataTrain = pd.read_csv('train.csv')
dataTest = pd.read_csv('test.csv')

featureNames = []
for i in range (1, 93):
    featureNames.append('feat_' + str(i))
xTrain = dataTrain[featureNames]
yTrain = dataTrain['target']
xTest = dataTest[featureNames]

from sklearn.svm import SVC
svm = SVC(gamma='auto', probability=True)
svm.fit(xTrain, yTrain)
print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(xTrain, yTrain)))
yTest = svm.predict_proba(xTest)

prediction = pd.DataFrame(yTest, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9']).round(5)
prediction.index += 1
prediction.to_csv('predictionSVM.csv')
