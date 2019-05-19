import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

from sklearn.preprocessing import StandardScaler
from sklearn.cluster importAgglomerativeClustering
from sklearn.mixture import GaussianMixture
import os
import sys

input = pd.read_csv("iris.csv")
X = input[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

scaler = StandardScaler()
scaler.fit_transform(X)

from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=3)

clust_labels = model.fit_predict(X)
dataFrame = pd.DataFrame(clust_labels)

dataFrame.to_csv('predictionIris.csv')
