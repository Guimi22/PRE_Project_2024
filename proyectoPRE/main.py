from almacen import *
from Ventana import MainWindow

ancho_pantalla = 640
alto_pantalla = 480
ini =(50,440)
blanco = (255, 255, 255)

def main():

    pygame.init()
    item1 = items(4, 20, 33434, 200, 300,3)
    item1 = items(4, 20, 33434, 160, 300,3)

    p = MainWindow(ancho_pantalla,alto_pantalla,3,3,3,3,3)
    dirx = 200
    diry = 200

    MainWindow.ruta(p,dirx,diry)
    MainWindow.ruta(p,ini[0],ini[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
