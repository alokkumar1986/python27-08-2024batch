#bytes and bytearray  

#both are list 
# allowed values 0 to 255
# bytes is immutable
# bytearray is mutable

b = bytes([10, 20, 30, 40]) 
print(type(b))
c = bytearray([10, 20, 30, 40, 255]) 
print(type(c))

print(b[0])
print(c[0])

#b[0] = 100
c[0] = 100