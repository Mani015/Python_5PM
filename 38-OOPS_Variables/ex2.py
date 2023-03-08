class Employee:
    classvariable_1 = 'amala'
    classvariable_2 = 'Rajesh'
    classvariable_3 = 'Arif'
    classvariable_4 = 'chaithu'
    classvariable_5 = 'swapna'
    classvariable_6 = 'venkatesh'

# calling classvariable

# print(Employee.classvariable_1)
# print(Employee.classvariable_2)
# print(Employee.classvariable_3)
# print(Employee.classvariable_4)
# print(Employee.classvariable_5)
# print(Employee.classvariable_6)
# amala
# Rajesh
# Arif
# chaithu
# swapna
# venkatesh

# using object

object1 = Employee()
# print(object1.classvariable_1)
# print(object1.classvariable_2)
# print(object1.classvariable_3)
# print(object1.classvariable_4)
# print(object1.classvariable_5)
# print(object1.classvariable_6)
# amala
# Rajesh
# Arif
# chaithu
# swapna
# venkatesh

# Updating classvariable name:
# Syntax:
# object.classvariable = newvalue

object1.classvariable_1 = 'vimala'
print(object1.classvariable_1)
print(object1.classvariable_2)
print(object1.classvariable_3)
print(object1.classvariable_4)
print(object1.classvariable_5)
print(object1.classvariable_6)
# vimala
# Rajesh
# Arif
# chaithu
# swapna
# venkatesh