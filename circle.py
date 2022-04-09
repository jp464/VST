from psychopy import core, visual, event
from psychopy.visual import ShapeStim
import math
import numpy as np

def translate(coord, dx, dy):
    (x, y) = coord
    j = np.array([[1, 0, dx],
                [0, 1, dy]])
    m = np.dot(j, [x, y, 1])

    return float(m.T[0]), float(m.T[1])

# Circle class 
class Circle:
    def __init__(self, trans, color):
        dx, dy = trans
        self.dx = dx
        self.dy = dy
        self.color = color 

    def instantiate(self, window):
        return visual.Circle(win = window, radius = 0.7, pos = translate((0, 0), self.dx, self.dy), fillColor = self.color, colorSpace = 'rgb255')

# indpt variable for circle: colors
c1 = [183, 56, 255]
c2 = [203, 112, 255]
c3 = [223, 168, 255]
c4 = [126, 0, 199]
c5 = [91, 0, 143]
c6 = [55, 0, 87]
stim1 = [c4]
stim2 = [c4, c6]
stim3 = [c4, c6, c2] 
stim4 = [c4, c6, c2, c5]
stim5 = [c4, c6, c2, c5, c3]
stim6 = [c4, c6, c2, c5, c3, c1]

cc1 = [255, 0, 0]
cc2 = [255, 255, 0]
cc3 = [255, 255, 0]
cc4 = [0, 255, 255]
cc5 = [0, 0, 255]
cc6 = [0, 0, 0]
Stim1 = [cc1]
Stim2 = [cc1, cc2]
Stim3 = [cc1, cc2, cc3]
Stim4 = [cc1, cc2, cc3, cc4]
Stim5 = [cc1, cc2, cc3, cc4, cc5]
Stim6 = [cc1, cc2, cc3, cc4, cc5, cc6]


# mywin = visual.Window([800, 650], monitor="stanleyMac", units="deg")
# Circle([-4, 0], c6).instantiate(mywin).draw()
# Circle([-2, 0], c5).instantiate(mywin).draw()
# Circle([0, 0], [162, 0, 255]).instantiate(mywin).draw()
# Circle([2, 0], c4).instantiate(mywin).draw()
# Circle([4, 0], c3).instantiate(mywin).draw()
# Circle([0, 3], c2).instantiate(mywin).draw()
# Circle([0, -3], c1).instantiate(mywin).draw()
# mywin.update()
# core.wait(30)


