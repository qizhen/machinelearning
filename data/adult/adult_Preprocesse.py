import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt



def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split(','))-1
    dataMat = []; labelMat = []
    file = open(fileName)
    for line in file.readlines():
        lineArr=[]
        curLine = line.strip().split(',')
        for i in range(numFeat):
            lineArr.append(curLine[i])
        dataMat.append(lineArr)
        if '>' in curLine[-1]:
            labelMat.append(1)
        else:
            labelMat.append(0)
    return dataMat,labelMat


adult = pd.read_table("adult.data.txt",sep=',',names=("age", "workclass", "fnlwgt", 
                        "education", "education_num", 
                        "marital_status", "occupation",
                        "relationship", "race", "sex", 
                        "capital_gain", "capital_loss", 
                        "hours_per_week", "native_country", "income"))
adult.replace(r' ?',np.nan,inplace = True)
adult = adult.dropna(axis = 0)
adult.reset_index(drop=True,inplace = True)
##############################################
adult.loc[adult['hours_per_week']<40,'hours_w'] = "less_than_40"
adult.loc[(adult['hours_per_week']>=40) & (adult['hours_per_week']<45),'hours_w'] = "between_40_and_45"
adult.loc[(adult['hours_per_week']>=45) & (adult['hours_per_week']<60),'hours_w'] = "between_45_and_60"
adult.loc[(adult['hours_per_week']>=60) & (adult['hours_per_week']<80),'hours_w'] = "between_60_and_80"
adult.loc[adult['hours_per_week']>=80,'hours_w']= "more_than_80"
################################################
summary = adult.describe()

Asia_East =(" Cambodia", " China", " Hong", " Laos", " Thailand",
               " Japan", " Taiwan", " Vietnam",' Philippines')

Asia_Central =(" India", " Iran")

Central_America =(" Cuba", " Guatemala", " Jamaica", " Nicaragua", 
                     " Puerto-Rico",  " Dominican-Republic", " El-Salvador", 
                     " Haiti", " Honduras", " Mexico", " Trinadad&Tobago")

South_America =(" Ecuador", " Peru", " Columbia"," Trinadad&Tobago")


Europe_West =(" England", " Germany", " Holand-Netherlands", " Ireland", 
                 " France", " Greece", " Italy", " Portugal", " Scotland")

Europe_East =(" Poland", " Yugoslavia", " Hungary")

North_America =(" United-States", " Canada"," Outlying-US(Guam-USVI-etc)"," South")

adult.loc[adult['native_country'].isin(Asia_East), 'native_region'] = "East-Asia"
adult.loc[adult['native_country'].isin(Asia_Central), 'native_region'] = "Central-Asia"
adult.loc[adult['native_country'].isin(Central_America), 'native_region'] = "Central-America"
adult.loc[adult['native_country'].isin(South_America), 'native_region'] = "South-America"
adult.loc[adult['native_country'].isin(Europe_West), 'native_region'] = "West-Europe"
adult.loc[adult['native_country'].isin(Europe_East), 'native_region'] = "East-Europe"
adult.loc[adult['native_country'].isin(North_America), 'native_region'] = " North_America"


##############################################
adult.loc[adult['capital_gain'] == 0,:].shape[0]/adult.shape[0]
adult.loc[adult['capital_loss'] == 0,:].shape[0]/adult.shape[0]

cg_summary = adult.loc[adult['capital_gain']>0,'capital_gain'].describe()
cl_summary = adult.loc[adult['capital_loss']>0,'capital_loss'].describe()

cg_nonezero = adult.loc[adult['capital_gain']>0,'capital_gain']
cl_nonezero = adult.loc[adult['capital_loss']>0,'capital_loss']

#plt.figure()
#plt.hist(cg_nonezero)
#plt.figure()
#plt.hist(cl_nonezero)

adult.loc[adult['capital_gain']<3464,'cap_gain'] = "Low"
adult.loc[(adult['capital_gain']>=3464) & (adult['capital_gain']<14080),'cap_gain'] = "Medium"
adult.loc[adult['capital_gain']>=14080,'cap_gain'] = "High"

adult.loc[adult['capital_loss']<1672,'cap_loss'] = "Low"
adult.loc[(adult['capital_loss']>=1672) & (adult['capital_loss']<1977),'cap_loss'] = "Medium"
adult.loc[adult['capital_loss']>=1977,'cap_loss'] = "High"
######################################
work_class = adult.groupby(by = 'workclass')['workclass'].count()
adult = adult.loc[adult.workclass !=' Without-pay',:]
#plt.pie(x=work_class,labels = work_class.index)

adult = adult.loc[adult.education != ' Preschool',:]
adult.to_csv('adult_df.csv',header = True,index = False)