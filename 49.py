import os

try :
    f = open('C:/tutorial/demo.txt', 'r')
    print(f.readline())
    f.close()

    f1 = open('C:/tutorial/demo.txt', 'r')
    print(f1.read(100))
    f1.close()
except :
    print('File not found')

#readline() : reads firstline of the file
#read() :reads all content of the file
#read(3) : reads first 3 characters from the file

if os.path.exists('C:/tutorial/demo.txt'):
    os.remove('C:/tutorial/demo.txt')
else :
    print('File not found')

os.rmdir('C:/tutorial')

#remove() : delete a file from the directory
#rmdir() : delete a folder from the directory