#Arbitary Arguments

'''def my_function(*kids):
    #print("The youngest child is "+kids[1])
    for i in kids:
        print(i)

my_function('Ram', 'Hari', 'Jaga', 'Shyam', 'Jenamani', 'Jagriti')
'''


#When a called function has a argument like '*argumentname', then your calling function can have any number of arguments
# This is called arbitary arguments

# arbitary argument is same as passing a list to calling function
'''
def my_function(kids):
    #print("The youngest child is "+kids[1])
    for i in kids:
        print(i)

l = ['Ram', 'Hari', 'Jaga', 'Shyam', 'Jenamani', 'Jagriti']
my_function(l)
'''
'''
return statement : in called function
pass statement : in called function

'''

def my_fn():
    pass
my_fn()