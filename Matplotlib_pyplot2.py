#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
from pandas.plotting import andrews_curves
from sklearn.datasets import load_iris
import seaborn as sns
from mpl_toolkits.mplot3d import axes3d
import time
import xlrd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def fun(t):
    return t**2 + 50

if __name__ == '__main__':
    # t1 = np.arange(1, 10, 0.5)
    # t2 = np.arange(1, 10, 0.2)
    # a = [3654,3624,3651,3490,3474,3586,3628,3686,3524,3577]
    # b = [3574,3633,3580,3640,3570,3608,3704,3683,3564,3598]
    # plt.figure(24)
    # plt.subplot(221)
    # plt.plot(a, b, 'b+', b, a, 'r--')
    df = pd.read_excel('aaa.xlsx', header=0)
    plt.figure(24)
    plt.subplot(221)
    plt.plot(df.iloc[:,0], df.iloc[:,5])

    plt.subplot(222)

    formula = 'df.iloc[:,5] ~ df.iloc[:,0] + df.iloc[:,1]+ df.iloc[:,2]+ df.iloc[:,3]+ df.iloc[:,4]'
    rst = anova_lm(ols(formula, df).fit())
    print(rst)
    print("="*401)
    print(pairwise_tukeyhsd(df.iloc[:,5], df.iloc[:,3]))


    # plt.figure(12)
    # plt.subplot(221)
    # plt.plot(t1, fun(t1), 'b+', t2, fun(t2), 'r--')
    #
    # plt.subplot(222)
    # plt.plot(t2, np.cos(2*np.pi * t2), 'bo')
    #
    # plt.subplot(212)
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])



    plt.show()