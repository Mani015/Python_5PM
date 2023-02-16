# INBUILT_METHODS:
#map() function returns a map object(which is an iterator) of the results after applying the given function to
# each item of a given iterable (list, tuple etc.)
# Syntax :
# map(fun, iter)


def function(i):
    return i**2

k=[1,2,3,4,5,6,7]

x = map(function,k)
print(list(x))

# print(x)
# <map object at 0x000001BE4C699BB0>

