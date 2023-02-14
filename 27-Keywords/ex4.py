# NONLOCAL KEY WORD:


g1=10
print(f'global va:{g1}')
def f1():
    g1=20
    print(f'enclosing v:{g1}')
    def f2():

        nonlocal g1
        g1=30
        print('locla variable:',g1)

    f2()
    print(f'enclosing variable:{g1}')
f1()
print(f'global va:{g1}')
# global va:10
# enclosing v:20
# locla variable: 30
# enclosing variable:30
# global va:10
