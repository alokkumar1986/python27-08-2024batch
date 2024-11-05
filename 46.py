'''
a = 100
b = 200
c = 50

d = a/b
print(d)
try:
 e = c/5
except :
    print('Error : Division is not possible with 0')
else: 
    print(e)
finally :
    print('Error Handled successfully')
'''

#write a program to input two number and find their division

num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
try :
 division = num1/num2
except : 
 print('Error : Division is not possible with 0')
else: 
 print('Division of ', num1, ' and ', num2, ' is : ', division)

  