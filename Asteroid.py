import pygame
from circleshape import CircleShape
import random
from constants import *
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius<=ASTEROID_MIN_RADIUS:
			return
		else:
			ran_angle=random.uniform(20,50)
			new_angle_1=self.velocity.rotate(ran_angle)
			new_angle_2=self.velocity.rotate(-ran_angle)
			self.radius-=ASTEROID_MIN_RADIUS
			new_Asteroid=Asteroid(self.position.x,self.position.y,self.radius)
			new_Asteroid_2=Asteroid(self.position.x,self.position.y,self.radius)
			new_Asteroid.velocity=new_angle_1*1.2
			new_Asteroid_2.velocity=new_angle_2*1.2
