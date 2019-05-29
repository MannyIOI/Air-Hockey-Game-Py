from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os


class Shape:
    def __init__(self):
        self.drawing_type = None
        self.vertexes = None
        self.program = None
        self.vao = None
        self.vbo = None
        self.event_handlers = []
        self.dPos = np.array([0,0],dtype=np.float32)
##        self.pos=[0,0,0]


    def getFileContent(self,filename):
        p = os.path.join(os.getcwd(), "shaders", filename)
        return open(p, 'r').read()

    def add_event_handler(self,fun):
        self.event_handlers.append(fun)

    def exec_event_handler(self,event):
        for i in self.event_handlers:
            i(self,event)
    def update(self):
        # print(self.program)
        newPosLoc = glGetUniformLocation(self.program, "dPos")
        # print(newPosLoc)
        glUniform2fv(newPosLoc, 1, self.dPos)




