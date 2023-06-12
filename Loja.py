import math

class Loja(object):
    numeroLoja = int()
    x = int()
    y = int()
    listaDeEntrega = []

    def __init__(self, numeroLoja, x, y, listaDeEntrega):
        self.numeroLoja = numeroLoja
        self.x = x
        self.y = y
        self.listaDeEntrega =  listaDeEntrega