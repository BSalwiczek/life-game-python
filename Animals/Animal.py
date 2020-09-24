from Organism import Organism
from Plants.Plant import Plant
from copy import deepcopy
import random


class Animal(Organism):

    def __init__(self, x, y, world, graphic_engine):
        super(Animal, self).__init__(x, y, world, graphic_engine)
        self.step = 1

    def draw(self):
        if self.world.mode == 1:
            self.graphic_engine.drawHex(self.color, self.x, self.y)
        else:
            self.graphic_engine.drawBox(self.color, self.x, self.y)

    def growOlder(self):
        self.age += 1

    def action(self):
        self.growOlder()
        self.move()

    def move(self):
        for _ in range(10):
            dx = random.randint(-self.step, self.step)
            dy = random.randint(-self.step, self.step)
            new_x, new_y = self.x + dx, self.y + dy
            if self.world.isCorrectPosition(new_x, new_y):
                self.world.moveTo(self, new_x, new_y)
                return

    def introduce(self):
        pass

    def findPlaceForChild(self, a1, a2):
        pos1 = [a1.x, a1.y]
        pos2 = [a2.x, a2.y]
        new_pos = []
        for _ in range(10):
            dxy = 1 if random.randint(0, 1) == 1 else -1
            if random.randint(0, 1) == 0:  # pos1 chosen
                new_pos = deepcopy(pos1)
                if random.randint(0, 1) == 0:
                    new_pos[0] += dxy
                else:
                    new_pos[1] += dxy
            else:
                new_pos = deepcopy(pos2)
                if random.randint(0, 1) == 0:
                    new_pos[0] += dxy
                else:
                    new_pos[1] += dxy
            if self.world.isEmptyPosition(new_pos[0], new_pos[1]):
                return new_pos
        return []

    def reproduce(self, partner):
        pass

    def collision(self, other_organism):
        if other_organism.power > self.power:
            if isinstance(other_organism, Plant):
                self.world.removeOrganism(other_organism)
                self.world.addComment(self.introduce() + " ate plant " + other_organism.introduce() + " and died")
            else:
                self.world.addComment(self.introduce() + " attacked " + other_organism.introduce() + " and died")

            self.world.removeOrganism(self)
        else:
            if isinstance(other_organism, Plant):
                other_organism.bonusForEating(self)
                self.world.addComment(self.introduce() + " ate plant " + other_organism.introduce())
            else:
                if isinstance(other_organism, Turtle):
                    if self.power < other_organism.fight_off_power:
                        self.world.addComment("Turtle fight off " + self.introduce() + " attack. ")
                        return
                if isinstance(other_organism, Antelope):
                    if random.randint(0, 1) == 0:
                        self.x = other_organism.x
                        self.y = other_organism.y
                        other_organism.action()
                        self.world.addComment("Antelope run away from " + self.introduce() + " attack. ")
                        return

                self.world.addComment(self.introduce() + " win battle with " + other_organism.introduce())

            self.x = other_organism.x
            self.y = other_organism.y
            self.world.removeOrganism(other_organism)


from Animals.Turtle import Turtle
from Animals.Antelope import Antelope
