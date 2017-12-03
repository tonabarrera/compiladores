from auxiliares import Auxiliares, Tipo


class LALR(Auxiliares, Tipo):
    """docstring for LALR"""
    def __init__(self, archivo):
        super(LALR, self).__init__(archivo)
        self.leer_archivo()

    def construir_tabla(self):
        pass

    def imprimir_tabla(self):
        pass