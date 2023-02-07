# RETURN IN FUNCTION:
# A return statement is used to end the execution of the function call and “returns” the result
# (value of the expression following the return keyword) to the caller.
# The statements after the return statements are not executed.
# If the return statement is without any expression, then the special value None is returned.
# A return statement is overall used to invoke a function so that the passed statements can be executed.

# def Sunny():
#     print('basic fucntion')
# Sunny()
# basic fucntion

# def Python(a,b):
#     print(a,b)
# Python()
# TypeError: Python() missing 2 required positional arguments: 'a' and 'b'

#
def New_Function(a,b):
    print('To display a value and b value:')
    print(a,
          b)
# With out return keyword calling using print fucntion
print(New_Function(10,20))
# print()
# To display a value and b value:
# 10 20
# None
