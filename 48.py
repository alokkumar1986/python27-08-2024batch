try :
 f = open('demo.txt', 'a')
except :
 print('There is already demo.txt in the directory')

f.write('Hello World4')

# print(f.read())

f.close()


f1 = open('demo.txt', 'r')
print(f1.read())
f1.close()



'''readline()
read(2)


Regular expression in python'''