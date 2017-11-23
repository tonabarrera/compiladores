from funciones_auxiliares import Auxiliares


class TablaLL(Auxiliares):
    """docstring for TablaLL"""
    def __init__(self):
        super(TablaLL, self).__init__()
        self.terminales = {
            "a": 0,
            "b": 1,
            "$": 2,
        }
        self.no_terminales = {
            "S": 0,
            "A": 1,
            "B": 2,
            "C": 3,
        }

        self.tabla = [[None] * len(self.terminales) for i in range(len(self.no_terminales))]

    def construir_tabla(self):
        produccion_num = 1
        for clave, valor in self.gramatica.items():
            for produccion in valor.get("producciones"):
                primeros = self.primero(produccion)
                for a in primeros:
                    if a != "e":
                        self.agregar_elemento(clave, a, produccion_num)
                if "e" in primeros:
                    siguientes = self.siguiente(clave)
                    for c in siguientes:
                        self.agregar_elemento(clave, c, produccion_num)

                produccion_num += 1

    def agregar_elemento(self, A, a, num):
        if self.tabla[self.no_terminales.get(A)][self.terminales.get(a)] == None:
            self.tabla[self.no_terminales.get(A)][self.terminales.get(a)] = set()
        self.tabla[self.no_terminales.get(A)][self.terminales.get(a)].add(num)

    def mostrar_tabla(self):
        print("Mostrando tabla:")
        for a in self.tabla:
            print(a) 