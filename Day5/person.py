class Person:
    def __init__(self,name):
        self.name=name
    def talk(self,name):
        print(f" Hello,I am {name} and happy to connected with you")
john=Person("john smith")
print(john.name)
john.talk("johnnn")