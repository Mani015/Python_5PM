# Multiple Inheritance:

class Parent1:
    def property1(self):
        print('This is parent1 class')
class Parent2:
    def property2(self):
        print('This is parent2 class')

class Child(Parent1,Parent2):
    def property3(self):
        print('This is child class')


Obj1 = Child()
Obj1.property1()
# This is parent1 class
Obj1.property2()
# This is parent2 class
Obj1.property3()
# This is child class