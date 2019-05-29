from Canvas import Canvas
from Circle import Circle
from Engine import *

c1 = Circle(pos=[0, 0.75,0],radius=0.25)
c2 = Circle(pos=[0,-0.75,0],radius=0.25)
pu = Circle(pos=[0,0,0], radius=0.1,color=[0,1,1])

engine = Engine(c1, c2, pu)
engine.startGame()