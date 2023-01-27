from ParentClass import ParentClass
from main import Test


class ChildClass(ParentClass):
    t = 10

    def __init__(self):
        ParentClass.__init__(self, 2, 3)

    def getData(self):
        return self.t + self.sum()


a = ChildClass()
print(a.getData())
