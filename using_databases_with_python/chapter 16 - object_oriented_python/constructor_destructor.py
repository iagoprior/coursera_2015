#class
class PartyAnimal:
    #construction message
    def __init__(self):
        self.x = 0
        print("I am constructed")
    #method message
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
    #destruction message
    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()

# calls the party method
an.party()
an.party()
an.party()
an = 42
print("An contains", an)