class grandparent:
    def wealth1(self):
        print('this is grandparent wealth1')

class parent1(grandparent):
    def wealth2(self):
        print('this is parent1 wealth2')
class parent2():
    def wealth3(self):
        print('this is parent2 wealth3')

class child(parent1,parent2):
    def wealth4(self):
        print('this is child wealth4')

ojt1=child()
ojt1.wealth1()
ojt1.wealth2()
ojt1.wealth3()
ojt1.wealth4()





