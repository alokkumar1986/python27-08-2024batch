rec={} 

n=int(input("Enter number of students: ")) 
i=1 
while i <= n: 
    name=input("Enter Student Name: ") 
    marks=input("Enter % of Marks of Student: ") 
    rec[name]=marks 
    i=i+1 
print("Name of Student","\t","% of Marks") 
for x in rec: 
 print("\t", x,"\t",rec[x])   
#print(rec)

'''
Name of Student     % of Marks
  Ardhendu            88
  Akash               89
'''  

'''
print('I am a stu\tdent of  \n aptech')

print('Hello World \r Bye Bye')
#Bye Byeorld

print('hello\b world ') #hell world

print("hello' world ") # hello' world
print('hello" world ') # hello" world

print('hello/ world ') # hello" world

'''