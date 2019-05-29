import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import math
# from Engine import Engine

class Canvas:
    def __init__(self, engine):
        self.shapes = []
        self.engine = engine
        pygame.init()
        display = (600,600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glClearColor(.30, 0.20, 0.20, 1.0)
        glViewport(0, 0, display[0], display[1])

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for shape in self.shapes:
            vao = shape.vao
            program = shape.program
            n_vertexes = len(shape.vertexes)

            glUseProgram(program)
            glBindVertexArray(vao)

            shape.update()
            glDrawArrays(shape.drawing_type, 0, n_vertexes)
            glBindVertexArray(0)

    def exec_handlers(self,event):
        for shape in self.shapes:
            shape.exec_event_handler(event)
            # print(shape.pos)

    def flip(self):
        self.draw()
        pygame.display.flip()
        pygame.time.wait(10)


    def update(self):
        count = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.exec_handlers(event)

            keys=pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]==1:
                self.engine.moveright(self.shapes[0])   
                # self.engine.update()

            if keys[pygame.K_d]==1:
                self.engine.moveright(self.shapes[1])   
                # self.engine.update()

            if keys[pygame.K_LEFT]==1:
                self.engine.moveleft(self.shapes[0])   
                # self.engine.update()
            if keys[pygame.K_a]==1:
                self.engine.moveleft(self.shapes[1])   
                # self.engine.update()

            if keys[pygame.K_UP]==1:
                self.engine.moveup(self.shapes[0])  
                # self.engine.update()
  
            if keys[pygame.K_w]==1:
                self.engine.moveup(self.shapes[1])  
                # self.engine.update()

            if keys[pygame.K_DOWN]==1:
                self.engine.movedown(self.shapes[0])   
                # self.engine.update()
            if keys[pygame.K_s]==1:
                self.engine.movedown(self.shapes[1])   
                # self.engine.update()

            if self.engine.movePuck:
                puckPos = self.shapes[2].pos[0:2] + self.shapes[2].dPos
                # print(puckPos[0], puckPos[0] + 0.9 <= 0.0001)
                if puckPos[0] + 0.9 <= 0.0001 or puckPos[0] - 0.9 >= 0.0001:
                    # if it reaches the left border from top and bottom
                    self.engine.deg = -1*(self.engine.deg - 180) % 360
                    # print("top player won")
                    pass

                # if puckPos[1] + 0.9 <= 0.0001:
                #     # if it reaches the bottom border
                #     print("top player won")
                #     pass
                if puckPos[1] - 0.9 >= 0.0001:
                    # if it reaches the top border
                    self.engine.deg = (-1 * self.engine.deg) % 360
                    print("bottom player won")
                    pygame.quit()
                    quit()
                if puckPos[1] + 0.9 <= 0.0001:
                    self.engine.deg = (-1 * self.engine.deg) % 360
                    print("top player won")
                    pygame.quit()
                    quit()

                
                deg = self.engine.deg
                x_comp = math.cos(deg / 57.2958) / 50
                y_comp = math.sin(deg / 57.2958) / 50
                
                self.shapes[2].dPos+=[x_comp, y_comp]

            self.draw()
            self.engine.update()
            # self.engine.update2()


            pygame.display.flip()
            pygame.time.wait(10)