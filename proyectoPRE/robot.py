class robot:
    def __init__(self, peso, tamaño, posicion, carga):
        self.pos = posicion
        self.tam = tamaño
        self.pes = peso
        self.car = carga
    def recoger(self, item):
        self.car = item.sn
    def dejar(self, item):
        self.car = 0

