from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import random

learningRate = 0.001 #try on different learning rates like 0.1, 0.01, 0.001 and 0.05
epochs = 10000;

np.random.seed(0)
feature_set, labels = datasets.make_moons(100, noise=0.15)
# plt.figure(figsize=(10,7))
# plt.scatter(feature_set[:,0], feature_set[:,1], c=labels, cmap=plt.cm.winter)
# plt.show();

labels = labels.reshape(100, 1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoidDeriative(x):
    return sigmoid(x) *(1-sigmoid (x))

def LeakyReLU(x):
    return np.where(x > 0, x, x * learningRate)

def LeakyReLUDeriative(x):
    return np.where(x > 0, 1, learningRate)

wh = np.random.rand(len(feature_set[0]),4) #hidden layers weights
wo = np.random.rand(4, 1) #output layers weights

errorArray = []
for epoch in range(epochs):
    # feedforward
    zh = np.dot(feature_set, wh)
    ah = sigmoid(zh) #output of hidden layer

    zo = np.dot(ah, wo)
    ao = sigmoid(zo) #output of output layer

    # backpropagation

    error = ((1 / 2) * (np.power((ao - labels), 2))) #MSE
    print(error.sum())
    errorArray.append(error.sum());

    dcost_dao = ao - labels #d means derivative
    dao_dzo = sigmoidDeriative(zo)
    dzo_dwo = ah

    dcost_wo = np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

    dcost_dzo = dcost_dao * dao_dzo
    dzo_dah = wo
    dcost_dah = np.dot(dcost_dzo , dzo_dah.T)
    dah_dzh = sigmoidDeriative(zh)
    dzh_dwh = feature_set
    dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

    wh -= learningRate * dcost_wh
    wo -= learningRate * dcost_wo

def predict(x,y):
    point = np.array([x,y])
    zh = np.dot(point, wh)
    ah = sigmoid(zh)
    zo = np.dot(ah, wo)
    result = sigmoid(zo)
    print("("+str(x)+","+str(y)+") probability: "+str(result) + " that the point belongs to the green set")

def showErrorGraph():
    from matplotlib import pyplot as plt2
    input = np.linspace(0, epochs, epochs)
    plt2.suptitle('Learning rate = ' +str(learningRate))
    plt2.xlabel('Number of epochs')
    plt2.ylabel('Mean squared error')
    plt2.plot(input, errorArray, c="r")
    plt2.show()

for i in range (1,20):
    predict(round(random.uniform(-1.0, 2.0),1), round(random.uniform(-0.75, 1.25),1))

showErrorGraph()
