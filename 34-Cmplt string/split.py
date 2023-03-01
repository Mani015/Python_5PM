
# split:


python = 'python is a general purpose programming'
# print(python)
print()
# print(python.split('p'))
# ['', 'ython is a general ', 'ur', 'ose ', 'rogramming']
# print(python.split('e'))
# ['python is a g', 'n', 'ral purpos', ' programming']


Type = 'programming,eating,playing,dancing,watching,cooking,sleeping'
# print(Type)
print()

# print(Type.split('ing'))
# ['programm', ',eat', ',play', ',danc', ',watch', ',cook', ',sleep', '']

# using sceond parameter:
# print(Type.split(sep,max))
print(Type.split('ing',4))
# ['programm', ',eat', ',play', ',danc', ',watching,cooking,sleeping']