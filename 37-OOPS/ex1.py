
class Student:
    x1=10
    x2=20

obj1=Student()
obj2=Student()
print(obj1.x1)
print(obj2.x1)
print()
# obj2.x1=100
print(obj2.x1)
print()
print(obj1.x1)
print()
# Updating attribute value using class name:

# Sy:classname.attributename =  Newvalue

Student.x1='arif'
print(obj1.x1)
print(obj2.x1)


# 10
# 10
#
# 10
#
# 10
#
# arif
# arif