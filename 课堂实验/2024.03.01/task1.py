def add(*args):
    print(sum(args))

def data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    d = 4
    print("a + b + c =")
    add(a, b, c)
    print("a + b + c + d =")
    add(a, b, c, d)

    print("----------------")
    data(name = "D5", city = "ShenZhen", number = "22354191")