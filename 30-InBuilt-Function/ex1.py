# Filter

def evennumber(i):
    if i%2==0:
        return i
l1=[11,22,33,44,55,66,77,88]
# Syn:
# filter(functionname,iterable)

x1 = filter(evennumber,l1)
# print(x1)
# <filter object at 0x00000166AF880BB0>

# print(set(x1))
# print(list(x1))
# [22, 44, 66, 88]



def Consonants(c):
    if c  not in 'aeiou':
        return c
x='abcdefghijklmnopqrstuvwxyz'

con = filter(Consonants, x)
print(tuple(con))
# ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
