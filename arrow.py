from psychopy import core, visual, event
from psychopy.visual import ShapeStim
import math
import numpy as np

def rotate(coord, radians):
    (x, y) = coord
    c, s = np.cos(radians), np.sin(radians)
    j = np.array([[c, s], [-s, c]])
    m = np.dot(j, [x, y])

    return float(m.T[0]), float(m.T[1])

def translate(coord, dx, dy):
    (x, y) = coord
    j = np.array([[1, 0, dx],
                [0, 1, dy]])
    m = np.dot(j, [x, y, 1])

    return float(m.T[0]), float(m.T[1])

# arrow
defaultArw = [(-.5, -1.5), (.5, -1.5), (.5, .5), (1, .5), (0, 1.5), (-1, .5), (-.5, .5)]
class Arrow:
    def __init__(self, trans, angle):
        dx, dy = trans
        self.angle = math.radians(angle) 
        self.dx = dx 
        self.dy = dy

    def instantiate(self, win):
        modifiedArw = list(map(lambda x: rotate(x, self.angle), defaultArw))
        modifiedArw = list(map(lambda x: translate(x, self.dx, self.dy), modifiedArw))
        return ShapeStim(win, vertices=modifiedArw, fillColor='CornflowerBlue', size = 0.5, lineColor="CornflowerBlue")

stim1 = [90]
stim2 = [90, 180]
stim3 = [90, 180, 270]
stim4 = [90, 180, 270, 45]
stim5 = [90, 180, 270, 45, 135]
stim6 = [90, 180, 270, 45, 135, 315]
