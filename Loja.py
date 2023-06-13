import math

class Loja(object):
    numero = int()
    x = int()
    y = int()
    destinos = []

    def __init__(self, numero, x, y, destinos):
        self.numero = numero
        self.x = x
        self.y = y
        self.destinos =  destinos