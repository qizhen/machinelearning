import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

sns.set_context('poster')

def getData():
    '''
    Get the data
    '''
    filePath = "./data/challenger_data.csv"
    data = np.genfromtxt(filePath,skip_header=1, usecols=[1,2],missing_values='NA',delimiter=',')

    data = data[~np.isnan(data[:,1])]
    return data

def prepareForFit(data):
    '''
    Make the temperature-values unique, and count the number of failure and successes

    Params
    -----------
    data: The data to be process
    -----------

    Returns
    -----------
    DataFrame

    '''

    df = pd.DataFrame()
    df['temp'] = np.unique(data[:,0])
    df['value'] = 0
    df.index = df.temp.values

    for i in range(data.shape[0]):
        temp = data[i,0]
        val = data[i,1]
        if val == 1:
            df.loc[temp,'value'] = 1
    return df

def model(x):
    return 1 / (1 + np.exp(-x))

def showResult(data,clf):
    '''
    Show the original data, and the result of logit-fit

    Params
    -------------
    data: The challenger_data
    model: Logistic regression

    '''

    temperature = data[:,0]
    failures = data[:,1]

    plt.figure()
    sns.set_style('darkgrid')
    np.set_printoptions(precision=3, suppress=True)

    plt.scatter(temperature,failures, s=200, color='k', alpha=0.5)
    plt.yticks([0,1])
    plt.ylabel("Damage Incident")
    plt.xlabel("Outside temperature [F]")
    plt.title("Defects of the Space Shuttle O-Rings vs temperature")
    plt.tight_layout

    x = np.arange(50,85)
    y = model(x* lr.coef_ + lr.intercept_).ravel()

    plt.hold(True)
    plt.plot(x,y,color = 'red',linewidth = 3)
    plt.xlim([50,85])


if __name__ == '__main__':
    data = getData()
    dfFit = prepareForFit(data)

    x=dfFit.temp
    x = x[:,np.newaxis]
    y=dfFit['value']

#    penaltys = ['l1','l2']
#    Cs = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
#    tuned_parameters = dict(penalty = penaltys, C = Cs)
#    lr = LogisticRegression()
#    grid= GridSearchCV(lr, tuned_parameters, cv=5)
#
#    grid.fit(x,y)
#    
#    print(grid.best_estimator_)
#    print(grid.best_params_)
#    print(grid.best_score_)
#    
    lr =LogisticRegression(C=10, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l1', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)
    lr.fit(x,y)
    

    showResult(data,lr)

