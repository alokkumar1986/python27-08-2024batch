# Logical Operators
'''and
or
not '''

#precedency order (highest to loweset) : not and or

# <left operand> logical operator <right operand>
# Output : True/False

'''True and True  = True
True and False = False
False and True = False
False and False = False

True or True  = True
True or False = True
False or True = True
False or False = False

not True = False
not False = True '''

a = 10
b = 20
print(a and b) #20
print(a or b) #10

print(a>b and b>a) #False
print(a>b or b>a) # True

print(a>b or b>a and b!=a)  #a>b or (b>a and b!a)  #True