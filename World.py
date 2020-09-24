import pygame
from Organism import Organism
from GraphicEngine import GraphicEngine
from Animals.Human import Human
from Animals.Wolf import Wolf
from Animals.Sheep import Sheep
from Animals.Fox import Fox
from Animals.Antelope import Antelope
from Animals.CSheep import CSheep
from Animals.Turtle import Turtle
from Plants.SowThistle import SowThistle
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.DeadlyNightshade import DeadlyNightshade
from Plants.SosnowskyHogweed import SosnowskyHogweed
from Commentator import Commentator
import os.path
import random


class MenuOption:
    def __init__(self, organism, x, y, text):
        self.organism = organism
        self.x = x
        self.y = y
        self.text = text


class World:
    def __init__(self, m, n, graphic_engine, mode):
        self.width = int(m)
        self.height = int(n)
        self.graphic_engine = graphic_engine
        self.commentator = Commentator()

        self.mode = mode

        self.organisms = []
        self.types = [SowThistle, Grass, Guarana, DeadlyNightshade, SosnowskyHogweed, Wolf, Sheep, Antelope, Fox,
                      Turtle, CSheep]
        self.randomOrganisms()

        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.human_text = self.font.render('Human', True, (100, 100, 100))
        self.wolf_text = self.font.render('Wolf', True, (0, 0, 0))
        self.sheep_text = self.font.render('Sheep', True, (0, 0, 0))
        self.fox_text = self.font.render('Fox', True, (0, 0, 0))
        self.turtle_text = self.font.render('Turtle', True, (0, 0, 0))
        self.antelope_text = self.font.render('Antelope', True, (0, 0, 0))
        self.cyber_sheep_text = self.font.render('Cyb-sheep', True, (0, 0, 0))
        self.grass_text = self.font.render('Grass', True, (0, 0, 0))
        self.deadly_nightshade_text = self.font.render('Deadly N.', True, (0, 0, 0))
        self.guarana_text = self.font.render('Guarana', True, (0, 0, 0))
        self.sosnowsky = self.font.render('Sosnowsky', True, (0, 0, 0))
        self.sow_thistle = self.font.render('Sow-Thistle', True, (0, 0, 0))
        self.skill = self.font.render('a - human skill', True, (0, 0, 0))
        self.save = self.font.render('s - save world', True, (0, 0, 0))
        self.load = self.font.render('l - load world', True, (0, 0, 0))

        self.round = 0
        self.offset = 40
        self.box_size = self.graphic_engine.BLOCK_SIZE
        self.options = [
            MenuOption(Human, 5, self.offset + (5 + self.box_size) * 0, self.human_text),
            MenuOption(Wolf, 5, self.offset + (5 + self.box_size) * 1, self.wolf_text),
            MenuOption(Sheep, 5, self.offset + (5 + self.box_size) * 2, self.sheep_text),
            MenuOption(Fox, 5, self.offset + (5 + self.box_size) * 3, self.fox_text),
            MenuOption(Turtle, 5, self.offset + (5 + self.box_size) * 4, self.turtle_text),
            MenuOption(Antelope, 5, self.offset + (5 + self.box_size) * 5, self.antelope_text),
            MenuOption(CSheep, 5, self.offset + (5 + self.box_size) * 6, self.cyber_sheep_text),
            MenuOption(Grass, 5, self.offset + (5 + self.box_size) * 8, self.grass_text),
            MenuOption(DeadlyNightshade, 5, self.offset + (5 + self.box_size) * 9, self.deadly_nightshade_text),
            MenuOption(Guarana, 5, self.offset + (5 + self.box_size) * 10, self.guarana_text),
            MenuOption(SosnowskyHogweed, 5, self.offset + (5 + self.box_size) * 11, self.sosnowsky),
            MenuOption(SowThistle, 5, self.offset + (5 + self.box_size) * 12, self.sow_thistle),
        ]

        self.draggable_organism = None
        self.click_coodinates = pygame.mouse.get_pos()

    def randomOrganisms(self):
        self.addNewOrganism(
            Human(random.randint(0, self.width), random.randint(0, self.height), self, self.graphic_engine))
        for t in self.types:
            n = random.randint(1, int(min(self.width, self.height) / 6))
            for _ in range(n):
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                if self.isEmptyPosition(x, y):
                    self.addNewOrganism(t(x, y, self, self.graphic_engine))

    def addComment(self, comment):
        self.commentator.addComment(comment)

    def displayMenu(self):
        s = pygame.Surface((self.graphic_engine.MENU_WIDTH, self.graphic_engine.height))  # the size of your rect
        s.set_alpha(30)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        self.graphic_engine.screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates

        rounds = self.font.render('Round: ' + str(self.round), True, (0, 0, 0))
        self.graphic_engine.screen.blit(rounds, dest=(self.offset, 10))

        if self.draggable_organism is not None:
            coordinates = pygame.mouse.get_pos()
            if self.mode == 1:
                self.draggable_organism.y = int(coordinates[1] / 34)
                tmp = self.graphic_engine.MENU_WIDTH + self.draggable_organism.y*20
                if coordinates[0] < self.graphic_engine.MENU_WIDTH + self.draggable_organism.y*20:
                    self.draggable_organism.x = 0
                else:
                    self.draggable_organism.x = int((coordinates[0] - tmp) / 40)
            else:
                self.draggable_organism.x = 0 if coordinates[0] < self.graphic_engine.MENU_WIDTH else int(
                    (coordinates[0] - self.graphic_engine.MENU_WIDTH) / 20)
                self.draggable_organism.y = int(coordinates[1] / 20)

            self.draggable_organism.draw()

            if self.click_coodinates[0] > 0:
                self.addNewOrganism(self.draggable_organism)
                self.draggable_organism = None

        for option in self.options:
            self.drawOption(option)
            if option.x <= self.click_coodinates[0] <= option.x + self.box_size:
                if option.y <= self.click_coodinates[1] <= option.y + self.box_size:
                    if option.organism is not Human:
                        self.draggable_organism = option.organism(1, 1, self, self.graphic_engine)
                        self.click_coodinates = (-1, -1)

        self.graphic_engine.screen.blit(self.skill, dest=(self.offset - 30, 380))
        self.graphic_engine.screen.blit(self.save, dest=(self.offset - 30, 410))
        self.graphic_engine.screen.blit(self.load, dest=(self.offset - 30, 440))

    def drawOption(self, option):
        self.graphic_engine.drawBoxAbsolute(option.organism.color, option.x, option.y)
        self.graphic_engine.screen.blit(option.text, dest=(self.box_size * 1.4, option.y))

    def drawScene(self):
        for organism in self.organisms:
            if organism is not None:
                organism.draw()

    def playRound(self):
        self.cleanOrganisms()
        self.sortOrganisms()
        self.round += 1
        for organism in self.organisms:
            if organism is not None:
                organism.action()

        self.commentator.comment()
        self.commentator.clear()

    def sortOrganisms(self):
        self.organisms.sort(reverse=True)

    def cleanOrganisms(self):
        new_org = []
        for o in self.organisms:
            if o is not None:
                new_org.append(o)
        self.organisms = new_org

    def save_world(self):
        with open('save.txt', 'w') as file:
            file.write(str(self.height) + '\n')
            file.write(str(self.width) + '\n')
            file.write(str(self.round) + '\n')
            file.write(str(self.mode) + '\n')
            for o in self.organisms:
                if o is not None:
                    if isinstance(o, Human):
                        file.write(type(o).__name__ + " " + str(o.x) + " " + str(o.y) + " " + str(o.power) + " " + str(
                            o.age) + " " + str(o.skill_rounds_active) + '\n')
                    else:
                        file.write(type(o).__name__ + " " + str(o.x) + " " + str(o.y) + " " + str(o.power) + " " + str(
                            o.age) + '\n')
            self.addComment("World was saved!")

    def load_world(self):
        if os.path.exists('save.txt'):
            self.organisms.clear()
            with open('save.txt', 'r') as file:
                index = 0
                for line in file:
                    l = line.split()
                    if index == 0:
                        self.height = int(l[0])
                    elif index == 1:
                        self.width = int(l[0])

                    elif index == 2:
                        self.round = int(l[0])
                    elif index == 3:
                        self.mode = int(l[0])
                        self.graphic_engine = GraphicEngine(self.width, self.height, self.mode)
                    else:
                        o = eval(l[0])(int(l[1]), int(l[2]), self, self.graphic_engine)
                        o.power = int(l[3])
                        o.age = int(l[4])
                        if l[0] == 'Human':
                            o.skill_rounds_active = int(l[5])
                        self.addNewOrganism(o)
                    index += 1
        else:
            self.addComment("There are no saved world!")

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == ord("s"):
                    self.save_world()
                    self.commentator.comment()
                    self.commentator.clear()
                elif event.key == ord("l"):
                    self.load_world()
                    self.commentator.comment()
                    self.commentator.clear()
                else:
                    self.playRound()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_coodinates = pygame.mouse.get_pos()
        return True

    def moveTo(self, organism, x, y):
        for potential_enemy in self.organisms:
            if potential_enemy is not None and potential_enemy is not organism:
                if potential_enemy.x == x and potential_enemy.y == y:
                    if not organism.reproduce(potential_enemy):
                        organism.collision(potential_enemy)
                    return

        organism.x = x
        organism.y = y

    def removeOrganism(self, organism):
        for i in range(len(self.organisms)):
            if self.organisms[i] is not None and self.organisms[i] == organism:
                self.organisms[i] = None
                break

    def isCorrectPosition(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def isEmptyPosition(self, x, y):
        if self.isCorrectPosition(x, y):
            for organism in self.organisms:
                if organism is not None and organism.x == x and organism.y == y:
                    return False
            return True
        return False

    def getOrganismAtPostition(self, x, y):
        if self.isCorrectPosition(x, y):
            for organism in self.organisms:
                if organism is not None and organism.x == x and organism.y == y:
                    return organism
            return None
        return None

    def addNewOrganism(self, organism):
        self.organisms.append(organism)
