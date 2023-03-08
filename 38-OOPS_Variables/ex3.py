# updating class/static variable name using [classname]
class Employee:
    classvariable_1 = 'amala'
    classvariable_2 = 'Rajesh'
    classvariable_3 = 'Arif'
    classvariable_4 = 'chaithu'
    classvariable_5 = 'swapna'
    classvariable_6 = 'venkatesh'

ob1 = Employee()
ob2= Employee()

# Sytax:
# classname.staticvariable  = New varaible

Employee.classvariable_1 = 'priyanka'
print(ob1.classvariable_1)
print(ob2.classvariable_1)