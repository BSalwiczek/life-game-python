from Animals.Animal import Animal
from GraphicEngine import Colors
import random


class Fox(Animal):
    color = Colors.ORANGE

    def __init__(self, x, y, world, graphic_engine):
        super(Fox, self).__init__(x, y, world, graphic_engine)
        self.power = 3
        self.initiative = 7

    def introduce(self):
        return "Fox"

    def reproduce(self, partner):
        if isinstance(partner, Fox):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(Fox(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Foxes reproduced! There is one more fox now.")
            return True
        return False

    def action(self):
        self.growOlder()
        for _ in range(10):
            dx = random.randint(-1,1)
            dy = random.randint(-1,1)
            new_x, new_y = self.x + dx, self.y + dy

            potential_enemy = self.world.getOrganismAtPostition(new_x,new_y)
            if potential_enemy is not None and potential_enemy.power > self.power:
                continue

            if self.world.isCorrectPosition(new_x, new_y):
                self.world.moveTo(self, new_x, new_y)
                return
