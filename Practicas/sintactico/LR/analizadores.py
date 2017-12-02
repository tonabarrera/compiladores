import pdb
from gramatica import Gramatica


class Elemento:
    def __init__(self, izquierda, derecha, punto):
        self.izq = izquierda
        self.der = derecha
        self.punto = punto
        self.ID = self.izq + "->" + self.der + ':' + str(self.punto)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.ID


class Estado:
    def __init__(self, simbolo, conjunto, numero, anterior):
        self.anterior = anterior
        self.simbolo = simbolo
        self.conjunto = conjunto
        self.numero = numero

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.anterior) + "->" + str(self.numero) + ":" + self.simbolo


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
            if A.punto < len(A.der) and not self.es_terminal(A.der[A.punto]):
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
            if i.punto < len(i.der) and i.der[i.punto] == X:
                conjunto.add(Elemento(i.izq, i.der, i.punto+1))
        return frozenset(conjunto)

    def obtener_conjuntos(self):
        inicio = set()
        elemento_inicio = Elemento("W", "E", 0)
        inicio.add(elemento_inicio)
        a = self.cerradura(inicio)
        edo_inicio = Estado("INICIO", a, 0, -1)
        C = list()
        C.append(edo_inicio)
        pdb.set_trace()
        i = 1
        agregado = dict()
        agregado.update({str(edo_inicio): True})
        for esta in C:
            for no_term in self.no_terminales.keys():
                aux = self.mover(esta.conjunto, no_term)
                if len(aux) != 0:
                    temp = self.cerradura(aux)
                    if len(temp) != 0:
                        existe = self.ya_existe(C, temp)
                        if not existe:
                            edo = Estado(no_term, temp, i, esta.numero)
                            agregado.update({str(edo): True})
                            C.append(edo)
                            i += 1
                        else:
                            edo = Estado(no_term, temp, existe, esta.numero)
                            if str(edo) not in agregado:
                                agregado.update({str(edo): True})
                                C.append(edo)
                            else:
                                if not agregado.get(str(edo)):
                                    C.append(edo)

            for term in self.terminales.keys():
                aux = self.mover(esta.conjunto, term)
                if len(aux) != 0:
                    temp = self.cerradura(aux)
                    if len(temp) != 0:
                        existe = self.ya_existe(C, temp)
                        if not existe:
                            edo = Estado(term, temp, i, esta.numero)
                            agregado.update({str(edo): True})
                            C.append(edo)
                            i += 1
                        else:
                            edo = Estado(term, temp, existe, esta.numero)
                            if str(edo) not in agregado:
                                agregado.update({str(edo): True})
                                C.append(edo)
                            else:
                                if not agregado.get(str(edo)):
                                    C.append(edo)

        pdb.set_trace()
        return C

    def ya_existe(self, lista, conjunto):
        aux = set()
        pdb.set_trace()
        for estado in conjunto:
            aux.add(estado.ID)
        for estado in lista:
            aux2 = set()
            for elemento in estado.conjunto:
                aux2.add(elemento.ID)
            if aux == aux2:
                return estado.numero

        return False


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