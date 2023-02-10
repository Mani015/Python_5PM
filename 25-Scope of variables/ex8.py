# end =

# for k in range(10):
#     print(k,end= ' ')
# 0 1 2 3 4 5 6 7 8 9

# FORMAT STRING:
# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# The format() method returns the formatted string.

# Syntax:
# string.format(value1, value2...)
a=10
b=20
# print('a value is :',a , 'b value is:',b, 'addtion of a,b:',a+b)


print(f'a value is {a} b value is {b} addition of {a+b}')
x= int(input('Enter one number:'))
for i in range(1,11):
    print(f'{x} * {i} = {x*i}')
# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# 10 * 6 = 60
# 10 * 7 = 70
# 10 * 8 = 80
# 10 * 9 = 90
# 10 * 10 = 100