# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:33:32 2018

@author: Administrator
"""

import numpy as py
import pandas as pd

import scorecardpy as sc
import warnings

warnings.filterwarnings('ignore')

original_data = pd.read_csv('./german.data.txt','\s+')
num_data = pd.read_csv('./german.data-numeric.txt','\s+')

data = sc.germancredit()
#data.head()

print("变量： ",data.columns)
#data.creditability.value_counts()

dt_sel = sc.var_filter(data, y = "creditability")

print("变量预处理前后变化：",data.shape[1],"->",dt_sel.shape[1])

bins = sc.woebin(dt_sel, y="creditability")
sc.woebin_plot(bins['age.in.years'])
sc.woebin_plot(bins['housing'])

breaks_adj = {
    'age.in.years': [26, 35, 40],
    'other.debtors.or.guarantors': ["none", "co-applicant%,%guarantor"]
}
bins_adj = sc.woebin(dt_sel, y="creditability", breaks_list=breaks_adj)

train, test = sc.split_df(dt_sel, 'creditability').values()
print("训练集、测试集划分比例为",train.shape[0],":",test.shape[0])

train_woe = sc.woebin_ply(train, bins_adj)
test_woe = sc.woebin_ply(test, bins_adj)

y_train = train_woe.loc[:,'creditability']
X_train = train_woe.loc[:,train_woe.columns != 'creditability']
y_test = test_woe.loc[:,'creditability']
X_test = test_woe.loc[:,train_woe.columns != 'creditability']

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(penalty='l1', C=0.9, solver='saga', n_jobs=-1)
lr.fit(X_train, y_train)

train_pred = lr.predict_proba(X_train)[:,1]
test_pred = lr.predict_proba(X_test)[:,1]

from sklearn.linear_model import LogisticRegressionCV

c = [1,10,100,1000]
lr_cv=LogisticRegressionCV(Cs=c,cv=5,penalty='l1',solover='liblinear',multi_class='ovr')
lr.fit(X_train,y_train)
lr_cv.scores_

from sklearn.model_selection import GridSearchCV

penaltys = ['l1','l2']
Cs = [0.001,0.01,0.1,1,10,100,1000]
tuned_parameters = dict(penalty=penaltys,C=Cs)

lr_penalty=LogisticRegression()

grid=GridSearchCV(lr_penalty,tuned_parameters,cv=5)
grid.fit(X_train,y_train)

grid.cv_results_
print(grid.best_score_)
print(grid.best_params_)


train_perf = sc.perf_eva(y_train,train_pred,title="train")

test_perf = sc.perf_eva(y_test,test_pred,title="test")
card = sc.scorecard(bins_adj,lr,X_train.columns)

train_score= sc.scorecard_ply(train,card,print_step=0)
test_score=sc.scorecard_ply(test,card,print_step=0)






