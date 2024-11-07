# []  : A set of character

import re
'''
str = 'Python easy learning in easy'
c = re.findall('easy', str)
print(c)
print(len(c))
'''

str = 'Python easy learning in easy'
c = re.findall('[a-t]', str)
print(c)
print(len(c))

#write program to find the name containing 'a' as a charcter in third location
#['Sukant', 'Saurav', 'Saam', 'Harendra']

