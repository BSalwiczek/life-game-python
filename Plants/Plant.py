from Organism import Organism
import random


class Plant(Organism):

    def __init__(self, x, y, world, graphic_engine):
        self.SPREAD_PROBABILITY = 0.02
        self.initiative = 0
        super(Plant, self).__init__(x, y, world, graphic_engine)

    def growOlder(self):
        self.age += 1

    def draw(self):
        if self.world.mode == 1:
            self.graphic_engine.drawHex(self.color, self.x, self.y)
        else:
            self.graphic_engine.drawBox(self.color, self.x, self.y)

    def action(self):
        self.growOlder()
        self.spreadOut()

    def collision(self, other_organism):
        self.bonusForEating(other_organism)
        pass

    def bonusForEating(self, attacer):
        pass

    def introduce(self):
        pass

    def getInstance(self, x, y, world, graphic_engine):
        pass

    def spreadOut(self):
        if random.randint(0, 100) < self.SPREAD_PROBABILITY:
            for _ in range(10):
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                if self.world.isEmptyPosition(self.x + dx, self.y + dy):
                    self.world.addNewOrganism(
                        self.getInstance(self.x + dx, self.y + dy, self.world, self.graphic_engine))
                    break

