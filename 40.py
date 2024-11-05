#function 

'''def functionname() : #called functio
    body of the function

functionname()   # calling function


parameters or arguments

return statement'''

#Default Argument 
'''
def sum(num1, num2=20):
    return num1+num2

summation = sum(10)

print(summation)
'''


'''def sum(num1, num2=20):
    return num1+num2

summation = sum(10, 30)

print(summation)

'''

# Calling and Called must have same number of arguments/ parameters and order is important
# If there is not equal no. of arguments or parameters in both calling or called function, 
# your program will give error
# For handling this situation, we have default arguments
# Default arguments have a default value in function definition or called function
# when we call the function without passing value of that argument, default value will be cinsidered
# And your program will run successfully
# when we call the function with passing value of that argument, default value will not be cinsidered
# And your program will run successfully


# default argument always comes from the right of the argument list

def sum(num1, num2=40, num3=30):
    return num1+num2+num3

summation = sum(10, 30)
print(summation)