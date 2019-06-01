class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"hi i am {self.name}")


nilu = Person("nilu cw")
print(nilu.name)
nilu.talk()

bob =  Person("bob smith")
bob.talk()