from task1 import add
def deco(func):
    def wrapper(*args):
        print("函数开始")
        f = func(*args)
        print("函数结束")
    return wrapper

@deco
def sayHello():
    print("hello world!")

if __name__ == "__main__":
    add = deco(add)
    add(1, 2, 3, 4, 5)
    add(1, 2)
    print("--------------------")

    sayHello()