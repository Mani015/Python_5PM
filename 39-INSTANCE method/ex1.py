

class Institute:
    Institute_Name = 'GRK TRAINING, Marthahalli'
    def __init__(pen,student_name,Student_address,Student_number,Student_technology):
        pen.name = student_name
        pen.address = Student_address
        pen.number = Student_number
        pen.techno = Student_technology


ob1 = Institute('Naveen kumar','Hyd',123654,'Python developer')
ob2 = Institute('Amala','tirupathi',12321,'Java Developer')
ob3 = Institute('priyanka','kakinada',11223344,'Devops')
ob4 = Institute('Arif','mumbai',12365478,'AWS')
ob5 = Institute('Swapna priya','madanapalli',23564,'Dot net')
ob6 = Institute('chaitu','andhra pradesh',2012064,'Data Science')

Institute.Institute_Name = 'J-Spider'

Rajesh = [ob1,ob2,ob3,ob4,ob5,ob6]

for i in [ob1,ob2,ob3,ob4,ob5,ob6]:
    print(i.name)
    print(i.address)
    print(i.number)
    print(i.Institute_Name)
    print(i.techno)
    print('<-------------------------------->')

