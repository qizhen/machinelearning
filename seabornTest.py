# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:23:13 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt


import seaborn as sns
sns.set(style="whitegrid",color_codes = True)
np.random.seed(sum(map(ord, "distributions")))

#################################################
'''
一维数据
'''
'''

#x = np.random.normal(size=100)
#plt.hist(x)

#sns.kdeplot(x,shade=True)

#sns.distplot(x)

#sns.distplot(x, kde=False, rug=True)
#sns.distplot(x, hist=False, rug=True)

#sns.distplot(x, bins=20, kde=False, rug=True)

x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)
'''
#############################################
'''
二维数据
'''
'''
#mean, cov = [0, 1], [(1, .5), (.5, 1)]
#data = np.random.multivariate_normal(mean, cov, 200)
#df = pd.DataFrame(data, columns=["x", "y"])

#plt.scatter(df['x'].values,df['y'].values)

#sns.jointplot(x="x", y="y", data=df);

#sns.jointplot(x="x", y="y", data=df,kind ='hex' )
#sns.jointplot(x="x", y="y", data=df, kind="kde")
#
#f, ax = plt.subplots(figsize=(6, 6))
#cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
#sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)

#g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
#g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
#
#g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$X$", "$Y$");

iris = sns.load_dataset("iris")
#sns.pairplot(iris);
#sns.pairplot(iris, kind="reg")
#sns.pairplot(iris, hue="species", palette="husl")

g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot);

'''

##################################33
'''
带有类别属性的数据可视化
'''
'''
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

#sns.stripplot(x="day", y="total_bill", data=tips);

#sns.stripplot(x="day", y="total_bill", data=tips, jitter=True);

#sns.swarmplot(x="day", y="total_bill", data=tips);

#sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
#sns.swarmplot(x="day", y="total_bill", data=tips, color="w", alpha=.5);

#sns.barplot(x="sex", y="survived", hue="class", data=titanic);

g = sns.PairGrid(tips,x_vars=["smoker", "time", "sex"],y_vars=["total_bill", "tip"],aspect=.75, height=3.5)
g.map(sns.violinplot, palette="pastel");

'''

#####################################3
'''
线性回归
'''
tips = sns.load_dataset("tips")
#sns.regplot(x="total_bill", y="tip", data=tips);
#sns.lmplot(x="total_bill", y="tip", data=tips);

#带有奇异值

anscombe = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),ci=None, scatter_kws={"s": 80})

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),robust=True, ci=None, scatter_kws={"s": 80})