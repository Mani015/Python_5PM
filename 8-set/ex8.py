p1={'chaithanya', 'rajesh', 'priya', 'arif'}
print(p1)
# {'priya', 'arif', 'chaithanya', 'rajesh'}

x2=p1.copy()
print(x2)
# {'priya', 'arif', 'rajesh', 'chaithanya'}

x3=x2.copy()
print(x3)
# {'rajesh', 'chaithanya', 'priya', 'arif'}
x3.update({'python','smile'})
# print(x3)
# {'python', 'smile', 'rajesh', 'chaithanya', 'arif', 'priya'}



