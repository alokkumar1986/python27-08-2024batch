#Bitwise Operator
'''
>>  Bitwsie leftshift 
<<  Bitwise rightshift
&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT '''

'''<left operand> Bitwise Operator <right operand>
Convert left and Right operand in Binary

AND : 1 when both bits are 1

2 = 10
3 = 11

2 & 3 = 10 = 2 

x = 12 
y = 13
print(x & y) #12 '''

#OR : 1 when one of the bit is 1

'''x = 12      #1100
y = 13      #1101
print(x | y) #1101 = 13 '''

#XOR : 1 when only one bit is 1

'''x = 12      #1100
y = 13      #1101
print(x ^ y) #0001 = 1 '''

#NOT : The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
#Add 1 then change the sign

'''x = 12      #1100  # 0000 0000 0000 1100
y = 13      #1101
print(~x)   # -13
print(~y)   # -14

print(~-12)  #11

'''
'''1 = 0000 0000 0000 0001
-1 = 1111 1111 1111 1110 
12 = 0000 0000 0000 1100
-12 = 1111 1111 1111 0011 '''