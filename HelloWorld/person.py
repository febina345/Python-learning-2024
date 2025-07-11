class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, Iam {self.name}")

john = Person("john smith")
bob= Person("Bob smith")


john.talk()
bob.talk()

