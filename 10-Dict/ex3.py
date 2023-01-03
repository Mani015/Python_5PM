
# dc1={'state':'capital',1:'a',2:'b',3:'c',4:'d',5:'e','man':'women','brother':'sister'}
# print('before dictionary:',dc1)
# before dictionary: {'state': 'capital', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 'man': 'women', 'brother': 'sister'}

# duplicate keys() are not allows
dc1={'state':'capital',1:'a',2:'b',3:'c',4:'d',5:'e','man':'women','brother':'sister',1:'apple',
     2:'ninja',4:'real'}
print('after using some items:',dc1)
# after using some items: {'state': 'capital', 1: 'apple', 2: 'ninja', 3: 'c', 4: 'real', 5: 'e', 'man': 'women', 'brother': 'sister'}