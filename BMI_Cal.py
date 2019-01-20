#!/usr/bin/python
# -*- coding:utf-8 -*-
#Author: Devin Z
import tkinter as tk


def Cal(h, w):
    global bmi
    bmi = w/(h*h)
    return bmi

def judge1(bmi):
    global i
    if bmi<18.5:
        i = "根据我们的计算，您目前的体重指数偏低！"
    elif bmi<23.9:
        i = "根据我们的计算，您目前的体重指数正常！"
    elif bmi<27:
        i = "根据我们的计算，您目前的体重指数略高于正常范围！"
    elif bmi<=32:
        i = "根据我们的计算，您目前的体重指数已经属于肥胖范围！"
    elif bmi>32:
        i = "根据我们的计算，您目前的体重指数已经属于过于肥胖范围！"
    else:
        i = "输入有误！"
    return i

def reg():
    # 从相应输入框中，得到用户的输入
    try:

        h_i = float(en1.get().strip())
        w_i = float(en2.get().strip())

    except:
        lb4 = tk.Label(base, text="输入有误").grid(row=6, column=0, sticky=tk.W)
        en1.delete(0, 10)
        en2.delete(0, 10)
    lb4 = tk.Label(base, text="您的BMI指数为： {0}".format(round(Cal(h_i / 100, w_i), 2))).grid(row=6, column=0,
                                                                                          sticky=tk.W)
    lb5 = tk.Label(base, text=judge1(round(Cal(h_i / 100, w_i), 2))).grid(row=7, column=0, sticky=tk.W)
    w1 = round(18.5 * ((h_i / 100) ** 2))
    w2 = round(23.9 * ((h_i / 100) ** 2))
    lb6 = tk.Label(base, text="您的体重应控制在：{0}kg - {1}kg  之间".format(w1, w2)).grid(row=8, column=0, sticky=tk.W)



base = tk.Tk()
base.geometry("600x500")
base.wm_title("身体质量指数计算器")

lb1 = tk.Label(base, text= "请填写以下信息", font=("Arial", 20), width=30, height=1,bg="pink")
lb1.grid(row=0, sticky= tk.W)
lb2 = tk.Label(base, text="身高（cm）：", font=("Arial", 17))
lb2.grid(row=1, column=0, sticky= tk.W)
en1 = tk.Entry(base, width=30)
en1.grid(row=2, column=0, sticky=tk.W)
lb3 = tk.Label(base, text="体重（kg）：", font=("Arial", 17))
lb3.grid(row=3, column=0, sticky= tk.W)
en2 = tk.Entry(base, width=30)
en2.grid(row=4, column=0, sticky=tk.W)

btn = tk.Button(base, text="开始计算", command=reg).grid(row=5, column=0, sticky=tk.W)

base.iconbitmap("timg.ico")


base.mainloop()


