#Single Inheritance

class Person: #Parent
    def __init__(self, name):
       self.name= name
    def greet(self):
        return f'Hi, {self.name}'

class Employee(Person) : #Child
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Lima')
e = Employee('Aptech', 34)
print(e.greet())
    
'''
isinstance()
type()
issubclass()
'''
print(type(p))
print(type(e))

# print(isinstance(p, Person))  #True
# print(isinstance(e, Person))  #True

# print(isinstance(p, Employee)) #False
# print(isinstance(e, Employee)) #True

print(issubclass(Employee, Person))  #True
print(issubclass(Person, Employee))  #False