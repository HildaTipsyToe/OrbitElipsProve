import math
import random
import pygame as pg
import pygame.event
from Circle import Circle
from Lines import Lines



vector = pg.math.Vector2

class MainProgram():
    def __init__(self):
        pg.init()
        self.running = True
        self.width = 1280
        self.height = 720
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)

        self.radius = 350
        self.circle = Circle((self.width/2, self.height/2), self.radius, 2)


        self.R = 300
        self.rn = self.R * random.uniform(0, 1)
        self.thetan = random.uniform(0, 2*math.pi)
        self.rPos = vector(math.cos(self.thetan) * self.rn + self.width/2, math.sin(self.thetan) * self.rn + self.height/2)

        self.point_In_Circle = Circle(self.rPos, 10)


        self.lines = []
        self.n = 200
        for x in range(self.n):
            randColor = (random.uniform(0, 256), random.uniform(0, 256), random.uniform(0, 256))
            angle = (2*math.pi)/self.n
            endpos = math.cos(angle * x) * self.radius + self.width/2, math.sin(angle * x) * self.radius + self.height/2
            self.line = Lines(vector(self.rPos), vector(endpos), angle * x, (255, 255, 255), 3)
            self.lines.append(self.line)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.window.fill((25, 25, 25))
            self.circle.draw(self.window)
            for line in self.lines:
                line.draw(self.window)
                line.update()
            self.point_In_Circle.draw(self.window)
            pygame.display.update()
            self.clock.tick(144)
        pygame.quit()


MainProgram().run()
