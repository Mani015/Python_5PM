# a=20
# a=20
# a=a
# a=30
# print(a)
# print(a*2)
# Scope  of Variables:
# 1).local scope
# 2).Global Scope
# 3).Enclosed Scope
# 4).Built-in scope

# 1).local scope:In Python, the scope of a variable is an area where a variable is declared.
# It is called the variable’s local scope.
# We cannot access the local variables from outside of the function.
# Because the scope is local, those variables are not visible from the outside of the function.

def Swapna():
    a=10
    # local variable 'a'
    print('local variable:',a)
Swapna()
# local variable: 10

# Note: The inner function does have access to the outer function’s local scope.