def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

message = greeting()
result = next(message)
print(result)

result = next(message)
print(result)

result = next(message)
print(result)

result = next(message)
print(result)  #stopIteration