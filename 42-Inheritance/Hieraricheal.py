# one parent class devrived more one child class is called hier

class Parent:
    def Behaviour1(self):
        print('This is parent Behaviour')

class Child1(Parent):
    def attitude1(self):
        print(' I am a child1 class,my parent behaviour belongs to mine')

class Child2(Parent):
    def attitude2(self):
        print(' I am a child2 class,my parent behaviour belongs to mine')


# Creating a object child1
ob1  = Child1()
ob1.attitude1()
ob1.Behaviour1()
#  I am a child1 class,my parent behaviour belongs to mine
# This is parent Behaviou
print()


# Creating object child2
ob2 = Child2()
ob2.attitude2()
ob2.Behaviour1()
#  I am a child2 class,my parent behaviour belongs to mine
# This is parent Behaviour






