'''def add(x,y): 
 return x+y 

# result=add(10,20) 
# print("The sum is",result)
print("The sum is",add(100,200))'''

'''
def fact(num): 
 result=1
 while num>=1: 
    result=result*num 
    num=num-1
 return result 
for i in range(1,50): 
 print("The Factorial of",i,"is :",fact(i))
'''
 #write a program to input a number and find its factorial
'''
def fact(num): 
    result=1
    while num>=1: 
        result=result*num 
        num=num-1
    return result

i = int(input('Enter a number : '))
print("The Factorial of",i,"is :",fact(i))

'''

# A function can returm one or multiple value

def calc(a,b): # Here, 'a' & 'b' are called positional arguments
 sum = a + b
 sub = a - b
 mul = a * b
 div = a / b
 return sum,sub,mul,div


# a,b,c,d = calc(100,50) # Positional arguments
# print(a,b,c,d)

'''t = calc(100,50)
print(type(t))
for i in t :
    print(i, end= ' ')'''

'''
def wish(msg, name ='Guest'):
 print(msg,name)
wish('Hi')

def wish(msg,name ='Guest'):   # name : default argument, msg : positional argument   
 print(msg,name)
wish( name="Aptech" , msg='Hi')   #keyword argument

'''

def sum(*a):  # arbitary argument
    sum = 0
    for i in a:
      sum=sum+i
    return sum
print(sum(10, 90, 80)) 


#function vs module vs package vs library

function : It is few lines of code written  in a program .

A program cam contain several functions (Module)

package is a group of module.

library is a group of package

import function from module

from module import a, b, c

from module import *

import a
