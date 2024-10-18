d = {
    
    100 : "Ram",
    200 : "Chandra",
    300 : "Sahasra"
}

print(d)
print(d[100])
d['400']= 'Aptech'
print(d)

d['200'] = 'Karthik'  #dict doesnt allow duplicate
print(d) 

del d['400']
print(d)

for i in d:
    #print(i)
    print(d[i])
    
##### Methods ######
#dict() # We create dictionary
#e = dict()

#len() #It counts the number of items
print(len(d))

#clear()  #It clears all items in a dict
#d.clear()
#print(d)

#get() # It gives a value in a specified key
print(d['200'])
print(d.get(200))

#print(d[500])
print(d.get(500))

#both gives same value if dict is not changed
#Otherwise 1st one will give latest value whereas 2nd one will give original value
#If key is not available then 1st one gives keyError where 2nd one won't give error and returns None. 

print(d.get(500, 'Ravan'))

e = {
    'Potato' : 250,
    'Tomato' : 500,
    'Salt' : 100,
    'Rice' : 1580,
    'Dal' : 2575
}

sum = e.get('Potato', 0)+ e.get('Tomato', 0) + e.get('Salt',0) + e.get('Rice', 0) + e.get('Dal', 0) + e.get('Oil', 0) 

print(sum)

#pop() #removes an item from dict and returns the dict
print(d)
d.pop(200) 
print(d)


#popitem() #returns last item from dict and removes that item from dict
s = { 100: "Sachin", 200 : "Saurav", 300 : "Sehwag"}
print(s)
d = s.popitem()
print(d) #{ 300: 'Sehwag' }
print(s) #{100 : "Sachin", 200 : "Saurav"}


#keys() # returns a list of keys in a dict
di = { 100: "Sachin", 200 : "Saurav", 300 : "Sehwag"}
l = di.keys()
print(l)
print(type(l))
for i in l:
    print(i)
    
#values() # returns a list of values in a dict
div = { 100: "Sachin", 200 : "Saurav", 300 : "Sehwag"}
lv = div.values()
print(lv)
print(type(lv))
for i in lv:
    print(i)
    
#items #returns all the items in the form of tuple in a dict
ditm = { 100: "Sachin", 200 : "Saurav", 300 : "Sehwag"}
litm = ditm.items()
print(litm) # dict_items([(100, "Sachin"), (200, "Saurav"), (300, "Sehwag")])
print(type(litm))
for i in litm:
    print(i) #(100, "Sachin")
             #(200, "Saurav")
             #(300, "Sehwag")
             

#copy() #It clones a dict to another
d = {}
d1 = d.copy()

#setdefault() #it sets deafult value in dict 
'''d.setdefault(k, v)
k = Key,
v = Value'''

#update() # it adds all items from a dict to another dict
z={100:"karthi",200:"saha",300:"sri"} 
z1 ={'a':'apple', 'b':'banana'}
z1.update(z)
print(z)
print(z1)