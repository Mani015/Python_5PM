# User input:
x=int(input('Enter one number:'))
print('x value is:',x)

if x==int(input('ENter seocnd number:')):
    print('condition 1 is satisfied')
    if int(input('Enter 3rd number:'))==20:
        print('condtion 2 is satisfied')
    else:
        print('condition is failed')
else:
    print('Totally unsatisfied')
