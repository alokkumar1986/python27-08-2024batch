class AddTwoNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addNum(self):
        return self.a+self.b

class SubsctractTwoNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def subsctractNum(self):
        return self.a-self.b


class TwoNum(SubsctractTwoNum, AddTwoNum):
    def __init__(self, a, b):
        self.a = a
        self.b = b


t = TwoNum(20, 10)
print(t.addNum())
print(t.subsctractNum())
