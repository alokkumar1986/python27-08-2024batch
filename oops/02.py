'''
def sum(x, y):
    return x+y

a, b = 10, 20
print("sum of a, b is :", sum(a,b))

'''

'''
class NumberClass:
    x, y =0, 0
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def sum(self):
        return self.x+self.y

s = NumberClass(10, 20)
print("Sum is : ", s.sum())

'''

#write a program to find maximum of two number using oops
'''
def maxNum(x, y):
    if( x>y ):
        return x
    else:
        return y

a, b = 10, 20
print("Maximum number is ", maxNum(a,b))
'''
class NumberMax:
    a, b= 0, 0
    def __init__(self, a, b):
        self.a =a 
        self.b =b
    def maxNum(self):
        if( self.a>self.b ):
         return self.a
        else:
         return self.b
obj = NumberMax(10, 20)
print("Maximum number is :", obj.maxNum())

