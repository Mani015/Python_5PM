

# g1=20
# print('global variable;',g1)
# def Func():
#     g11=30
#     print('lovcal variable:',g11)
#     print('global variable:',g1)
# Func()
# print('global variable:',g1)

# global variable; 20
# lovcal variable: 30
# global variable: 20
# global variable: 20

g1=20
print('global variable;',g1)
def Func():
    g1=30
    print('lovcal variable:',g1)
    print('global variable:',g1)
Func()
print('global variable:',g1)
# global variable; 20
# lovcal variable: 30
# global variable: 30
# global variable: 20