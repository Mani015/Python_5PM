# Usinh inheritance
class School:
    def __init__(self,schoolname,schooladdress,schoolpincode):
        self.name = schoolname
        self.address = schooladdress
        self.pincode = schoolpincode

    # def view(self):
    #     print(f'parent class {self.name},{self.address},{self.pincode}')


class Student1(School):
    def __init__(self,schoolname,schooladdress,schoolpincode,studentname,studentrollno):
        School.__init__(self,schoolname,schooladdress,schoolpincode)
        self.sname = studentname
        self.roll = studentrollno

    def display(self):
        print(f'child class is :,{self.name},{self.address},{self.pincode},{self.sname},{self.roll}')

obj1 = Student1('Narayana','tirupathi',533004,'chaithanya',101)
obj1.display()
# child class is :,Narayana,tirupathi,533004,chaithanya,101

