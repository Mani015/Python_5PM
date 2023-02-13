
G1 = 10
print(f'global var:{G1}')
# global var:10
def Outer():
    ENC =20
    print(f'enclosing variable:{ENC}')
    # enclosing variable:20
    print(f'global var:{G1}')
    # global var:10
    def inner():
        L1 = 30
        print(f'local variable:{L1}')
        # local variable:30
        print(f'enclosing variable:{ENC}')
        # enclosing variable:20
        print(f'global var:{G1}')
    #    global var:10
    # inner()
    print(f'enclosing variable:{ENC}')
    #     enclosing variable:20
    print(f'global var:{G1}')
#     global var:10
# Outer()
print(f'global var:{G1}')
# global var:10
# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
# global var:10
# enclosing variable:20
# global var:10
# local variable:30
# enclosing variable:20
# global var:10
# enclosing variable:20
# global var:10
# global var:10

x=[1,2,3,4,5]
print(f'before updating variable{x}')
def f1():
    y=6,7
    x.append(y)
    print(f'after updation:{x}')
f1()
print(x)
