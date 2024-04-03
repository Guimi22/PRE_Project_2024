import pygame
from pygame.locals import *

class robot(pygame.sprite.Sprite):# hereda propiedades de una libreria interna de pygame
    def __init__(self, peso, tamaño, carga1,carga2,carga3, direccion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("robot-preview.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        self.speed = [3, 3]
        self.PL = peso  # Peso Limite que puede llevar
        self.cap = tamaño #Tamaño limite que  tiene
        self.carg = (carga1, carga2, carga3) #Que objetos lleva
        self.dir = direccion # Hacia donde se dirige

    def update(self):
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))

    def recoger(self, item):
        self.car = item.sn

    def dejar(self, item):
        self.car = 0

