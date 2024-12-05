'''
__init__() #Used bydefault to initilaize class variables
__str__() #Used to make string representation of class

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Person(name : {self.name}, age : {self.age})'

p = Person('Ardhendu', 34)
print(p.name) #Ardhendu
print(p.age) #34
print(p)
p1 = Person('Ramchandra', 23)
print(p1)

#write a program to represent a class in string having three variables

X(xyz : 'Aptech',pqr : [20])

