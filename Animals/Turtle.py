from Animals.Animal import Animal
from GraphicEngine import Colors
import random

class Turtle(Animal):
    color = Colors.AQUA

    def __init__(self, x, y, world, graphic_engine):
        super(Turtle, self).__init__(x, y, world, graphic_engine)
        self.power = 2
        self.fight_off_power = 5
        self.initiative = 1

    def action(self):
        self.growOlder()
        if random.randint(0,3) == 0:
            self.move()

    def reproduce(self, partner):
        if isinstance(partner, Turtle):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(Turtle(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Turtles reproduced! There is one more turtle now.")
            return True
        return False

    def introduce(self):
        return "Turtle"
