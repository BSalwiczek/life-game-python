from Plants.Plant import Plant
from GraphicEngine import Colors


class DeadlyNightshade(Plant):
    color = Colors.BLACK

    def __init__(self, x, y, world, graphic_engine):
        super(Plant, self).__init__(x, y, world, graphic_engine)
        self.power = 99
        self.SPREAD_PROBABILITY = 0.03

    def getInstance(self, x, y, world, graphic_engine):
        return DeadlyNightshade(x, y, world, graphic_engine)

    def introduce(self):
        return "Deadly nightshade"
