'''def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))

'''
'''map() : it takes a sequesnce, it returns another sequesnce with same number of item
        it return eith same item or derived value from existing item '''
 
 
'''def myfun1(i):
  return i-2
  
        
li = [2, 4, 10, 23, 32, 98]

#newli = [0, 2, 8, 21, 30, 96]

newli = map(myfun1, li)

print(list(newli))
'''

#write a program to find the following list from another list

#input list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#output list: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def myfun2(y):
  return 2*y-1
 
inputli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputli = map(myfun2, inputli)
print(list(outputli))

