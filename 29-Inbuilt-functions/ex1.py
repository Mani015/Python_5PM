print(abs(-20))

g1 = 100
def f1():
    enclosing = 10
    print(f'enclosing variable:{enclosing}')
    def f2():
        local = 20
        print(f'local variable:{local}')
        print('the sum of :',sum([enclosing+local+g1]))
        print('the maximu value:',max([enclosing,local,g1]))
    f2()
f1()