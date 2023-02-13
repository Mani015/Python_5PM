

g1 = 'chaithanya'
print('global name is :',g1)

def inner():
    l1 = 'rajesh'
    print(f'local name is: {l1}')
    print(f'global name is :{g1}')
    c = g1 + l1
    print(f'c is local variable is :{c}')
inner()
print(f'global variable is {g1}')
# global name is : chaithanya
# local name is: rajesh
# global name is :chaithanya
# c is local variable is :chaithanyarajesh
# global variable is chaithanya
print(f'c is local variable is :{c}')
# NameError: name 'c' is not defined

