import pdb
from gramatica import Gramatica


class Elemento:
    def __init__(self, izquierda, derecha, punto):
        self.izq = izquierda
        self.der = derecha
        self.punto = punto
        self.ID = self.izq + "->" + self.der + ': ' + str(self.punto)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.ID


class LR_CERO(Gramatica):
    def __init__(self, archivo):
        super(LR_CERO, self).__init__(archivo)
        self.leer_archivo()

    def es_terminal(self, A):
        return A in self.terminales

    def cerradura(self, I):
        J = list(I)
        agregado = dict()
        for A in J:
            if not self.es_terminal(A.der[A.punto]):
                if A.der[A.punto] not in agregado:
                    agregado.update({A.der[A.punto]: False})
                producciones = self.obtener_izq(A.der[A.punto])
                for pro in producciones:
                    if not agregado.get(A.der[A.punto]):
                        J.append(Elemento(A.der[A.punto], pro, 0))
                agregado[A.der[A.punto]] = True
        
        J_set = frozenset(J)
        return J_set

    def mover(self, I, X):
        conjunto = set()
        for i in I:
            if i.der[i.punto] == X:
                conjunto.add(Elemento(i.izq, i.der, i.punto+1))
        return frozenset(conjunto)

    def obtener_conjuntos(self, conjunto):
        C = set()
        C.add(conjunto)
        pdb.set_trace()
        for no_term in self.no_terminales.keys():
            C.add(self.mover(conjunto, no_term))
        for term in self.terminales.keys():
            C.add(self.mover(conjunto, term))
        pdb.set_trace()
        return C


class LR_UNO(object):
    """docstring for LR_UNO"""
    def __init__(self, arg):
        super(LR_UNO, self).__init__()
        self.arg = arg


class LALR(object):
    """docstring for LALR"""
    def __init__(self, arg):
        super(LALR, self).__init__()
        self.arg = arg