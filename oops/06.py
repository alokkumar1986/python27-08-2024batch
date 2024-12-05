class Person:
    def __init__(self, name, age):
        self.xyz = name
        self.pqr = age
    def __str__(self):
        return f'X(xyz : {self.xyz}, pqr : [{self.pqr}])'

p = Person('Aptech', 20)
print(p)
