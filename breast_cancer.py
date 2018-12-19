# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:08:44 2018

@author: Administrator
"""

from sklearn import metrics
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

x_train,x_test,y_train,y_test= train_test_split(cancer.data,cancer.target,random_state = 0)

lr = LogisticRegression()
lr.fit(x_train,y_train)


print("logistic regression with default parameters:")
print("accuracy on the training subset:{:.3f}".format(lr.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(lr.score(x_test,y_test)))
print(lr.sparsify())
print("coefficience:")
print(lr.coef_)
print("intercept:")
print (lr.intercept_)
print()

lr_l1 = LogisticRegression(penalty='l1',tol = 0.01)
lr_l1.fit(x_train,y_train)

print("logistic regression with pernalty l1:")
print("accuracy on the training subset:{:.3f}".format(lr_l1.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(lr_l1.score(x_test,y_test)))
print("coefficience:")
print(lr_l1.coef_)
print("intercept:")
print (lr_l1.intercept_)
print()