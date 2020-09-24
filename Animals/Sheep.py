from Animals.Animal import Animal
from GraphicEngine import Colors


class Sheep(Animal):
    color = Colors.LIGHT_BROWN

    def __init__(self, x, y, world, graphic_engine):
        super(Sheep, self).__init__(x, y, world, graphic_engine)
        self.power = 4
        self.initiative = 4

    def reproduce(self, partner):
        if isinstance(partner, Sheep):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(Sheep(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Sheeps reproduced! There is one more sheep now.")
            return True
        return False

    def introduce(self):
        return "Sheep"
