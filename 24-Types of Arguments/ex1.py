# Types of function arguments
# Default Arguments
# Keyword Arguments
# Positional Arguments
# Variable-length arguments
# Arbitrary positional arguments (*args)
# Arbitrary keyword arguments (**kwargs)




# Positional Arguments:
# Positional arguments are those arguments where values get assigned to the arguments by their position when the function is called.
# For example, the 1st positional argument must be 1st when the function is called.
# The 2nd positional argument needs to be 2nd when the function is called, etc

def F1(x,y):
    print(x,y)

# F1(10)
# TypeError: F1() missing 1 required positional argument: 'y'

def PositionalArguments(x,y):
    print(x)
    print(y)
PositionalArguments(2,3)
# 2
# 3