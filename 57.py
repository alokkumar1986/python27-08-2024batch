#reduce() : takes an iterator and returns a single value
from functools import reduce #reduce is not a built function

def myfun(a, b):
    return a+b 

rohit = [10, 26, 50, 54, 0, 2, 109]

total = reduce(myfun, rohit)
print(total)