from Plants.Plant import Plant
from GraphicEngine import Colors


class Guarana(Plant):
    color = Colors.LIGHT_RED

    def __init__(self, x, y, world, graphic_engine):
        super(Guarana, self).__init__(x, y, world, graphic_engine)
        self.SPREAD_PROBABILITY = 0.03

    def getInstance(self, x, y, world, graphic_engine):
        return Guarana(x, y, world, graphic_engine)

    def introduce(self):
        return "Guarana (+3 power)"

    def bonusForEating(self, other_organism):
        other_organism.power += 3
