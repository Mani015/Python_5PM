

# With out decorator:


def Outer(fun):
    def inner():
        name = fun()
        return name + ' full stack developer'
    return inner

@Outer
def Next_Fun():
    return  'python'

# techno = Outer(Next_Fun)
# print(techno())
print(Next_Fun())