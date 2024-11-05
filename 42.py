#Function recursion

#A function can call itself within its function definition

'''
def my_fn():
    #body
    #print('Hello')
    my_fn()  # recursion

my_fn()
'''

# It is similar like a loop 
# It should be called on a condition, in order to avoid infinite calling


def my_fn(num):
    if num<4 :
        print(num)
    else:
     print(num)  
     num = num-1
     my_fn(num)
my_fn(10)


# Write a program to find even numbers between 1 to 100 using function recursion
def findEven(num):
    if num%2==0 :
        print(num)
    num = num-1
    if num>1:
        findEven(num)
findEven(100)


