import re
import pdb
import string


class Gramatica:
    def __init__(self, archivo):
        self.nombre_archivo = archivo
        self.no_terminales = dict()
        self.terminales = dict()
        self.inicial = None
        self.gramatica = dict()
        self.gramatica_id = dict()
        self.extendido = None

    def leer_archivo(self):
        archivo = open(self.nombre_archivo, 'r')
        primera = 0
        j = 1
        for linea in archivo:
            if primera == 0:
                self.guardar_no_terminales(linea)
                primera = 1
                continue
            if primera == 1:
                self.inicial = linea[0]
                primera = 2
            j = self.guardar_produccion(linea, j)
        self.terminales.update({"$": j})

        for caracter in string.ascii_uppercase:
            if caracter not in self.no_terminales:
                self.extendido = caracter
                break

    def guardar_produccion(self, linea, j):
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
            expr_regular = re.match("[a-df-z\(\)\+\-\*]", c)
            if expr_regular is not None and c not in self.terminales:
                self.terminales.update({c: j})
                j += 1
        return j

    def obtener_izq(self, N):
        return self.gramatica.get(N).get("producciones")

    def guardar_no_terminales(self, linea):
        i = 1
        for c in linea:
            expr_regular = re.match("[A-Z]", c)
            if expr_regular is not None and c not in self.no_terminales:
                self.no_terminales.update({c: i})
                i += 1
