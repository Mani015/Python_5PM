x=10
# print(f'global variable:{x}')
def func():
    global x
    x=20
    print(f'local variable:{x}')
    # print(globals()['x'])
# func()
# print(f'global v:{x}')


en='Arif'
def outer():
    global en
    en = 'chaithanya'
    print(en)
    def inner():
        l1 = 'swapna'
        print(l1)
        print(en)
        print(en)
    inner()
    print(en, en)
outer()
print(en)
# chaithanya
# swapna
# chaithanya
# chaithanya
# chaithanya chaithanya
# chaithanya