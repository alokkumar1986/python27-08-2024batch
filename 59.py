#generators : It is a function which has at least a yield inside 
def fun():
    print('1')
    print('10')
    print('100')
    print('1000')
    print('10000')
    print('100000')
    yield 1
    print('1000000')
    yield 2
    print('10000000')
    print('100000000')
    print('1000000000')
fun()
