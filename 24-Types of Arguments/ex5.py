# Variable-length arguments:
# In Python, sometimes, there is a situation where we need to pass multiple arguments to the function.
# Such types of arguments are called arbitrary arguments or variable-length arguments.
#
# We use variable-length arguments if we don’t know the number of arguments needed for the function in advance.

# Arbitrary positional arguments (*args)
# Arbitrary keyword arguments (**kwargs)

# # Arbitrary positional arguments (*args):

def variable_length_Arguments(*chaithanya):
    print(chaithanya)
# variable_length_Arguments(1,2,3,4,5,6,7,89,10,1,12,13,45,69,85,74)
variable_length_Arguments()
# (1, 2, 3, 4, 5, 6, 7, 89, 10, 1, 12, 13, 45, 69, 85, 74)

# def percentage(*args):
#     sum = 0
#     for i in args:
#         # get total
#         sum = sum + i
#     # calculate average
#     avg = sum / len(args)
#     print('Average =', avg)
#
# percentage(56, 61, 73)

# def percentage(*subjects):
#     sum = 0
#     for i in subjects:
#         # get total
#         sum = sum + i
#     # calculate average
#     avg = sum / len(subjects)
#     print('Average =', avg)
#
# percentage(56, 61, 73)

