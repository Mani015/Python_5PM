# with out using inheritance
class School:
    def __init__(self,schoolname,schooladdress,schoolpincode):
        self.name = schoolname
        self.address = schooladdress
        self.pincode = schoolpincode

    def view(self):
        print(f'parent class {self.name},{self.address},{self.pincode}')
class Student:
    def __init__(self,studentname, studentclass, studentrollno):
        self.sname = studentname
        self.sclass = studentclass
        self.roll = studentrollno
    def display(self):
        print(f'next class--->{self.sname},{self.sclass},{self.roll}')

ob1 = School('Narayana','Tirupathi',516302)
ob1.view()
# parent class Narayana,Tirupathi,516302

ob2 = Student('chaitanya','10th',101)
ob2.display()
# next class--->chaitanya,10th,101
