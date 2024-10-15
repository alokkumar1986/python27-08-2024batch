# frozenset
#frozenset is same as set but it is immutable
#it cannot grow

#varibale_name = frozenset({item1, item2, item3... })

b = {1, 3, 6}
a = frozenset(b)
print(type(b))
print(type(a))

b.add(12)
print(b)

a.add(12)

#frozenset does not support index and slicing like set

#forzenset does not allow duplicate like set