#Collection  

'''Collection is a type where we can store more values

str 
list
tuple
set
frozenset
dict '''

# list 

# list is a collection where we can store ordered, changable, duplicate values.

#syntax to declare a list
'''
variablename = [val1, val2, val3 .....]
variablename = list((val1, val2, val3...))
'''

#list values are indexed
# a = [1, 2, 5, 7, 9, 2, 9] #a[1] = 2

#list supports slicing
#a = [1, 2, 5, 7, 9, 2, 9]    #var[startindex:endindex:step]
#print(a[1:]) # 2, 5, 7, 9, 2, 9

#list is changable
# a = [1, 2, 5, 7, 9, 2, 9]
# print(a) # [1,2,5,7,9,2,9]
# a[6] = 20
# print(a) #[1,2,5,7,9,2,20]

#list can hold multiple types of values
'''
a = [1, 2, 5, 7, 9, 2, 9]
b = [1.0, 2.7, 5.7, 6.5, 2.3]
c = [True, False, False, False, True]
d = [100, 100.8, True, 100+10j, 'Aptech']
print(a[3]) #7
print(b[2]) #5.7
print(c[4]) #True
print(d[3]) #100+10j
'''

#list can hold duplicate value
'''
a = [1, 2, 5, 7, 9, 2, 9]
b = list((1, 2, 5, 7, 9, 2, 9))
print(a)
print(b)
'''

#list is ordered
#ordered means addtion of value is from right and removal is from left
'''
a = [1, 2, 5, 7, 9, 2, 9]
print(a)
a.append(6)  #append() is used to add a value to the list
             #[1, 2, 5, 7, 9, 2, 9, 6]
print(a)
a.append(7) #[1, 2, 5, 7, 9, 2, 9, 6, 7]
print(a)
a.append(100) #[1, 2, 5, 7, 9, 2, 9, 6, 7, 100]
print(a)

a.remove(2) #[1, 5, 7, 9, 2, 9, 6, 7, 100]
print(a)
a.remove(9) #[1, 5, 7, 2, 9, 6, 7, 100]
print(a)
'''

#How we access the values of a list
'''
a = [1, 2, 5, 7, 9, 2, 9]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7]) #error index out of range
for i in a:
    if i%2!=0:
      print(i)
      
'''
   
   
#list is dynamic 
a = [1, 2, 5, 7, 9, 2, 9]
print(len(a))  #len() = no of values in a list
# print(a[7])
a.append(100)
print(len(a))
print(a[7])