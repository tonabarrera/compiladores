class Nodo:
    """docstring for Nodo"""
    def __init__(self, tipo, hijos=None, hoja=None):
        self.tipo = tipo
        if hijos:
            self.hijos = hijos
        else:
            self.hijos = list()
        self.hoja = hoja

    def __str__(self):
        return self.tipo

    def __repr__(self):
        return str(self)