
# def outer():
#     x1=20
#     print('variable of x1 is:',x1)
#     def inner():
#         x2=30
#         print('variable of x2:',x2)
#     inner()
# outer()
# variable of x1 is: 20
# variable of x2: 30


def outer():
    x1=20
    print('variable of x1 is:',x1)
    def inner():
        x2=30
        print('variable of x2:',x2)
        print('variable of x1 is:', x1)
    inner()
    print('variable of x1 is:', x1)
outer()
# variable of x1 is: 20
# variable of x2: 30
# variable of x1 is: 20
# variable of x1 is: 20
