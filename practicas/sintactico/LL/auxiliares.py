from gramatica import Gramatica
import re


class Auxiliares(Gramatica):
    """Clase que contiene la implementacion de los
    metodos primero y siguiente"""
    def __init__(self, archivo):
        """Se envia el nombre del archivo
        a la clase padre"""
        super(Auxiliares, self).__init__(archivo)

    def es_epsilon(self, A):
        return A == 'e'

    def es_terminal(self, A):
        return A not in self.gramatica

    def es_inicial(self, S):
        return self.inicial == S

    def primero(self, A):
        """Metodo que calcula primero de una cadena"""
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
        """Metodo que calcula primero de un solo simbolo"""
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
        """Metodo para el calculo de siguiente
        se inicializan los banderas que indican si ya
        se calculo siguiente"""
        for clave, valor in self.gramatica.items():
            valor["siguiente"] = False
        return self.S(N)

    def S(self, N):
        """Calculo de siguiente"""
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
        """Obtiene la parte izquierda de una produccion"""
        claves = list()
        for clave, valor in self.gramatica.items():
            for v in valor.get("producciones"):
                if N == v[len(v)-1]:
                    claves.append(clave)
        return claves

    def obtener_derecha(self, N):
        """Obtiene la parte derecha de una produccion"""
        simbolos = list()
        for clave, valor in self.gramatica.items():
            for v in valor.get("producciones"):
                for m in re.finditer(N, v):
                    if m.start() != len(v)-1:
                        simbolos.append({
                            "clave": clave,
                            "cadena": v[m.start()+1:]
                            })
        return simbolos
