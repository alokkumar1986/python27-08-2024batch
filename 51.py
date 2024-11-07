import re
'''
str = 'Python easy learning in easy'
c = re.findall('easy', str)
print(c)
print(len(c))
'''
'''
str = 'Python easy learning in easy'
c = re.search("\n", str)  #escape character \t \n \b
print(c)
# print(c.start())
'''

#write a program to check whether 'cuttack' in 'Bhubaneswar is the capital of Odisha'

str1 = 'Cuttack is the capital of Odisha'
str2 = 'Cuttack'
f = re.search(str2, str1)
if f==None:
    print('Cuttack is not found')
else : 
    print('Cuttack is found')