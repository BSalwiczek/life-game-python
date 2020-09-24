from Animals.Animal import Animal
from GraphicEngine import Colors


class Wolf(Animal):
    color = Colors.BROWN

    def __init__(self, x, y, world, graphic_engine):
        super(Wolf, self).__init__(x, y, world, graphic_engine)
        self.power = 9
        self.initiative = 5

    def reproduce(self, partner):
        if isinstance(partner, Wolf):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(Wolf(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Wolves reproduced! There is one more wolf now.")
            return True
        return False

    def introduce(self):
        return "Wolf"
