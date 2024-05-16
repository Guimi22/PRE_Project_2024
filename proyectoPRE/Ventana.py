import pygame
from pygame.locals import *
blanco = (255, 255, 255)
clock = pygame.time.Clock()

class MainWindow(pygame.sprite.Sprite):
    def __init__(self, width, height, peso, tamaño, carga1, carga2, carga3):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Almacen")
        self.image = pygame.image.load("robot-preview.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        self.speed = [1, 1]
        self.TL = tamaño  # limite del robot
        self.PL = peso
        self.car = (carga1, carga2, carga3)  # objetos que lleva encima (sus numeros de serie)


    def actpantalla(self):
        self.display.fill(blanco)
        self.display.blit(self.image, self.rect)
        pygame.display.flip()
        clock.tick(60)

    def mover(self, dir):
        match (dir):
            case 1:
                self.rect.move_ip((self.speed[1], 0))
            case 2:
                self.rect.move_ip((-self.speed[1], 0))
            case 3:
                self.rect.move_ip((0, self.speed[1]))
            case 4:
                self.rect.move_ip((0, -self.speed[1]))

    def ruta(self, x, y):
        pasa = 40
        pasb = 440
        if (self.rect.top - pasa) > abs(self.rect.top - pasb):
            pas = pasb
        else:
            pas = pasa

        if self.rect.bottom < pas:
            while self.rect.bottom < pas:
                self.mover(3)
                self.actpantalla()
        else:
            while self.rect.bottom > pas:
                self.mover(4)
                self.actpantalla()

        if self.rect.right < x:
            while self.rect.right < x:
                self.mover(1)
                self.actpantalla()
        else:
            while self.rect.right > x:
                self.mover(2)
                self.actpantalla()

        if self.rect.bottom < y:
            while self.rect.bottom < y:
                self.mover(3)
                self.actpantalla()
        else:
            while self.rect.bottom > y:
                self.mover(4)
                self.actpantalla()

    def espera(self):
        self.rect.move_ip(0, 0);

    def recoger(self, item):
        self.car = item.sn

    def dejar(self, item):
        self.car = 0;
