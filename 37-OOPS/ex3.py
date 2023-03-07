# Using object


# class Bike:
#     def __init__(self,Bike_color,Bike_Cost,Bike_Brand,Bike_milege,Bike_Model):
#         self.color = Bike_color
#         self.cost = Bike_Cost
#         self.brand = Bike_Brand
#         self.milege = Bike_milege
#         self.model = Bike_Model
#
# object1 = Bike('Blue',200000,'java',40,'400cc')
# print(object1.color)
# print(object1.cost)
# print(object1.brand)
# print(object1.milege)
# print(object1.model)
# Blue
# 200000
# java
# 40
# 400cc


class Bike:
    def __init__(self,Bike_color,Bike_Cost,Bike_Brand,Bike_milege,Bike_Model):
        self.color = Bike_color
        self.cost = Bike_Cost
        self.brand = Bike_Brand
        self.milege = Bike_milege
        self.model = Bike_Model
    def Display(self):
        print(self.color)
        print(self.model)
        print(self.milege)
        print(self.cost)
        print(self.brand)

object1 = Bike('Blue',200000,'java',40,'400cc')

# Function calling using object
# Syn: objectName.methodName()

# object1.kanipinchu()

Bike.Display(object1)


# Blue
# 400cc
# 40
# 200000
# java


object2=Bike('red',90000,'glamour',60,'afas')
object2.Display()







