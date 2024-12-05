#multple inheritance

class Employee:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(self.name)


class Department:
    def __init__(self, deptname):
        self.deptname = deptname
    def showDept(self):
        print(self.deptname)


class SalesEmployee(Department, Employee):
    def __init__(self, name, deptname):
        self.name = name
        self.deptname =deptname

    # def show(self):
    #     super().showName()
    #     super().showDept()


s = SalesEmployee('Harendra', 'Human Resource')
# s.show()
s.showName()
s.showDept()

# Write a programm to demonstrate adding and substraction of two numbers in multiple inheritance concept
class addNum:
   add
class substractNum
   substraction
class TwoNum(addNum, substractNum):
