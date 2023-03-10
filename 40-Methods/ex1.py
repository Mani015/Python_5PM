
# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.


class Vegitables:
    Tomoto = 'Red colour'
    def veg1(self):
        print('I am instance method')
    @classmethod
    def classmethod(cls):
        print(Vegitables.Tomoto)

object = Vegitables()
# using class name:

# Vegitables.classmethod()
# Red colour

# using parameter object
# Vegitables.classmethod(object)
# TypeError: classmethod() takes 1 positional argument but 2 were given

