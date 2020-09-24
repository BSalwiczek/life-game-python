import pygame
import random
import math


class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (126, 220, 31)
    DARK_GREEN = (0, 115, 0)
    LIGHT_RED = (209, 0, 5)
    BROWN = (121, 81, 0)
    LIGHT_BROWN = (255, 207, 66)
    ORANGE = (246, 111, 0)
    ORANGE_YELLOW = (255, 170, 0)
    AQUA = (0, 115, 89)
    PINK = (241, 0, 136)
    PURPLE = (184, 3, 255)


class GraphicEngine(object):
    BLOCK_SIZE = 20
    MENU_WIDTH = 170

    def __init__(self, m, n, mode):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = self.BLOCK_SIZE * int(m) * (3 if mode == 1 else 1)
        self.height = self.BLOCK_SIZE * int(n) * (2 if mode == 1 else 1)
        self.screen = pygame.display.set_mode([self.MENU_WIDTH + int(self.width), int(self.height)])
        pygame.display.set_caption('Life game')

    def reset(self):
        self.screen.fill((255, 255, 255))

    def render(self):
        self.clock.tick(30)
        pygame.display.flip()

    def drawHex(self, color, x, y):
        n, r = 6, self.BLOCK_SIZE
        pygame.draw.polygon(self.screen, color, [
            (self.MENU_WIDTH + x*2*self.BLOCK_SIZE +y*self.BLOCK_SIZE + self.BLOCK_SIZE + r * math.cos(math.pi/2 + 2 * math.pi * i / n), y*1.7*self.BLOCK_SIZE + self.BLOCK_SIZE + r * math.sin(math.pi/2 + 2 * math.pi * i / n))
            for i in range(n)
        ])

    def drawBox(self, color, x, y):
        pygame.draw.rect(self.screen, color,
                         [self.MENU_WIDTH+x * self.BLOCK_SIZE, y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE])

    def drawBoxAbsolute(self, color, x, y):
        pygame.draw.rect(self.screen, color,[x, y, self.BLOCK_SIZE, self.BLOCK_SIZE])

    @staticmethod
    def quit():
        pygame.quit()
