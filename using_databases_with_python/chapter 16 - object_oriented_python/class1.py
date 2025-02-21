#class
class PartyAnimal:
    # method 1 , self is a instance, x is an attribute
    #special meaning function -> initializing the class PartyAnimal / get back the value
    def __init__(self):
        self.x = 0
    # method 2
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

#variable/ instance an -> Contruct the class
an = PartyAnimal()

# calls the party method
an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))