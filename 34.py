'''
list  = []  duplicate, order, mutable
tuple = ()  duplicate, order, immutable
set = {}    no duplicate, no order, mutable
frozenset = {}  no duplicate, no order, immutable


dict =

'''
'''
range() : It is a function which returns a sequence of values. By default
values are increased by 1 and stops before end index.

syntax :
range(start, end, step)

a = range(0, 10, 3)  = 0, 3, 6, 9

a = range(0, 10)  = 0, 1, 2, ....... 9

a = range(10, 0, -1)  = 10, 9....... 1

 '''
 
'''
a = range(0, 10)
print(a)
for i in a:
    print(i)
'''
    
'''    
a = range(10)  #: start = 0, end =10, step =1
for i in a:
    print(i)
'''

#write a program to print values in decrasing order from 100 to 78
'''
a = range(100, 77, -1)
for i in a:
    print(i)
'''
    
#write all even numbers between 1 t0 25
'''
a = range(2, 25, 2)
for i in a: 
    print(i)
'''    
#write a program to print following patterns 
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

        1
      1   2
    1   2   3
  1   2   3   4   
'''

# range supports index, slicing

a = range(1, 21) # 1, 2, 3, ........ 20
print(a[0])  # 1
print(a[-1]) # 20
print(a[1:5]) # range(2, 6)
print(a[:-1]) # range(1, 20)
print(a[-1: :-1]) # range(20, 0, -1)
print(a[::-1])  # range(20, 0, -1)
print(a[::1])  # range(1, 21)


'''
range Data Type represents a sequence of numbers.
Different forms of ragne data type are as follows:
 1. range with one argument   -    range(10) 
 2. range with Two arguments   -    range(10,21) 
 3. range with three arguments   -    range(10,21,2)
Once order is important, obviously indexing, slicing concepts are also applicable.
range object is immutable

'''

a = range(10)
#a[0] = 10
