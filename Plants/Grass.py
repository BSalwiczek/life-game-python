from Plants.Plant import Plant
from GraphicEngine import Colors


class Grass(Plant):
    color = Colors.GREEN

    def __init__(self, x, y, world, graphic_engine):
        super(Grass, self).__init__(x, y, world, graphic_engine)
        self.SPREAD_PROBABILITY = 0.03

    def getInstance(self, x, y, world, graphic_engine):
        return Grass(x, y, world, graphic_engine)

    def introduce(self):
        return "Grass"
