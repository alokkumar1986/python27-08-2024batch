#Regular Expression :

import re

'''
findall() : Find all the occurance string in a string
search()  : Find first occurance of a string/character in string / None
split()   : Prepare a list of string by spliting with a character from a string
sub()     : Find a string/character in another string and replace with a string/character
'''

txt = 'Python Tutorial in Aptech'
c = re.findall('[Tt]', txt)
print(c)

q = re.search('t', txt)
print(q)