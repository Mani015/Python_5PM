
# def func(amala):
#     return amala+amala
# k = map(func,{1,2,3,4,5,6,7,8})
# print(tuple(k))
# (2, 4, 6, 8, 10, 12, 14, 16)


def func(chaitu):
    return chaitu**2


value = map(func,range(1,10))
# print(list(value))

# using lambda map function

# print(map((lambda n : n**2),[1,2,3,44,55,66,77,88,99,20]))
# <map object at 0x0000014360676F10>

arif = [1,2,3,44,55,66,77,88,99,20]
print(tuple(map((lambda n : n**2),arif)))
