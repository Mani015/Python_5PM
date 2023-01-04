x1=int(input('Enter your 1st number='))

print(type(x1))

x2=int(input('Enter 2nd number='))

print(type(x2))
print('addition of x1 and x2:',x1+x2)
print('subtraction of x1 and x2=',x1-x2)

#
# Enter your 1st number=12
# <class 'int'>
# Enter 2nd number=3.0
# Traceback (most recent call last):
#   File "C:\Users\DELL\PycharmProjects\5PM\11-day\ex7.py", line 5, in <module>
#     x2=int(input('Enter 2nd number='))
# ValueError: invalid literal for int() with base 10: '3.0'