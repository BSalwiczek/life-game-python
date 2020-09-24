from Animals.Sheep import Sheep
from GraphicEngine import Colors
from Plants.SosnowskyHogweed import SosnowskyHogweed


class CSheep(Sheep):
    color = Colors.PINK

    def __init__(self, x, y, world, graphic_engine):
        super(CSheep, self).__init__(x, y, world, graphic_engine)
        self.power = 11

    def action(self):
        self.growOlder()
        target = self.findNearestSosnowsky()
        if target:
            vec = [target[0]-self.x, target[1]-self.y]
            new_x = self.x
            new_y = self.y
            if vec[0] > 0:
                new_x += 1
            if vec[0] < 0:
                new_x -= 1
            if vec[1] > 0:
                new_y += 1
            if vec[1] < 0:
                new_y -= 1
            self.world.moveTo(self, new_x, new_y)
        else:
            self.move()

    def findNearestSosnowsky(self):
        closest = []
        for o in self.world.organisms:
            if isinstance(o, SosnowskyHogweed):
                if closest:
                    if self.dist2(closest[0],closest[1]) > self.dist2(o.x,o.y):
                        closest[0] = o.x
                        closest[1] = o.y
                else:
                    closest.append(o.x)
                    closest.append(o.y)
        return closest

    def dist2(self,x,y):
        return (x-self.x)**2+(y-self.y)**2

    def reproduce(self, partner):
        if isinstance(partner, CSheep):
            child_pos = self.findPlaceForChild(self, partner)
            if child_pos:
                self.world.addNewOrganism(CSheep(child_pos[0], child_pos[1],self.world, self.graphic_engine))
                self.world.addComment("Cyber-Sheeps reproduced! There is one more cyber-sheep now.")
            return True
        return False

    def introduce(self):
        return "Cyber-sheep"
