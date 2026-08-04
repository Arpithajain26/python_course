class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass
class Cat(Mammal):
    pass

fof=Dog()
fof.walk()