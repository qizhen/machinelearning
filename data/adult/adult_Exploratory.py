# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:49:14 2018

@author: Administrator
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

adult = pd.read_csv("adult_df.csv")
summary = adult.describe()

def featurePer(feature,data):
    featureArr = data.groupby([feature],sort = False)[feature].count().sort_values(ascending = False)
    x = np.arange(len(featureArr.index))
    
    cmap = plt.get_cmap("tab20c")
    colors = cmap(x*2)    
    width = 0.35 
    
    p = plt.bar(x,featureArr/featureArr.sum(),width,color = colors)
    
    # 添加数据标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, round(height,2), ha='center', va='bottom',rotation=45)
            # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')
    add_labels(p)

    
    plt.xticks(x,tuple(featureArr.index),rotation=45)
    plt.grid(True)
    plt.xlabel(feature)
    plt.ylabel("percentage")
    plt.title(feature + " percentage")
    plt.show()

def featurePercentage(feature,data):
    '''
    the feature percentage of income
    '''
    featureArr = data.groupby(['income',feature],sort = False)[feature].count().sort_values(ascending = False)
    x = np.arange(len(featureArr.index.levels[1]))
    
    width = 0.35 
    
    p1 = plt.bar(x,featureArr.loc[' <=50K',:]/featureArr.loc[' <=50K',:].sum(),width)
    p2 = plt.bar(x+width,featureArr.loc[' >50K',:]/featureArr.loc[' >50K',:].sum(),width)
    
    # 添加数据标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, round(height,2), ha='center', va='bottom',rotation=45)
            # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')
    add_labels(p1)
    add_labels(p2)
    
    plt.xticks(x,tuple(featureArr.index.levels[1]),rotation=45)
    plt.legend((p1[0],p2[0]),tuple(data.income.unique()))
    plt.grid(True)
    plt.xlabel(feature)
    plt.ylabel("percentage")
    plt.title(feature + " percentage")
    plt.show()
    


def feaPerforeach(feature,data):
    x = np.arange(len(data.income.unique()))
    cmap = plt.get_cmap("tab20c")
    colors = cmap(x*4)
    width = 0.35
    
    for fea in adult[feature].unique():
        featureArr = adult.loc[adult[feature] == fea,:].groupby(['income'])[feature].count()
    
        p1 = plt.bar(x,featureArr/featureArr.sum(),width,color = colors)
        
        # 添加数据标签
        def add_labels(rects):
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height, round(height,2), ha='center', va='bottom')
                # 柱形图边缘用白色填充，纯粹为了美观
                rect.set_edgecolor('white')
        add_labels(p1)
        
        plt.xticks(x,tuple(featureArr.index),rotation=30)
        plt.xlabel("income")
        plt.ylabel("percentage")
        
        plt.grid(True)
        plt.title(fea)
        plt.show()


#############################

#age1 = adult.groupby(['income'])['age'].get_group(' <=50K')
#age2 = adult.groupby(['income'])['age'].get_group(' >50K')
#
#
#p1=plt.hist(age1,bins=20,facecolor='g', alpha=0.75)
#p2=plt.hist(age2,bins=20,facecolor='r', alpha=0.75)
#
#
#plt.legend((p1[0], p2[0]), tuple(adult.income.unique()))
#
#
#plt.title("cap_loss")
#plt.grid(True)
#plt.show()

##############################################

#workhour_M = adult.groupby(['sex']).get_group(adult.sex.unique()[0])
#workhour_F = adult.groupby(['sex']).get_group(adult.sex.unique()[1])
#
#workhour_M = workhour_M.groupby(['age'])['hours_per_week'].mean()
#
#workhour_F = workhour_F.groupby(['age'])['hours_per_week'].mean()
#p1=plt.plot(workhour_M.index,workhour_M)
#p2=plt.plot(workhour_F.index,workhour_F)
#plt.legend((p1[0], p2[0]), tuple(adult.sex.unique()))
#plt.grid(True)
#plt.xlabel("Age")
#plt.ylabel("hours_per_work")
#
#plt.show()

###################################################

#plt.boxplot(adult.hours_per_week)
#hours1 = adult.groupby(['income'])['hours_per_week'].get_group(' <=50K')
#hours2 = adult.groupby(['income'])['hours_per_week'].get_group(' >50K')

#plt.boxplot([hours1,hours2],labels=([' <=50K',' >50K']))
#plt.ylim([20,70])
#plt.ylabel("hours_per_week")
#plt.xlabel("income")
#plt.grid(True)

#income1 = adult.groupby(['income']).get_group(' <=50K')
#income2 = adult.groupby(['income']).get_group(' >50K')
#
#hours1 = income1.groupby(['age'])['hours_per_week'].mean()
#hours2 = income2.groupby(['age'])['hours_per_week'].mean()
#
#p1=plt.plot(hours1.index,hours1)
#p2=plt.plot(hours2.index,hours2)
#plt.legend((p1[0], p2[0]), tuple(adult.income.unique()))
#plt.grid(True)
#plt.xlabel("Age")
#plt.ylabel("hours_per_work")
#
#plt.show()

    
#######################################
        

#featurePer('cap_gain',adult)
#featurePercentage('cap_gain',adult)
#feaPerforeach('cap_gain',adult)

#featurePer('cap_loss',adult)
#featurePercentage('cap_loss',adult)
#feaPerforeach('cap_loss',adult)     

#featurePer('hours_w',adult)
#featurePercentage('hours_w',adult)
#feaPerforeach('hours_w',adult)  

#featurePer('native_region',adult)
#featurePercentage('native_region',adult)
#feaPerforeach('native_region',adult)     

#featurePer('workclass',adult)
#featurePercentage('workclass',adult)
#feaPerforeach('workclass',adult)
        
#featurePer('education',adult) 
#featurePercentage('education',adult)
#feaPerforeach('education',adult)


#featurePercentage('marital_status',adult)
#feaPerforeach('marital_status',adult)
        
#featurePer('occupation',adult)
#featurePercentage('occupation',adult)
#feaPerforeach('occupation',adult) 
        
#featurePer('relationship',adult)
#featurePercentage('relationship',adult)
#feaPerforeach('relationship',adult) 

featurePer('race',adult)
featurePercentage('race',adult)
feaPerforeach('race',adult) 

