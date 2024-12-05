#inheritance

class Person:
    def __init__(self, name):
       self.name= name
    def greet(self):
        return f'Hi, {self.name} from Person class'

class Employee :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f'Hi, {self.name} from Employee class'


p = Person('Aptech')
print(p.greet())

e = Employee('Aptech Learning', 30)
print(e.greet())

