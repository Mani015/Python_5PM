# Single Inheritance
# In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.



class Parent:
    def method1(self):
        print('I am parent class')

class Child:
    def method2(self):
        print('I am a child class')



# ob1 = Parent()
# ob1.method1()
# I am parent class
# ob1.method2()
# AttributeError: 'Parent' object has no attribute 'method2'

ob2 = Child()
ob2.method2()
# I am a child class
ob2.method1()
# AttributeError: 'Child' object has no attribute 'method1'
