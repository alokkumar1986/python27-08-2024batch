#zip(), zip(*)
'''
names = ['Ram', 'Hari', 'Jadu', 'Sankar']
ages = [20, 32, 30]

for student in zip(names, ages):
    print(student)
'''

students = (('Ram', 20),('Hari', 32), ('Jadu', 30))
names, ages = zip(*students)
print(names)
print(ages)