#sub()
'''
import re 
str1  = "Hoockey is our national game"
c = re.sub('\s', '#', str1)
print(c)
'''

#write a program to find following output from the given string
#output : "Hockey#is#our national game"
#string : "Hockey is our national game"

'''
import re 
str1  = "Hoockey is our national game"
c = re.sub('\s', '#', str1, 2)
print(c)
'''

#write a program to find the following output from a given string
#output : "Hockeyis#our national game"
#string : "Hockey is our national game"

import re 
str1  = "Hoockey is our national game"
c = re.sub('\s', '#', str1, 2) #Hockey#is#our national game
d = re.sub('#', '', c, 1) #Hockeyis#our national game
print(d)