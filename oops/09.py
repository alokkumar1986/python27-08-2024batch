#method overriding : Oops concept

#When we redefine a method of parent class in the child class, it is called as method overriding

class Employee:
    def __init__(self, name, bpay):
        self.name = name
        self.bpay = bpay
    def getGross(self):
        return f'{self.bpay}'
class SelesEmployee(Employee):
    def __init__(self, name, bpay, incentive):
        self.name = name
        self.bpay = bpay
        self.incentive = incentive
    def getGross(self):  #method Overriding
        return f'{self.bpay+self.incentive}'    
s = SelesEmployee('Rama', 1500, 200)
print(s.getGross())
