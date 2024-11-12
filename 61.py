# def squares(length):
#     for n in range(length):
#         yield n ** 2

#num = squares(5)

num = (n**2 for n in range(5))
print(next(num))

print(next(num))

print(next(num))

print(next(num))

print(next(num))

#print(next(num))