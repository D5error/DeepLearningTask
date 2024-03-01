def add(*args):
    print(sum(args))

if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    d = 4
    print("a + b =")
    add(a, b)
    print("a + b + c =")
    add(a, b, c)
    print("a + b + c + d =")
    add(a, b, c, d)