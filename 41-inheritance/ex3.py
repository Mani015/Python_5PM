
# Single -Inheritance

class Parent:
    def method1(self):
        print('I am parent class')

class Child(Parent):
    def method2(self):
        print('I am a child class')


ob1 = Child()
ob1.method1()
# I am parent class
ob1.method2()
# I am a child class