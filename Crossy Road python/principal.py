import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption( "Crossy Road" )
      fuente = pygame.font.Font(None, 30)
      background_image = util.cargar_imagen('imagenes/fondo.jpg');
      pierde_vida = util.cargar_sonido('sonidos/Pierde.wav')
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()
      heroe = Heroe()
      heroe.leer_archivo()
      villano = [Villano((0,57),3),Villano((400,57),3), Villano((250,10),5),Villano((210,157),4),Villano((0,205),1),Villano((400,205),1), Villano((0,250),4),Villano((120,295),3),Villano((0,340),2),Villano((400,340),2),Villano((280,390),3)]
      while jugando:
          heroe.update()
          if heroe.vida <= 0:
              jugando = False
          texto_puntaje = fuente.render("Puntaje: " + str(heroe.puntaje), 1, (250, 250, 250))
          texto_puntajeMax= fuente.render("Record: " + str(heroe.puntaje_maximo) , 2, (250, 250, 250))
          for n in villano:
              n.update()
          heroe.image = heroe.imagen
          for n in villano:
              if heroe.rect.colliderect(n.rect):
                  pierde_vida.play()
                  heroe.vida -= 100
                  heroe.escribir_archivo()
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          screen.blit(background_image, (0,0))
          screen.blit(heroe.imagen, heroe.rect)
          for n in villano:
              screen.blit(n.image, n.rect)
          screen.blit(texto_puntaje, (20, 10))
          screen.blit(texto_puntajeMax, (300, 10))

          pygame.display.update()
          pygame.time.delay(20)


if __name__ == '__main__':
      game()
