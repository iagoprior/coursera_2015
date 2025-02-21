#class
class PartyAnimal:
    #construction message
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")
    #method message
    def party(self):
        self.x = self.x + 1
        print(self.name,"party count", self.x)
    #destruction message
    def __del__(self):
        print("I am destructed", self.x)

s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Joe")

j.party()
s.party()
