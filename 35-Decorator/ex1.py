# A decorator is a higer ordr function is a function that operats on other function, either as its arguments or by returning a function


# Without decorator

def fun1():
    print('Functon')

def fun2():
    return fun1()

# fun2()
# Function


def f1(n):
    return 'squre of n :',n**2

def f2(n):
    return 'cube of n:',n**3

def f3(fun):
    return fun

# print(f3(f1(5)))


def c1(x):
    return x**2
def c2(y):
    return y**3
def c3(x1,y1):
    return x1,y1

print(c3(c1(10),c2(10)))

# (100, 1000)









