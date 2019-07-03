import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
        
	def __init__(self):
		Sprite.__init__(self)
		self.imagen = util.cargar_imagen('imagenes/Chicken.png')
		self.rect = self.imagen.get_rect()
		self.rect.move_ip(310, 450)
		self.vida = 100
		self.puntaje = 0
                self.puntaje_maximo = '10'
                
	def leer_archivo(self):
                f = open('Puntaje.txt','r')
                self.puntaje_maximo = f.read()
                f.close()
                
        def escribir_archivo(self):
                f = open('Puntaje.txt','w')
                f.write(str(self.puntaje_maximo))
                f.close()
                
	def update(self):
		teclas = pygame.key.get_pressed()
           	if teclas[K_LEFT] and self.rect.x>=10:
			self.rect.x -= 10
		if teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
			self.rect.x += 10
		if teclas[K_UP] and self.rect.y>=10:
			self.rect.y -= 10
                        self.puntaje+=1
                        if self.puntaje>int(self.puntaje_maximo):
                                self.puntaje_maximo=str(self.puntaje)
		if teclas[K_UP] and self.rect.y<=10:
                        self.rect.y=450
                elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
			self.rect.y += 10

