from funciones_auxiliares import Auxiliares
import pdb


class TablaLL(Auxiliares):
    """docstring for TablaLL"""
    def __init__(self, archivo):
        super(TablaLL, self).__init__(archivo)
        self.leer_archivo()
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
        pdb.set_trace()
        if self.tabla[self.no_terminales.get(A)][self.terminales.get(a)] is None:
            self.tabla[self.no_terminales.get(A)][self.terminales.get(a)] = set()
        self.tabla[self.no_terminales.get(A)][self.terminales.get(a)].add(num)

    def mostrar_tabla(self):
        print("Tabla LL(1):")
        print("    ", end="")
        for t in self.terminales.keys():
            print(t, end="\t")
        print("")
        for f, n in zip(self.tabla, self.no_terminales.keys()):
            for c in f:
                print(c, end="\t")
            print(n)
