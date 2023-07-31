import numpy as np
import pygame as pg
import pygame.math

vector = pygame.math.Vector2
class Lines():
    def __init__(self, startPos, endPos, angle, color=(125, 125, 125), width=1):
        self.startPos = startPos
        self.endPos = endPos
        self.width = width
        self.color = color
        self.angle = angle
        self.origin = ((self.startPos.x + self.endPos.x) / 2, (self.startPos.y + self.endPos.y) / 2)

    def update(self):
        self.rotateLine(0.5)

    def draw(self, window):
        pg.draw.line(window, self.color, self.startPos, self.endPos, self.width)
        pg.draw.circle(window, (255, 0, 0), self.origin, 4)

    def rotateLine(self, degrees):

        p = [(self.startPos.x, self.startPos.y), (self.endPos.x, self.endPos.y)]

        angle = np.deg2rad(degrees)
        R = np.array([[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle), np.cos(angle)]])
        o = np.atleast_2d(self.origin)
        p = np.atleast_2d(p)
        temp = np.squeeze((R @ (p.T - o.T) + o.T).T)

        self.startPos = vector(temp[0][0], temp[0][1])
        self.endPos = vector(temp[1][0], temp[1][1])