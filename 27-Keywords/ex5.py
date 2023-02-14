# nl=10
# print(f'global va:{nl}')
# def f1():
#     global nl
#
#     g1=20
#
#     print(f'enclosing v:{g1}')
#     def f2():
#         nonlocal g1
#         g1=30
#         print('locla variable:',g1)
#     f2()
#     print(f'enclosing variable:{g1}')
#     # nl = g1 + 10
# f1()
# print(f'global va:{nl}')

# global va:10
# enclosing v:20
# locla variable: 30
# enclosing variable:30
# global va:40


nl = 10
print(f'global va:{nl}')


def f1():
    global nl

    g1 = 20
    print(f'enclosing v:{g1}')


    def f2():
        nonlocal g1
        g1 = 30
        print('locla variable:', g1)

    f2()
    print(f'enclosing variable:{g1}')
    # nl = g1 + 10
    nl = g1


f1()
print('global;',nl)
