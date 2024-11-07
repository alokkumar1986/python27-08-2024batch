# split
import re
'''
str1 = 'Hockey is our national game'
f = re.split('\s', str1)
print(f)
'''
#write a program to read number of words in a file
try:
 f = open('demo1.txt', 'w')
except:
 print('File not found')
else: 
 f.write('\nHockey is our national game')
 f.close()

try:
    f1 = open('demo1.txt', 'r')
except:
    print('File not found')
else: 
    str1 = re.split('\s',f1.read())
    print('Number of words in the file is : ', len(str1))
    f1.close()
