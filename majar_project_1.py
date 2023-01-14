# -*- coding: utf-8 -*-
"""Majar Project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ii3I9_hXmsirmcSwSv8ztfdQmInrKpK4
"""

from sklearn.datasets import fetch_openml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

mnist=fetch_openml('MNIST_784')

x=mnist['data']
y=mnist['target']
x=np.array(x)
some_digit=x[36002]
some_digit_img=some_digit.reshape(28,28)
plt.imshow(some_digit_img,cmap=matplotlib.cm.binary)

xtrain,xtest,ytrain,ytest=train_test_split(x,y)

ytrain=ytrain.astype(int)
ytest=ytest.astype(int)

ytrain_2=(ytrain==6)
ytest_2=(ytest==6)

log=LogisticRegression()

log.fit(xtrain,ytrain_2)

log.predict([some_digit])