import random
from multiprocessing import Pool

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
def anothermontecarlocool(c):
    integral = 0
    for i in range(c):
        x = random.uniform(2, 8)
        integral += f(x)
        integral_ = (8-2)*integral/c
    return integral_
def test_all(pool):
    l = pool.map(anothermontecarlocool, range(100000, 150000))
    return l
if anothermontecarlocool == 'main':
    pool = Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print("integral_:", integral_)
