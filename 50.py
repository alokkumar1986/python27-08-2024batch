#Regular Expression :

import re

'''
findall() : Find all the occurance in a string
search()
find()
sub()

'''

txt = 'Python Tutorial in Aptech'
c = re.findall('[Tt]', txt)
print(c)

q = re.search('t', txt)
print(q)