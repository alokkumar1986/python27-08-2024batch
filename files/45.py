#anonymous function  or lambda function
'''
def add(x, y):
  return x+y

sum = add(10, 20)
print(sum)
'''

#=========================
'''
add = lambda x, y : x+y
print(add(10, 20))
'''

#def, function_name, return is not present in lambda function


# Write a program to create a function to find square of given number

# num = 4, output = 16
'''
def squareIt(num):
    return num*num
num = 4
print('Square of ',4, ' is ', squareIt(num))
'''
'''
squareIt = lambda num: num*num
num = 4
print('Square of ',4, ' is ', squareIt(num))
'''

#Write a program to create a Lambda Function to find biggest of given values a, b, c
'''
def findBig(a, b, c):
    if a>b and a>c :
        print('Biggest is : ', a)
    elif b>c :
        print('Biggest is ', b)
    else:
        print('Biggest is : ', c)

findBig(30, 10, 20)
'''
findBig = a , b, c :
    if a>b and a>c :
        print('Biggest is : ', a)
    elif b>c :
        print('Biggest is ', b)
    else:
        print('Biggest is : ', c)
findBig(30, 10, 20)