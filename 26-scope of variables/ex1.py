# ENCLOSING VARIAVBLE:
# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.
# If the local scope is an inner or nested function,
# then the enclosing scope is the scope of the outer or enclosing function.


def Outer():
    
    def Inner():
        x=10
        print(x)
    Inner()
Outer()
