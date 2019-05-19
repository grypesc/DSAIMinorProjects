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
x_train, x_test, y_train, y_test = train_test_split(xTrain, yTrain, test_size=0.01, random_state=0)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(x_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'.format(clf.score(x_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'.format(clf.score(x_test, y_test)))
#yTest = clf.predict_proba(xTest)

#prediction = pd.DataFrame(yTest,dtype=np.float16, columns=['Class_1', 'Class_2', 'Class_3', 'Class_4', 'Class_5', 'Class_6', 'Class_7', 'Class_8', 'Class_9'])
#prediction.index += 1
#prediction.to_csv('predictionTree.csv')
