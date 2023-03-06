# How  to creating object


class Oops_1:
    obj='Instance of a class'
    cla = 'python'

object1 = Oops_1()
print(object1)
# <__main__.Oops_1 object at 0x000001AE01553FD0>

# Syntax:
# objectname.attributename
print(object1.obj)
print(object1.cla)

print('----------------------------------------------------------------------------')

object2=Oops_1()
# print(object2.obj,object2.cla)
# TO updating the attribute value using object
# Syn:
# objectname.attributename = newvalue
object2.cla = 'java'
print(object2.cla)
print('------------------------')
print(object1.cla)

# def f1():
#     print('hello function')
#     return 'good bye function'
#
# ob = f1()
# print(ob)
# l1  = [1,2,3,4,5]
# l2 = l1
#
# print(l2)