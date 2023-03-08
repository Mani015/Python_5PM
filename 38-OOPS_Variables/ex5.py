# Instance variables: If the value of a variable varies from object to object,
# then such variables are called instance variables.

# instance method is a method of object


class Student:
    def __init__(self,sname,snumber,saddress,smarks):
        self.name = sname
        # Instance variable
        self.number = snumber
        # Instance variable
        self.address = saddress
        # Instance variable
        self.marks = smarks

    def display(self):
        print(self.name)
        print(self.number)
        print(self.address)
        print(self.marks)
    def perumarchukooo(self,Newname):
        self.name = Newname
        print(self.name)
        print(self.number)
        print(self.address)
        print(self.marks)

new_Student = Student('chaithanya',101,'chennai',95)
new_Student.display()
print()
new_Student.perumarchukooo('Rajesh')
