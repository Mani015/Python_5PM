# get():Returns the value for the given key
# syn: dictionary.get(key)

dc1={'state':'capital',1:'a',2:'b',3:'c',4:'d',5:'e','man':'women','brother':'sister'}

print(dc1.get(2))
# b
print(dc1.get('brother'))
# sister


print(dc1.get('tv'))
# None
