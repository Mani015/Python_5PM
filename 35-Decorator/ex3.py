





def fun1(n):
    def fun2(func):
        global i
        for i in range(n):
            func()
    return fun2
# @fun1(10)
# def fun3():
#     print('loop:',i)

# print(fun3())
# ob = fun3()
# print(ob())


def decorator(func):
    def dec():
        num = func()
        return num*num
    return dec
@decorator
def outer():
    return 10

# ob=decorator(outer)
# print(ob())

print(outer())

@decorator
def next():
    return 20

print(next())










