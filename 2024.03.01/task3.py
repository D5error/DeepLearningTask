if __name__ == "__main__":
    list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    it = iter(list)

    print(it)
    for i in range(5):
        print(next(it))