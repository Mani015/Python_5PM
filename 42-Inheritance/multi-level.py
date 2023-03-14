# Multilevel -inheritance


class Grand_Parent:
    def method1(self):
        print('this is  grand parent property')

class Parent(Grand_Parent):
    def method2(self):
        print('this is parent property')

class Child(Parent):
    def method3(self):
        print('this is child property')

obj=Child()
obj.method1()
# this is  grand parent property
obj.method2()
# this is parent property
obj.method3()
# this is child property
