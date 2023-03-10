
# TO calling classmethod with out classname


class Fruits:
    Banana = 'chekkara keli'
    Apple = 'eat daily one apple---> away from doctor'
    @classmethod
    def classmethod(cls):
        print(cls.Banana)
        print(Fruits.Apple)

Fruits.classmethod()
# chekkara keli
# eat daily one apple---> away from doctor

# With out calling className to the classmethod

# classmethod()
# TypeError: classmethod expected 1 argument, got 0


# using classname ---> Fruits

Fruits.classmethod()
# chekkara keli
# eat daily one apple---> away from doctor
