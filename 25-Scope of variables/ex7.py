# How TO acesess global variabel inside  a function with the same variable name(global & local):

g1=20
# print('global variable;',g1)
def Func():
    g1=30
    # print('lovcal variable:',g1)
    # print('global variable:',globals()['g1'])
Func()
# global variable; 20
# lovcal variable: 30
# global variable: 20

# ADDtion of scope variables

g1=20
def outerfucntion():
    l1 = 30
    print('locla variable:',l1)
    k1 = l1+g1
    print('k1 is local variable:',k1)
outerfucntion()
# locla variable: 30
# k1 is local variable: 50
