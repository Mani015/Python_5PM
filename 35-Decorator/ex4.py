# List Comprehension:

l1 = [1,2,3,4,5,6,7]
# for i in l1:
#     k = i**2
    # print(list(k))


# Syntax:

# [expression for iterable in object]

# print([i**2 for i in l1])

# If I want only even number:
# Sy:[expression for iterable in object if(condition)]
# print([i for i in range(1,20) if i%2==0])

l1 = [1,2,3,4,5,6,7]
# print([i if i%2==0 else i+1 for i in range(20)])


# print([i for i in range(20) if i>10])
# [11, 12, 13, 14, 15, 16, 17, 18, 19]

print([i for i in range(20) if i%2==1])
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

