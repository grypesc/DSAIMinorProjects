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

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()
lda.fit(xTrain, yTrain)
print('Accuracy of LDA classifier on training set: {:.2f}'.format(lda.score(xTrain, yTrain)))
yTest = lda.predict_proba(xTest)

prediction = pd.DataFrame(yTest,dtype=np.float16, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9'])
prediction.index += 1
prediction.to_csv('predictionLDA.csv')
