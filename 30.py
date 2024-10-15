#tuple 

#tuple is same as list but it is read only (immutable) version of list

a = (1, 3, 4, 2, 4)   #tuple declarartion
print(type(a))

b = [1, 3, 4, 2, 4]
b.append(12)
print(b)
b[2] = 10
print(b)
b.remove(1)
print(b)


#read only version of list
# a[2] = 10  #error
# a.append(12) #error 
# print(a)
# a.remove(1) #error
# print(a)


#tuple can hold multiple datatype values
x = (90, 'aptech', 10.7, 10+90j)
print(x)


#tuple supports slicing
# print(a[:])
# print(a[::2])

#tuple can hold duplicate value

#we can access tuple element using index
print(a[0])
#print(a[10])  # error
print(a[-4])  #3
#print(a[-6])  # error
'''
for i in b:
    print(i)
'''  
for j in a:
    print(j)