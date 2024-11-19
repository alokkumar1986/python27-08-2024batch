OPPS : Object oriented programming

Everything is an object. 
Object is an instance of class. 

Class is a template which contains all the variables and methods.

syntax : 

class Person:
    x,y = 10, 20
    print('Sum is :' , sum(x, y))

    def __init__(_self):


    def sum(_self, a, b):
        return a+b
    

p = Person()

print(p.x)


Every class should have a constructor 

__init__()

It is used to intialize the class variables