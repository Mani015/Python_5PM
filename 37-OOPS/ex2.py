# __init__
# The __init__ function is called every time an object is created from a class.
# The __init__ method lets the class initialize the object's attributes and serves no other purpose.
# It is only used within classes.

# when an object of the class is created. Like methods,
# a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation.
# It is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.



# class Classname:
#     def __init__(self,para1,para2,para3,para4.......paraN):
#      self.attributeName = paramether1
#     object.attribute1 = para1
#     object.attribute2 = para2


# calling class
# Classname

class Bike:
    def __init__(self,Bike_color,Bike_Cost,Bike_Brand,Bike_milege,Bike_Model):
        self.color = Bike_color
        self.cost = Bike_Cost
        self.brand = Bike_Brand
        self.milege = Bike_milege
        self.model = Bike_Model
        print(self.model,self.brand,self.cost,self.milege,self.color)

# TO calling init method without object:

# Bike()
# TypeError: __init__() missing 5 required positional arguments: 'Bike_color', 'Bike_Cost', 'Bike_Brand', 'Bike_milege', and 'Bike_Model'

Bike('Black',100000,'Bmw',60,'B6model')
# B6model Bmw 100000 60 Black




# def f2(x,y):
#     print(x,y)
# f2()