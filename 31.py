#set

#store multiple values without duplicates and order is not important 

a = {10, 20, 10, 40, 50, 30, 40, 'aptech', 'aptech', 10.7}
print(type(a))

print(a)


#set doest not support index to access the values
#print(a[0])  

#set doesnot supports slicing
#print(a[0:4])


print(a)
a.add(70) 
print(a) 
a.remove(20)
print(a)

# a.append(100) #error append() is not an attribute of set
# print(a)


