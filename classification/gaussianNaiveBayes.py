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

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(xTrain, yTrain)
print('Accuracy of GNB classifier on training set: {:.2f}'.format(gnb.score(xTrain, yTrain)))
yTest = gnb.predict_proba(xTest)

prediction = pd.DataFrame(yTest,dtype=np.float16, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9'])
prediction.index += 1
prediction.to_csv('predictionGaussian.csv')
