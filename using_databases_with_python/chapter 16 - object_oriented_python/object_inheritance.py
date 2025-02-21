#superclass
class PartyAnimal:
    #construction message
    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, "constructed")
    #method message
    def party(self):
        self.x = self.x + 1
        print(self.name,"party count", self.x)

#subclass
class FootballFan(PartyAnimal):
    #initializing first the superclass, after that, initializing subclass
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()