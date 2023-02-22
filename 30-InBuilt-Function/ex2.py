
# Using labmda:

# print(list(filter(lambda x: x%2==0,range(1,20))))

# print(list(filter(lambda x: x not in 'aeiou','abcdefghijklmnopqrstuvwxyz')))

# using filter with map:

print(list(map(lambda x : x**2,filter(lambda x:x%2==0, range(1,20)))))
# [4, 16, 36, 64, 100, 144, 196, 256, 324]