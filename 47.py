num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
try:
    if num2 == 0:
        raise Exception('Sorry, numb2 can not be zero')
except :
    print('Sorry, numb2 can not be zero')
else :
    division = num1/num2
    print('Division of ', num1, ' and ', num2, ' is : ', division)