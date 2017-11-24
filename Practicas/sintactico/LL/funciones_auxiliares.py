import pdb
import re
from gramatica import Gramatica


class Auxiliares(Gramatica):
    def __init__(self, archivo):
        super(Auxiliares, self).__init__(archivo)

    def es_epsilon(self, A):
        return A == 'e'

    def es_terminal(self, A):
        return A not in self.gramatica

    def es_inicial(self, S):
        return self.inicial == S

    def primero(self, A):
        conjunto = set()
        for a in A:
            if a in self.gramatica:
                self.gramatica.get(a)["primero"] = False
            conjunto_extra = self.P(a)
            conjunto.update(conjunto_extra)
            if 'e' not in conjunto_extra:
                if 'e' in conjunto:
                    conjunto.remove('e')
                break
        return conjunto

    def P(self, A):
        conjunto = set()
        if self.es_terminal(A) or self.es_epsilon(A):
            conjunto.add(A)
        else:
            if self.gramatica.get(A).get("primero"):
                return conjunto
            else:
                self.gramatica.get(A)["primero"] = True

            producciones = self.gramatica.get(A).get("producciones")
            for produccion in producciones:
                i = 0
                while i < len(produccion):
                    extra = self.P(produccion[i])
                    conjunto.update(extra)
                    if 'e' in extra:
                        i += 1
                    else:
                        break
        return conjunto

    def siguiente(self, N):
        for clave, valor in self.gramatica.items():
            valor["siguiente"] = False
        return self.S(N)

    def S(self, N):
        conjunto = set()
        if not self.es_terminal(N) and self.gramatica.get(N).get("siguiente"):
            return conjunto
        else:
            if not self.es_terminal(N):
                self.gramatica.get(N)["siguiente"] = True

        if self.es_inicial(N):
            conjunto.add('$')
        # A -> xN
        no_terminales = self.obtener_izquierda(N)
        if len(no_terminales) != 0:
            for n in no_terminales:
                conjunto.update(self.S(n))
        # A -> xNy
        no_terminales = self.obtener_derecha(N)
        if len(no_terminales) != 0:
            for simbolo in no_terminales:
                primero = self.primero(simbolo.get("cadena"))
                if 'e' in primero:
                    primero.remove('e')
                    conjunto.update(self.S(simbolo.get("clave")))
                conjunto.update(primero)
        if not self.es_terminal(N):
            self.gramatica.get(N)["siguiente"] = False
        return conjunto

    def obtener_izquierda(self, N):
        claves = list()
        for clave, valor in self.gramatica.items():
            for v in valor.get("producciones"):
                if N == v[len(v)-1]:
                    claves.append(clave)
        return claves

    def obtener_derecha(self, N):
        simbolos = list()
        for clave, valor in self.gramatica.items():
            for v in valor.get("producciones"):
                for m in re.finditer(N, v):
                    if m.start() != len(v)-1:
                        simbolos.append({"clave": clave, "cadena": v[m.start()+1:]})
        return simbolos

    def obtener_producciones(self, N):
        claves = list()
        for clave, valor in self.gramatica.items():
            for v in valor.get("producciones"):
                if v.find(N) != -1:
                    claves.append(clave)
        return claves
