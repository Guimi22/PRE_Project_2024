import pygame
import time
blanco = (255, 255, 255)
clock = pygame.time.Clock()
Cnum = 0

class MainWindow(pygame.sprite.Sprite):
    def __init__(self, width, height, peso, tamaño, carga1, carga2, carga3):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Almacen")
        self.image = pygame.image.load("robot-preview.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = 440
        self.speed = [3, 3]
        self.TL = tamaño  # limite del robot
        self.PL = peso
        self.car = (carga1, carga2, carga3)  # objetos que lleva encima (sus numeros de serie)
        self.bg = pygame.image.load("almacenBG.png")
    Cnum = 0

    # Funcion para la catualizacion del fondo y el sprite
    def actpantalla(self):
        self.display.fill(blanco)
        self.display.blit(self.bg, (0, 0))
        self.display.blit(self.image, self.rect)
        pygame.display.flip()
        clock.tick(60)

    # Funcion para mover el sprite en las 4 direcciones segun dir
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

    #Funcion para mover el robot hasta un punto deseado de manera eficiente y evitando colisiones
    def ruta(self, x, y):
        pasa = 40
        pasb = 455
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
    # Funcion para actualizar el fondo
    def background(self):
        img = pygame.image.load("almacenBG.png")
        self.display.blit(img, (0,0))

    # Fucnion para devolver el robot a el punto inicial
    def home(self):
        self.ruta(50, 440)

    # Fucnion para mover el robot a el punto de entrega
    def puerta(self):
        self.ruta(625,240)

    #Funcion para la animacion de recogida de un item
    def recoger(self,Cnum):
        self.cambio_cajas(Cnum)
        self.rect.move_ip(0, 0);
        time.sleep(0.5)

    # Funcion para la animacion de soltar un item
    def dejar(self):
        time.sleep(0.5)
        self.image = pygame.image.load("robot2caja.png").convert_alpha()
        time.sleep(0.5)
        self.image = pygame.image.load("robot1caja.png").convert_alpha()
        time.sleep(0.5)
        self.image = pygame.image.load("robot-preview.png").convert_alpha()
        time.sleep(0.5)

   # Funcion para actualizar el sprite del robot y su velocidad segun el numero de cajas que cargue
    def cambio_cajas(self,N):
        match (N):
            case 0:
                self.image = pygame.image.load("robot-preview.png").convert_alpha()
                self.speed = [3, 3]
            case 1:
                self.image = pygame.image.load("robot1caja.png").convert_alpha()
                self.speed = [2, 2]
            case 2:
                self.image = pygame.image.load("robot2caja.png").convert_alpha()
                self.speed =  [2, 2]
            case 3:
                self.image = pygame.image.load("robot3cajas.png").convert_alpha()
                self.speed = [2, 2]