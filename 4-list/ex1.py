# Extend()
# extend()	Adds each element of the iterable to the end of the List
l=[1,2,3,'python', 'java',12.0,True]
# print(l)
# [1, 2, 3, 'python', 'java', 12.0, True]

l.extend([11,22,00,'html'])
# print(l)
# [1, 2, 3, 'python', 'java', 12.0, True, 11, 22, 0, 'html']


l2=['apple','banana', 'orange', 'grapes', 'pappaya']
print(l2)
# ['apple', 'banana', 'orange', 'grapes', 'pappaya']

l2.extend(['mango', 'pineapple', 'kiwi', 'dragon'])
print(l2)
# ['apple', 'banana', 'orange', 'grapes', 'pappaya', 'mango', 'pineapple', 'kiwi', 'dragon']

