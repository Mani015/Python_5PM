x1={'chaithanya','rajesh','priya','arif'}
# print(x1)
# {'arif', 'chaithanya', 'rajesh', 'priya'}


x1.add('python')
# print(x1)
# {'arif', 'python', 'chaithanya', 'priya', 'rajesh'}

x1.add('dell')
# print(x1)
# {'chaithanya', 'python', 'arif', 'dell', 'priya', 'rajesh'}


x1.add('acer','hp')
print(x1)
# TypeError: set.add() takes exactly one argument (2 given)


