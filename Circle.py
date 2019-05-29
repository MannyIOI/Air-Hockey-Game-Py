from Shape import Shape
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import math

class Circle(Shape):
    def __init__(self,pos=[0,0,0],radius=0.2,color=[0,1,0]):
        Shape.__init__(self)
        self.radius = radius
        self.pos = self.pos = np.array(pos+color, np.float32)
        self.drawing_type = GL_TRIANGLE_FAN
        self.color = color
        self.setup_shaders()
        self.build_buffer()

    def genCirclePoints(self,center,r):
        ans = [center]
        color = self.color
        for i in range(361):
            x = center[0] + r * math.sin(i / 57.2)
            y = center[1] + r * math.cos(i / 57.2)
            ans.append([x,y,0,color[0],color[1],color[2]])
    ##    print(ans)
        return ans

    # Setup the Shaders for the program
    def setup_shaders(self):
        # read Shader File content
        vertexShaderContent = self.getFileContent("rectangle.vertex.shader")
        fragmentShaderContent = self.getFileContent("rectangle.fragment.shader")

        # compile Shader content
        vertexShader = compileShader(vertexShaderContent, GL_VERTEX_SHADER)
        fragmentShader = compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
        # Compile shader program
        self.program = glCreateProgram()
        glAttachShader(self.program, vertexShader)
        glAttachShader(self.program, fragmentShader)
        assert isinstance(self.program, object)
        glLinkProgram(self.program)

    def build_buffer(self):
        # ver = [0,0,0,0,1,0]
        self.vertexes = np.array(self.genCirclePoints(self.pos,self.radius), dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertexes.nbytes, self.vertexes, GL_STATIC_DRAW)

        glBindVertexArray(self.vao)

        positionLocation = glGetAttribLocation(self.program, "position")
        glVertexAttribPointer(positionLocation, 4, GL_FLOAT, GL_FALSE, 6 * self.vertexes.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(positionLocation)

        colorLocation = glGetAttribLocation(self.program, "newColor");
        glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE, 6 * self.vertexes.itemsize, ctypes.c_void_p(12))
        glEnableVertexAttribArray(colorLocation)

        #positionLocation = glGetAttribLocation(self.program, "position")
        #glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE, 6 * self.vertexes.itemsize, ctypes.c_void_p(0))
        #glEnableVertexAttribArray(positionLocation)

        #colorLocation = glGetAttribLocation(self.program, "color")
        #glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE, 6 * self.vertexes.itemsize, ctypes.c_void_p(0))
        #glEnableVertexAttribArray(colorLocation)

        # unbind VBO
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        # unbind VAO
        glBindVertexArray(0)
        
    def __eq__(self, shape):
        # print(str(self))
        # print(str(shape))
        return str(self) == str(shape)

