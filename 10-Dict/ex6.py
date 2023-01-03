# setdefault():Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary


fruits={'apple':10,'banana':20,'mango':30,'kiwi':40,'graphes':50,'dragon':80,'lemon':5}
print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50, 'dragon': 80, 'lemon': 5}

# syn:dictionary.setdefault(key ,value)





fruits.setdefault('orange',40)
print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50, 'dragon': 80, 'lemon': 5, 'orange': 40}

fruits.setdefault('melon')
print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50, 'dragon': 80, 'lemon': 5, 'orange': 40, 'melon': None}