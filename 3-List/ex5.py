# List is mutable datatype :a mutable object is an object whose state can be modified after it is defined.
# append()	Adds an element at the end of the list
a=[1,2,3,4,5,6,7,8,9]
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# syntax:variable name .mehtod name
a.append('python')
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'python']


a.append('values')
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'python', 'values']

a.append(5+6j)
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'python', 'values', (5+6j)]

a.append(10,1)
print(a)
# TypeError: list.append() takes exactly one argument (2 given)
