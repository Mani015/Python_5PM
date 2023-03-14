class Parent1:
    def property1(self):
        print('This is parent1 class')
class Parent2:
    def property1(self):
        print('This is parent2 class')

class Child(Parent1,Parent2):
    def property1(self):
        print('This is child class')


ob1=Child()
ob1.property1()
# This is parent1 class
ob1.property1()
# This is parent1 class
