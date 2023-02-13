

# def outerfucntion():
#     x1=20
#     print('Enclosing variable:',x1)
#     def innerfunction():
#         x2=60
#         print('local variable:',x2)
#     innerfunction()
#     print('local variable :',x2)
# outerfucntion()
# Enclosing variable: 20
# local variable: 60
# NameError: name 'x2' is not defined



def outerfucntion():
    x1=20
    print('Enclosing variable:',x1)
    def innerfunction():
        x2=60
        print('local variable:',x2)
    innerfunction()
    print('local variable :',x1)
outerfucntion()
print('enclosing variable:', x1)
# NameError: name 'x1' is not defined
# Enclosing variable: 20
# local variable: 60
# local variable : 20

