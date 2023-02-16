# FILTER()
# The filter() function returns an iterator were the items are filtered through a function
# to test if the item is accepted or not.
# Syntax:

# filter(functionname, iterable)


def Filter(i):
    if i<10:
        return i

value = filter(Filter,range(1,21))
print(set(value))