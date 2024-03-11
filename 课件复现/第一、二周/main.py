# age = input ("输入年龄")
print(1, 2, 3, sep = "/")
print(1.23456e9)
print(ord("好"))
print(chr(22908))
print(len([1, 2, 3]))
print('Hello %s %d'%('asds', 12))


f = lambda a, b, c: a + b + c
print(f(1, 2, 3))
print((lambda a, b: a - b)(3, 2))

def deco(func):
    def d5(*args):
        print("start")
        func(*args)
        print("end")
    return d5

@deco
def hi():
    print("hi")

hi()

def bye():
    print("bye")

bye = deco(bye)
bye()

print("--------类的迭代器----------")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))


print("-----科学计算包numpy-------")
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)

print("-----pandas-------------")
import pandas as pd

a = pd.DataFrame({'one': [1, 2], 'two': [5, 6]})

print(a)
