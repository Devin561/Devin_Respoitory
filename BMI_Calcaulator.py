import numpy as np

def Cal(h, w):
    BMI = w/(h*h)
    return BMI

w_i = float(input("请输入你的体重（kg）："))
h_i = float(input(("请输入你的身高（cm）：")))

bmi = round(Cal(h_i/100, w_i), 2)
print("你的BMI指数为： {0}".format(bmi))

if bmi<18.5:
    print("根据我们的计算，你目前的体重指数偏低！")
elif bmi<23.9:
    print("根据我们的计算，你目前的体重指数正常！")
elif bmi<27:
    print("根据我们的计算，你目前的体重指数略高于正常范围！")
elif bmi<=32:
    print("根据我们的计算，你目前的体重指数已经属于肥胖范围！")
elif bmi>32:
    print("根据我们的计算，你目前的体重指数已经属于过于肥胖范围！")
else:
    print("输入有误！")
w1 = round(18.5*((h_i/100)**2))
w2 = round(23.9*((h_i/100)**2))

print("您的正常体重范围应该在：{0}kg - {1}kg  之间".format(w1, w2))

