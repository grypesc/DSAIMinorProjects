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

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xTrain, yTrain, test_size=0.1, random_state=0)

from sklearn.neural_network import MLPClassifier
neuralNetowrk = MLPClassifier(solver='adam', alpha=1e-6,hidden_layer_sizes=(40, 40), random_state=1)
neuralNetowrk.fit(x_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'.format(neuralNetowrk.score(x_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'.format(neuralNetowrk.score(x_test, y_test)))
# yTest = neuralNetowrk.predict_proba(xTest)
#
# prediction = pd.DataFrame(yTest, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9']).round(5)
# prediction.index += 1
# prediction.to_csv('predictionNeuralNetowrk.csv')
