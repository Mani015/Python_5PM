# popitem():Returns and removes the key-value pair from the dictionary, it removes end of the item from dictionary
fruits={'apple':10,'banana':20,'mango':30,'kiwi':40,'graphes':50,'dragon':80,'lemon':5}
print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50, 'dragon': 80, 'lemon': 5}
fruits.popitem()
print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50, 'dragon': 80}

# print(fruits.popitem())
# ('dragon', 80)
# print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40, 'graphes': 50}


# print(fruits.popitem())
# ('graphes', 50)
# print(fruits)
# {'apple': 10, 'banana': 20, 'mango': 30, 'kiwi': 40}

