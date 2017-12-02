import pdb
from gramatica import Gramatica
from auxiliares import Auxiliares, Tipo


class Elemento(Tipo):
    def __init__(self, izquierda, derecha, punto):
        self.izq = izquierda
        self.der = derecha
        self.punto = punto
        self.ID = self.izq + "->" + self.der + ':' + str(self.punto)
        self.tipo = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.ID

    def set_tipo(self, terminales):
        if len(self.der) == self.punto:
            self.tipo = self.TIPO_B
        elif self.der[self.punto] in terminales:
            self.tipo = self.TIPO_A


class Conjunto:
    def __init__(self, kernel):
        self.kernel = kernel
        self.repr_kernel = self.obtener_representacion()
        self.conjunto = None
        self.numero = None

    def obtener_representacion(self):
        representacion = set()

        for elemento in self.kernel:
            representacion.add(elemento.ID)

        return representacion

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.repr_kernel) + ":" + str(self.numero)


class LR_CERO(Auxiliares, Tipo):
    def __init__(self, archivo):
        super(LR_CERO, self).__init__(archivo)
        self.leer_archivo()
        self.conjuntos = None
        self.num_columnas = 0
        self.num_filas = 0
        self.tabla = None

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
                        ele = Elemento(A.der[A.punto], pro, 0)
                        ele.set_tipo(self.terminales)
                        J.append(ele)
                agregado[A.der[A.punto]] = True

        J_set = frozenset(J)
        return J_set

    def mover(self, I, X):
        conjunto = set()
        for i in I:
            if i.punto < len(i.der) and i.der[i.punto] == X:
                ele = Elemento(i.izq, i.der, i.punto+1)
                ele.set_tipo(self.terminales)
                conjunto.add(ele)
        return frozenset(conjunto)

    def obtener_conjuntos(self):
        lista = list()
        inicio = set()
        ele = Elemento("W", "E", 0)
        ele.set_tipo(self.terminales)
        inicio.add(ele)
        conjunto_inicio = Conjunto(inicio)
        conjunto_inicio.conjunto = self.cerradura(inicio)
        conjunto_inicio.numero = 0
        indice = 1
        lista.append(conjunto_inicio)
        for i in lista:
            for X in self.no_terminales:
                kernel = self.mover(i.conjunto, X)
                if len(kernel) != 0:
                    if not self.ya_existe(lista, kernel):
                        conjunto_aux = Conjunto(kernel)
                        conjunto_aux.conjunto = self.cerradura(kernel)
                        conjunto_aux.numero = indice
                        lista.append(conjunto_aux)
                        indice += 1

            for X in self.terminales:
                kernel = self.mover(i.conjunto, X)
                if len(kernel) != 0:
                    if not self.ya_existe(lista, kernel):
                        conjunto_aux = Conjunto(kernel)
                        conjunto_aux.conjunto = self.cerradura(kernel)
                        conjunto_aux.numero = indice
                        lista.append(conjunto_aux)
                        indice += 1

        self.conjuntos = set(lista)
        self.num_columnas = len(self.terminales) + len(self.no_terminales)
        self.num_filas = indice
        self.tabla = [["err"] * self.num_columnas for i in range(self.num_filas)]

    def ya_existe(self, lista, kernel):
        aux = set()
        for elemento in kernel:
            aux.add(elemento.ID)
        for conjunto in lista:
            if conjunto.repr_kernel == aux:
                return conjunto.numero

        return False

    def construir_tabla(self):
        contador_reducir = 1
        for I in self.conjuntos:
            for X, valor in self.no_terminales.items():
                temp = self.mover(I.conjunto, X)
                num = self.ya_existe(self.conjuntos, temp)
                if num:
                    self.tabla[I.numero][valor-1] = num
            for elemento in I.conjunto:
                if elemento.tipo == self.TIPO_A:
                    temp = self.mover(I.conjunto, elemento.der[elemento.punto])
                    num = self.ya_existe(self.conjuntos, temp)
                    if num:
                        self.tabla[I.numero][len(self.no_terminales)+self.terminales.get(elemento.der[elemento.punto])-1] = "d"+str(num)

                if elemento.tipo == self.TIPO_B:
                    if elemento.izq != "W":
                        siguientes = self.siguiente(elemento.izq)
                        for sig in siguientes:
                            self.tabla[I.numero][len(self.no_terminales)+self.terminales.get(sig)-1] = "r" + str(contador_reducir)
                    else:
                        self.tabla[I.numero][len(self.no_terminales)+self.terminales.get("$")-1] = "ACE"
                    contador_reducir += 1

        self.imprimir_tabla()

    def imprimir_tabla(self):
        print("Tabla LR(0):")
        for t in self.no_terminales.keys():
            print(t, end="\t")

        for t in self.terminales.keys():
            print(t, end="\t")

        print("estado")

        for fila, edo in zip(self.tabla, range(self.num_filas)):
            for columna in fila:
                print(columna, end="\t")
            print(edo)


class LALR(object):
    """docstring for LALR"""
    def __init__(self, arg):
        super(LALR, self).__init__()
        self.arg = arg
