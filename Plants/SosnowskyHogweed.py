from Plants.Plant import Plant
from GraphicEngine import Colors
import Animals


class SosnowskyHogweed(Plant):
    color = Colors.PURPLE

    def __init__(self, x, y, world, graphic_engine):
        super(Plant, self).__init__(x, y, world, graphic_engine)
        self.power = 10
        self.SPREAD_PROBABILITY = 0.02

    def getInstance(self, x, y, world, graphic_engine):
        return SosnowskyHogweed(x, y, world, graphic_engine)

    def action(self):
        self.growOlder()
        self.spreadOut()
        self.killNeighbors()

    def killNeighbors(self):
        for organism in self.world.organisms:
            if organism is not None:
                if organism.x in [self.x-1,self.x,self.x+1] and organism.y in [self.y-1,self.y,self.y+1]:
                    if isinstance(organism,Animals.Animal.Animal) and not isinstance(organism,Animals.CSheep.CSheep):
                        self.world.addComment(self.introduce()+" poisoned animal "+organism.introduce())
                        self.world.removeOrganism(organism)

    def introduce(self):
        return "Sosnowsky's hogweed"

