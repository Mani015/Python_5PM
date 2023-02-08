# Keyword Arguments
# Usually, at the time of the function call, values get assigned to the arguments according to their position.
# So we must pass values in the same sequence defined in a function definition.
def Keyword(x,y,z):
    print(f'x is {x}')
    print(f'y is {y}')
    print(f'z is {z}')

# Keyword(x=10,y=20,z=30)
# x is 10
# y is 20
# z is 30
Keyword(y=10,z=20,x=30)
# x is 30
# y is 10
# z is 20

