#map() : 
#filter() : takes an iterator and return another iterator having same or less number of item

'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#nli = [2, 4, 6, 8, 10]

def myfun(i):
    if i%2==0 :
        return i
nli = filter(myfun, li)
print(list(nli))

'''


'''
nli = [6]
     [1, 2, 4, 7, 6, 12, 8, 15, 13, 18]

1 = 1 = 1
2 = 1, 2 =3
3 = 1, 3 = 4
4 = 1, 2, 4 = 7
5 = 1, 5 = 6
6 = 1, 2, 3, 6 = 12
7 = 1, 7 = 8
8 = 1, 2, 4, 8 = 15
9 = 1, 3, 9 = 13
10 = 1, 2, 5, 10 = 18
'''
'''
def myfun1(n) :
    sum = 0
    for i in range(1, n+1):
        if n%i==0:
          sum= sum +i
    if sum/n ==2:
        return n
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nli = filter(myfun1, li)
print(list(nli))
'''
def myfun1(n) :
    if n/2 == 3:
        return n
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nli = filter(myfun1, li)
print(list(nli))