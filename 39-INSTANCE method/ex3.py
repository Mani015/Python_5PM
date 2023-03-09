
class Employee:
    def __init__(self,empname,empage):
        self.name = empname
        self.age = empage

    def show(self):
        print('empname :',self.name, 'empage:',self.age)
    def update(self,emp_Newname, emp_age):
        self.name = emp_Newname
        self.age = emp_age
        print(self.age,
              self.name)
    # TO deleting the instance attribute
    def Delete(self):
        del self.name
        print(self.name)


ob=Employee('varun',13)
ob.show()
ob.Delete()
ob1 = Employee('charan',20)
ob1.show()