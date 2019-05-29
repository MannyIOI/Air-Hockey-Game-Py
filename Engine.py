from events import *
import numpy as np
import math
from Canvas import Canvas
from Circle import Circle
import time
class Engine:
	def __init__(self):
		self.canvas = Canvas(self)
		self.p1 = Circle(pos=[0, 0.8,0],radius=0.2, color=[1,0,0])
		self.p2 = Circle(pos=[0,-0.8,0],radius=0.2, color=[0,0,1])
		self.ball = Circle(pos=[0,0,0], radius=0.1,color=[0,1,1])
		# self.canvas = canvas
		self.movePuck = False
		self.deg = 0


	def startGame(self):
		# self.addMovement(self.p1)
		# self.addMovement2(self.p2)
		self.canvas.add_shape(self.p1)
		self.canvas.add_shape(self.p2)
		self.canvas.add_shape(self.ball)
		self.canvas.update()
		self.force = 0

	def update(self):
		if self.isCollided(self.p1):
			# this should be before it starts to play the game and the ball is stationery
			# pos = self.p1.pos[0:2]
			plPos = (self.p1.pos[0:2] + self.p1.dPos)
			ballPos = (self.ball.pos[0:2] + self.ball.dPos)
			
			vector = plPos + ballPos
			start = np.array([0 ,1])
			vector = [vector[1],vector[0]]

			self.movePuck = True
			# vector = [vector[0],vector[1]]
			self.deg = self.angle_between(vector, start) + 180

		if self.isCollided(self.p2):
			plPos = self.p2.pos[0:2] + self.p2.dPos
			ballPos = self.ball.pos[0:2] + self.ball.dPos
			self.movePuck = True
			
			vector = plPos + ballPos
			start = np.array([0 ,1])
			vector = [vector[0],vector[1]]

			self.deg = self.angle_between(vector, start)
			# self.movePuck(deg,20)

	def unit_vector(self, vector):
		return vector / np.linalg.norm(vector)

	def angle_between(self, vector, start):
		vector = self.unit_vector(vector)
		start = self.unit_vector(start)

		return np.arccos(np.clip(np.dot(vector, start), -1, 1)) * 57.2958
		

	# def addMovement(self, player):
	# 	player.add_event_handler(self.evmoveup)
	# 	player.add_event_handler(self.evmovedown)
	# 	player.add_event_handler(self.evmoveleft)
	# 	player.add_event_handler(self.evmoveright)

	# def addMovement2(self, player):
	# 	player.add_event_handler(self.evmoveup2)
	# 	player.add_event_handler(self.evmovedown2)
	# 	player.add_event_handler(self.evmoveright2)
	# 	player.add_event_handler(self.evmoveleft2)

		# keys=pygame.key.get_pressed()
            # if keys[pygame.K_RIGHT]==1:
            #     self.shapes[0].pos+=[0.1,0,0]

	def isCollided(self, player):
		# a = player.pos + player.dPos
		pldPos = np.array([player.dPos[0],player.dPos[1],0])
		balldPos = np.array([self.ball.dPos[0],self.ball.dPos[1],0])
		pos1 = player.pos[0:3] + pldPos
		pos2 = self.ball.pos[0:3] + balldPos
		mag = player.radius + self.ball.radius
		diff = (np.linalg.norm(pos1-pos2) - (player.radius + self.ball.radius - 0.001))
		return diff < 0.001

	def moveup(self,shape):
		pldPos = np.array([shape.dPos[0],shape.dPos[1],0]) + shape.pos[0:3]
		# print(pldPos)
		if pldPos[1]+shape.radius <= 1 and not self.isCollided(shape) and shape == self.p1:
			dPos = np.array([shape.dPos[0],shape.dPos[1],0])
			pos = shape.pos[0:3] + dPos
			shape.dPos+=[0,0.01]
			self.update()
		elif pldPos[1] + shape.radius <= 0 and not self.isCollided(shape) and shape == self.p2:
			dPos = np.array([shape.dPos[0],shape.dPos[1],0])
			pos = shape.pos[0:3] + dPos
			shape.dPos+=[0,0.01]
			self.update()

	def movedown(self,shape):
		pldPos = np.array([shape.dPos[0],shape.dPos[1],0]) + shape.pos[0:3]
		# print(pldPos[1] + shape.radius > 0, pldPos[1] ,"+",shape.radius)
		if pldPos[1]-shape.radius > 0 and not self.isCollided(shape) and shape == self.p1:
			dPos = np.array([shape.dPos[0],shape.dPos[1],0])
			pos = shape.pos[0:3] + dPos
			# print("here")
			shape.dPos-=[0,0.01]
			self.update()
		elif pldPos[1]-shape.radius >= -1 and not self.isCollided(shape) and shape == self.p2:
			dPos = np.array([shape.dPos[0],shape.dPos[1],0])
			pos = shape.pos[0:3] + dPos
			# print("here2")
			shape.dPos -= [0,0.01]
			self.update()
	def moveleft(self,shape):
		pldPos = np.array([shape.dPos[0],shape.dPos[1],0]) + shape.pos[0:3]
		if shape.dPos[0] > -0.79 and not self.isCollided(shape):
			shape.dPos -= [0.01,0]
			self.update()
	def moveright(self,shape):
		if shape.dPos[0] < 0.79 and not self.isCollided(shape):
			shape.dPos += [0.01,0]
			self.update()

engine = Engine()
engine.startGame()
