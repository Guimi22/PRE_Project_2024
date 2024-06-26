class items():
    def __init__(self, serialnumber, peso, tamano, columna, fila, stock, varname):
        self.columnas = {'A': 75, 'B': 200, 'C': 320, 'D':460, 'E':560}
        self.filas = {'1': 400, '2': 320, '3': 240, '4': 160, '5':80}
        self.SN = serialnumber
        self.W = int(peso)
        self.S = int(tamano)
        self.posx = self.posicion_x(columna)
        self.posy = self.posicion_y(fila)
        self.st = int(stock)
        self.name = varname

    #posicion_x(columna) --> Metodo que devuelve la coordenada en el eje horizontal de la pantalla de cada columna.
    def posicion_x(self,columna):
        valor = self.columnas[columna]
        return valor

    #posicion_y(fila) --> Metodo que devuelve la coordenada en el eje vertical de la pantalla de las filas de cada columna.
    def posicion_y(self,fila):
        valor = self.filas[fila]
        return valor

    #diccionario_item() --> Metodo que devuelve un diccionario con clave el numero de serie y de valor una lista con los
    #atributos de cada objeto dentro de la clases items.
    def diccionario_item(self):
        vector_aux = [self.W, self.S, self.posx, self.posy, self.st, self.name]
        dicc = {self.SN: vector_aux}
        return dicc

    #update_stock_item(cantidad, operacion) --> Metodo que actualiza el stock de un item en el almacen segun el robot lo
    #recoja o deje en la estanteria.
    def update_stock_item(self, quantity, operation):
        if operation == 0:
            self.st = self.st - int(quantity)
        else:
            self.st = self.st + int(quantity)
        return self.diccionario_item()
