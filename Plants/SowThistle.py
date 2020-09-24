from Plants.Plant import Plant
from GraphicEngine import Colors


class SowThistle(Plant):
    color = Colors.YELLOW

    def __init__(self, x, y, world, graphic_engine):
        super(SowThistle, self).__init__(x, y, world, graphic_engine)

    def getInstance(self, x, y, world, graphic_engine):
        return SowThistle(x, y, world, graphic_engine)

    def introduce(self):
        return "Sow-thistle"

    def action(self):
        self.growOlder()
        self.spreadOut()
        self.spreadOut()
        self.spreadOut()
