# Indirect Recursion

def f1():
    print('Fucntion 1')
    f2()
def f2():
    print('fucntion 2')
    f1()

def f3():
    print('fucntion 3')
    f2()

f3()

# fucntion 3
# Fucntion 1
# fucntion 2