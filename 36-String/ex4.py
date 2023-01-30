
a='python developer'

# print(a.upper())
# PYTHON DEVELOPER
# print(a.lower())
# python developer

# print(a.capitalize())
# Python developer
# print(a.isupper())
# Fasle
# print(a.islower())
# True

import keyword

a=keyword.kwlist
# for k in a:
#     print(k)
# print(len(k))

# print(len(a))

f=[-22,-5,1,0,2,3,-2,-4,-5,-6,11,22,33,44]
i=0
for k in f:
    if k>=0:
        k+=2
        i+=1
        print(k)
print('loop iteration:',i)