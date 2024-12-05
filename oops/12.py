from abc import ABC, abstractmethod

class XYZ(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def showName(self):
        pass

class PQR(XYZ):
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


x = PQR('Aptech')
x.showName()