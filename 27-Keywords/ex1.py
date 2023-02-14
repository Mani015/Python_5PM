# GLOBAL KEYWORD:
# In Python, the global keyword allows us to modify the variable outside of the current scope.
#
# It is used to create a global variable and make changes to the variable in a local context.
#
# Before we learn about the global keyword, make sure you have got some basics of Python Variable Scope.
x=10
print(f'global variable:{x}')
def func():
    global x
    x=20
    print(f'local variable:{x}')
    print(globals()['x'])
func()
print(f'global v:{x}')
# global variable:10
# local variable:20
# 20
# global v:20