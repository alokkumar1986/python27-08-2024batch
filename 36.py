#dict
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
set = { 1, 2, 3, 4, 5}

dict = {
    'name': "Ardhendu",
    'age' : 29,
    'profession': 'Graduate Engineer'
}


d = {
    'name': "Ardhendu",
    'age' : 29,
    'profession': 'Graduate Engineer',
}

'''
'name'--> key
"Ardhendu" --> Value

d['name']   # Ardhendu
'''

print(type(d))
print(d)
print(d['name'])
print(d['age'])
print(d['profession'])


#Duplicate key is not allowed
#Duplicate values are allowed

'''
creation of dict
1) d = {}
2) d = dict()

'''

k = {}
#l = dict()
print(type(k))
#print(type(l))


m = {
    100:'karthi',
    200:'sahasra',
    300:'sri'
    }

print(m[300]) #sri
print(m[200] )#sahasra

print(m[100])

print(m)

m[100] = 'Karthik'  #dict is mutable

print(m[100])

print(m)



z={'a':'apple' ,'b':'banana', 'c':'cat'} 
if 'c' in z:  # has_key()
              # in : membership operator
 print(z['c'])
else :
 print('dict z has no key z')
 
'''
for i in z:
    print(i)  #will print keys
for i in z:
    print(z[i])   #will print values at the key
'''  
    
#Add object to a dict
    
z['d'] = 'donkey'
print(z)

#update a dict
z['a'] = 'arm'
print(z)


#delete an object from dict
del z['d']
print(z)
#del z['k']