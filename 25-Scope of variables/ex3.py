
def localscope_1():
    variable_1=20
    variable_2=30
    print(variable_1)
    print(variable_2)

def localvariable_2():
    variable_3 = 'python'
    variable_4 = 'developer'
    print(variable_3)
    print(variable_4)
    print(variable_2)


# localscope_1()
localvariable_2()
# NameError: name 'variable_2' is not defined
