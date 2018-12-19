# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:13:31 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
from pylab import *
################exp1
'''
series
'''

#s = pd.Series([1,3,5,np.nan,6,8])

#############exp2
'''
 DataFrame
 
'''

'''
 NumPy array, with a datetime index and labeled columns:
'''
#dates = pd.date_range('20130101', periods=6)
#df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

'''
by passing a dict of objects that can be converted to series-like
'''

df = pd.DataFrame({ 'A' : 1.,
                      'B' : pd.Timestamp('20130102'),
                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                      'D' : np.array([3] * 4,dtype='int32'),
                      'E' : pd.Categorical(["test","train","test","train"]),
                      'F' : 'foo' })

#############exp3
'''
Viewing Data
'''
df.head()
df.tail()
df.index
df.columns
df.values

df.describe()       #统计描述

df.T                #转置

'''
Sorting by an axis:
'''

df.sort_index(axis=1, ascending=False)

'''
Sorting by values:
'''

df.sort_values(by='B')

##############exp4

''''
Selection
''''
df.A
df['A']

'''
 slices the rows.
'''

df[0:3]

df['20130102':'20130104']

df.loc[dates[0]] = df.iloc[0]
'''
Selection by Label
'''
df.loc[:,['A','B']]

df.loc[dates[0],'A'] = df.at[dates[0],'A']


df.iloc[3:5,0:2]

df.iloc[[1,2,4],[0,2]]

df.iloc[:,1:3]

'''
Boolean Indexing
'''

df[df.A > 0]

df[df > 0]

'''
isin()
'''
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['!'].isin(['two','four'])]


#############exp5

'''
赋值
'''

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))

df['F'] = s1

df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.loc[:,'D'] = np.array([5] * len(df))

############exp6
'''
Missing Data
dropna
fillna
isna
'''

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1],'E'] = 1

df1.dropna(how='any')
df1.fillna(value=5)
pd.isna(df1)

##############exp7
'''
Stats
mean()
'''

df.mean()

'''
Apply
'''

df.apply(np.cumsum)


'''
String Methods
'''

 s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
 
 s.str.lower()
 
 ##############exp8
 
 '''
 Merge
 '''
 
 df = pd.DataFrame(np.random.randn(10, 4))
 
 pieces = [df[:3], df[3:7], df[7:]]
 
 pd.concat(pieces)
 
 '''
 Join
 '''
 
 left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
 
 right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
 pd.merge(left, right, on='key')
 
 '''
 Append
 '''
 
 df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
 s = df.iloc[3]
 df.append(s, ignore_index=True)
 
 
 ##################exp9
 '''
 Grouping
 '''
 
 df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                              'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                    'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
    
 df.groupby('A').sum()
 
  df.groupby(['A','B']).sum()
  
###################exp10
  '''
  Reshaping
  stack
  '''
  
  tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                  ['one', 'two', 'one', 'two',
                   'one', 'two', 'one', 'two']]))
    
 index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
 
 df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
 
 df2 = df[:4]
  stacked = df2.stack()
  stacked.unstack(1)
  stacked.unstack(0)
  
'''
Pivot Tables
'''

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                       'B' : ['A', 'B', 'C'] * 4,
                       'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D' : np.random.randn(12),
                       'E' : np.random.randn(12)})

###############exp11
    
'''
Time Series
'''

 rng = pd.date_range('1/1/2012', periods=100, freq='S')
 ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
 ts.resample('5Min').sum()
  
'''
time zone
'''
 rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
 ts = pd.Series(np.random.randn(len(rng)), rng)
 ts_utc = ts.tz_localize('UTC')
 
 
 rng = pd.date_range('1/1/2012', periods=5, freq='M')
 
'''
Converting between time span
'''
 
 ts = pd.Series(np.random.randn(len(rng)), index=rng)
 
 ps = ts.to_period()
  
 ps.to_timestamp()
 
 prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
 ts = pd.Series(np.random.randn(len(prng)), prng)
 ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
 
 ############exp12
 
 '''
 Categoricals
 '''
 
  df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
  df["grade"] = df["raw_grade"].astype("category")
  df["grade"]
  
  df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
  df.sort_values(by="grade")
  
  df.groupby("grade").size()
  
  ############exp13
  
'''
Plotting
'''

 ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
 ts = ts.cumsum()  
 ts.plot()
 
 df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                 columns=['A', 'B', 'C', 'D']) 
 df = df.cumsum()
 plt.figure(); df.plot(); plt.legend(loc='best')
 
###############exp14
 
 '''
 Getting Data In/Out
 '''
 
 df.to_csv('foo.csv')
 pd.read_csv('foo.csv')
 
 df.to_excel('foo.xlsx', sheet_name='Sheet1')
 pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])