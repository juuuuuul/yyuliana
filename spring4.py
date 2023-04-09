import random

def montecarlocool(f, a, b, c):
    integral = 0
    for i in range(c):
        x = random.uniform(a, b)
        integral += f(x)
    integral_ = (b-a)*integral/c
    return integral_

def f(x):
    return x**4+x
integral_ = montecarlocool(f, 2, 8, 100000)
print(integral_)
