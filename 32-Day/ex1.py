i=0
while i<9:
    Student_Name = input('Enter Student name:')
    s1 = int(input('Enter s1 marks:'))
    s2 = int(input('Enter s1 marks:'))
    s3 = int(input('Enter s1 marks:'))
    s4 = int(input('Enter s1 marks:'))
    s5 = int(input('Enter s1 marks:'))
    s6 = int(input('Enter s1 marks:'))

    Total_Subjectmarks = s1 + s2 + s3 + s4 + s5 + s6

    print(f'{Student_Name} total marks :{Total_Subjectmarks}')

    percentage = (Total_Subjectmarks / 600) * 100

    print(f'Total percentage of student:{percentage}')

    print('All the best')
    i=i+1
print('loop completed')
