
# g = 10
# print('global variable:',g)
#
# def Function():
#     print('global variable:',g)
# Function()
# print('global variable:',g)
# global variable: 10
# global variable: 10
# global variable: 10


g1 = 'Global variable'
print('global v:',g1)
def fun1():
    print('global v:', g1)
    l1='local variable'
    print(l1)
def fun2():
    print('global v:', g1)
fun1()
print('global v:',g1)
fun2()
print('global v:',g1)
# global v: Global variable
# global v: Global variable
# local variable
# global v: Global variable
# global v: Global variable
# global v: Global variable

