class ParentClass:
    num = 100
    res = num + 19

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def testing(self):
        return self.res + 1

    def sum(self):
        return self.a + self.b


if __name__ == "__main__":
    obj = ParentClass(1, 2)
    print(obj.sum())
