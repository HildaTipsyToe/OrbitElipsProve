import pygame as pg


vector = pg.math.Vector2
class Circle():
    def __init__(self, pos, radius, width=0, color=(125, 125, 125)):
        self.pos = vector(pos)
        self.radius = radius
        self.color = color
        self.width = width


    def update(self):
        pass

    def draw(self, window):
        pg.draw.circle(window, self.color, self.pos, self.radius, width=self.width)
