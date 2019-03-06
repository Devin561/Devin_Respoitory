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

# start = time.clock()
font = FontProperties(fname="C:/Windows/Fonts/simhei.ttf", size=14)

# t = np.arange(1, 10, 0.05)
# x = np.sin(t)
# y = np.cos(t)
#
# plt.figure(figsize=(8, 5))
# plt.plot(x, y, 'r-*')
# plt.axis('equal')
# plt.xlabel('正弦', FontProperties = font)
# plt.ylabel('余弦', FontProperties = font)
# plt.title('一个圆', FontProperties = font)
#

iris = load_iris() #example
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
# df.to_csv('outdf.txt', sep='\t')
# plt.subplot(2, 1, 1)
sns.violinplot(x='target', y='sepal length (cm)', data=df, inner=None)
sns.swarmplot(x='target', y='sepal length (cm)', data=df,color='w', alpha = .5)

# plt.subplot(2, 1, 2)
plt.figure(figsize=(6,4))
andrews_curves(df, 'target')
plt.title("andrews curves")
#
#
def function1(x0, x1):
    return x0**2 + x1**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
x0 = np.arange(-3, 3, 0.1)
x1 = np.arange(-3, 3, 0.1)
x0,x1 = np.meshgrid(x0, x1)
y = function1(x0, x1)
ax.plot_wireframe(x0, x1, y, rstride=5, cstride=5)
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.set_zlabel('f(x0, x1)')
# time.sleep(5)
# end = time.clock()
# print("加载消耗：{0}s".format(end - start))
t = time.perf_counter()
print("加载消耗：{0}s".format(t))
plt.show()