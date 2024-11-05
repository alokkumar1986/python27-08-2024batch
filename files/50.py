'''
try:
 f= open('demo.txt', 'a')
except :
 print('File not found')
finally :
  f.write('\nHello Python')
  f.close()

try :
    f1 = open('demo.txt', 'r')
except: 
    print('file not found')
finally:
    txt = f1.read()
    f1.close()
    print(txt)
    count = 0
    for i in txt:
        if i=='\n':
          count=count+1
    print(count)

    #write a program to find number of lines in a file
    #write a program to find number of words in a file
'''

f2 = open('demo.txt', 'r')
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readline())
f2.close()
