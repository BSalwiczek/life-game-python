from Animals.Animal import Animal
from GraphicEngine import Colors


class Antelope(Animal):
    color = Colors.ORANGE_YELLOW

    def __init__(self, x, y, world, graphic_engine):
        super(Antelope, self).__init__(x, y, world, graphic_engine)
        self.power = 4
        self.step = 2
        self.initiative = 4

    def reproduce(self, partner):
        if isinstance(partner, Antelope):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(Antelope(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Antelopes reproduced! There is one more antelope now.")
            return True
        return False

    def introduce(self):
        return "Antelope"
