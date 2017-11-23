from funciones_auxiliares import Auxiliares


class TablaLL(Auxiliares):
    """docstring for TablaLL"""
    def __init__(self):
        super(TablaLL, self).__init__()
        self.terminales = {
            "i": 0,
            "+": 1,
            "*": 3,
            "(": 4,
            ")": 5,
            "$": 6,
        }
        self.no_terminales = {
            "E": 0,
            "R": 1,
            "T": 2,
            "Y": 3,
            "F": 4,
        }

        self.tabla = [[0] * len(self.terminales)] * len(self.no_terminales)

    def construir_tabla(self):
        produccion_num = 1
        for clave, valor in self.gramatica.items():
            for produccion in valor.get("producciones"):
                primeros = self.primero(clave)
                #sprint(primeros)
                for a in primeros:
                    if a != "e":
                        print(clave + " " + a + " " + str(produccion_num))
                produccion_num += 1

    def mostrar_tabla(self):
        print("Mostrando tabla:")
        for a in self.tabla:
            print(a) 