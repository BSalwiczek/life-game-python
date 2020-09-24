from Animals.Animal import Animal
from GraphicEngine import Colors
import pygame
import random

class Human(Animal):
    color = Colors.BLUE

    def __init__(self, x, y, world, graphic_engine):
        super(Human, self).__init__(x, y, world, graphic_engine)
        self.power = 5
        self.step = 1
        self.initiative = 4
        self.skill_active = False
        self.skill_rounds_active = 0

    def introduce(self):
        return "Human"

    def action(self):
        if self.skill_rounds_active < 0:
            self.skill_rounds_active += 1
        elif 0 < self.skill_rounds_active < 3:
            self.skill_active = True
            self.step = 2

        if self.skill_active:
            self.skill_rounds_active += 1
            if self.skill_rounds_active >= 3:
                if random.randint(0,1) == 0:
                    self.step = 1
                else:
                    self.step = 2
            if self.skill_rounds_active >= 5:
                self.skill_active = False
                self.skill_rounds_active = -5
                self.world.addComment("Human deactivated skill - antelope speed")
                self.step = 1

        self.growOlder()
        pressed_keys = pygame.key.get_pressed()
        new_x = self.x
        new_y = self.y
        if pressed_keys[pygame.K_UP]:
            new_y -= self.step
        if pressed_keys[pygame.K_DOWN]:
            new_y += self.step
        if pressed_keys[pygame.K_LEFT]:
            new_x -= self.step
        if pressed_keys[pygame.K_RIGHT]:
            new_x += self.step
        if pressed_keys[pygame.K_a]:
            if not self.skill_active and self.skill_rounds_active == 0:
                self.world.addComment("Human activated skill - antelope speed")
                self.step = 2
                self.skill_active = True

        if self.world.isCorrectPosition(new_x,new_y):
            self.world.moveTo(self, new_x, new_y)