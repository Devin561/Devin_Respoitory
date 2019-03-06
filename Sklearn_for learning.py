#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'weight':[51,53,54,55,57,60,62,65,69,72],'height':[152,156,160,164,168,172,176,180,184,188]})
x = pd.DataFrame(df['weight'])
y = df['height']

clf = linear_model.LinearRegression()
clf.fit(x, y)
print('回归系数：\n{0}'.format(clf.coef_))
y_pred = clf.predict(x)
print(y_pred)

plt.scatter(x, y, edgecolors="purple")
plt.plot(x, y_pred, color='yellow', linewidth=1.5)
plt.show()
