import pygame
from pygame.sprite import Sprite
from pygame import *
import util
from random import randint

class Villano(Sprite):
	def __init__(self,coord,vel):
                i=randint(0,5)
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/carro'+str(i)+'.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		self.dir = "l"
		self.velocidad=vel
        
	def update(self):
		if self.dir == "l":
			self.rect.x -= self.velocidad
		if self.rect.x<=0:
                        self.rect.x=608
			self.dir="1"
		elif self.rect.x>0:
                        self.rect.x -= self.velocidad
