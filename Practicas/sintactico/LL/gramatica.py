import re
import pdb


class Gramatica:
    """docstring for Gramatica"""
    def __init__(self, archivo):
        self.nombre_archivo = archivo
        self.no_terminales = dict()
        self.terminales = dict()
        self.inicial = None
        self.gramatica = dict()

    def leer_archivo(self):
        archivo = open(self.nombre_archivo, 'r')
        primera = 0
        j = 0
        for linea in archivo:
            if primera == 0:
                self.obtener_no_terminales(linea)
                primera = 1
                continue
            if primera == 1:
                self.inicial = linea[0]
                primera = 2
            j = self.obtener_produccion(linea, j)
        self.terminales.update({"$": j})
        # pdb.set_trace()

    def obtener_produccion(self, linea, j):
        izq = linea[0]
        der = linea[3:]
        der = re.match("[^\n]*", der).group()
        if izq not in self.gramatica:
            self.gramatica.update({izq: {
                "producciones": list(),
                "primero": False,
                "siguiente": False
            }})
        self.gramatica.get(izq).get("producciones").append(der)
        for c in der:
            if re.match("[a-df-z\(\)\+\-\*]", c) is not None and c not in self.terminales:
                self.terminales.update({c: j})
                j += 1
        return j

    def obtener_no_terminales(self, linea):
        i = 0
        for c in linea:
            if re.match("[A-Z]", c) is not None and c not in self.no_terminales:
                self.no_terminales.update({c: i})
                i += 1
