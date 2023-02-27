# RECURSION:
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.

# Normal Function:

# def fun():
#     print('I am Function')
# fun()
# I am Function

# Using recursion(defined function can call itself)
def fun():
    print('I am function')
    fun()
fun()

# I am function
# I am function
# I am function
# I am function
# I am function
# I am function
# I am function
# I am function
# I am function

# RecursionError: maximum recursion depth exceeded while calling a Python object