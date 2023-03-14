# class Parent1:
#     pass
# class Parent2:
#     def property1(self):
#         print('This is parent2 class')
#
# class Child(Parent1,Parent2):
#    pass
#
#
#
# ob1=Child()
# ob1.property1()
# This is parent2 class


# --------------------------------------------------------------------------------------------------------------------------

class Parent1:
   def property1(self):
       print('this is parent 1 class')
class Parent2:
    def property2(self):
        print('This is parent2 class')

class Child(Parent1,Parent2):
    def property3(self):
        print('this is child class')


ob1=Child()
ob1.property1()
# this is parent 1 class
ob1.property2()
# This is parent2 class
ob1.property3()
#this is child class