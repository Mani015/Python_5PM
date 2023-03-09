# Define Instance Method
# Instance variables are not shared between objects. Instead, every object has its copy of the instance attribute.
# Using the instance method, we can access or modify the calling object’s attributes.
#
# Instance methods are defined inside a class, and it is pretty similar to defining a regular function.


# Use the def keyword to define an instance method in Python.
# Use self as the first parameter in the instance method when defining it. The self parameter refers to the current object.
# Using the self parameter to access or modify the current object attributes.
# You may use a variable named differently for self, but it is discouraged since self is the recommended convention in Python.


class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()
print()
# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()