

class Organism:
    color = ()

    def __init__(self, x, y, world, graphic_engine):
        self.y = y
        self.x = x
        self.world = world
        self.graphic_engine = graphic_engine
        self.power = 0
        self.initiative = 0
        self.age = 0

    def draw(self):
        pass

    def __lt__(self, other):
        if other is None:
            return True
        if self.initiative < other.initiative:
            return True
        if self.initiative > other.initiative:
            return False
        if self.age < other.age:
            return True
        return False

    def reproduce(self, partner):
        pass

    def introduce(self):
        pass

    def action(self):
        pass

    def collision(self, other_organism):
        pass
