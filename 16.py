'''
*
**
***
****
*****
'''

for i in range(1,6):
    print('*'*i)
    
'''
     #
    # #
  #  #  #
#  #  #   #
'''

for i in range(1, 6):
    print(" "*(6-i), end='')
    print(i*'# ')
    
'''while (condition):
    statement '''

i = 1
while(i<11):
    print(i)
    i=i+1

j = 1
while(j<6):
    print(' '*(6-j), end= '')
    print('# '*j)
    j= j+1
    