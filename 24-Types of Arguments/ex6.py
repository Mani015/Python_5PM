# Arbitrary keyword arguments (**kwargs):
# We saw how to use *args. Now let’s see how to use the **kwargs argument.
# The **kwargs allow you to pass multiple keyword arguments to a function.
# Use the **kwargs if you want to handle named arguments in a function.
def KeywordArguments(**xyz):
    print(xyz)
KeywordArguments(a=1,b=2,c=3,d=4)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# KeywordArguments(a=1,b=2,c=3,b=4)
# KeywordArguments(a=1,b=2,c=3,b=4)
#                                  ^
# SyntaxError: keyword argument repeated: b


# def percentage(**kwargs):
#     sum = 0
#     for sub in kwargs:
#         # get argument name
#         sub_name = sub
#         # get argument value
#         sub_marks = kwargs[sub]
#         print(sub_name, "=", sub_marks)
#
# # pass multiple keyword arguments
# percentage(math=56, english=61, science=73)
