from lr_cero import Elemento as ElementoCero
from lr_cero import Conjunto as ConjuntoCero
from auxiliares import Tipo, Auxiliares
import pdb


class Elemento(ElementoCero):
    def __init__(self, izquierda, derecha, punto, terminal):
        super(Elemento, self).__init__(izquierda, derecha, punto)
        self.terminal = terminal
        self.ID = self.ID + "," + self.terminal


class Conjunto(ConjuntoCero):
    def __init__(self, kernel):
        super(Conjunto, self).__init__(kernel)


class LR_UNO(Auxiliares, Tipo):
    def __init__(self, archivo):
        super(LR_UNO, self).__init__(archivo)
        self.leer_archivo()
        self.conjuntos = None
        self.num_columnas = 0
        self.num_filas = 0
        self.tabla = None

    def cerradura(self, I):
        agregado = dict()
        for i in I:
            agregado.update({str(i): True})
        # pdb.set_trace()
        J = list(I)
        for A in J:
            if A.punto < len(A.der) and not self.es_terminal(A.der[A.punto]):
                B = A.der[A.punto]
                producciones = self.obtener_izq(B)
                for pro in producciones:
                    sub_cadena = A.der[A.punto+1:]
                    sub_cadena += A.terminal
                    primeros = self.primero(sub_cadena)
                    for pri in primeros:
                        ele = Elemento(B, pro, 0, pri)
                        if str(ele) not in agregado:
                            ele.set_tipo(self.terminales)
                            J.append(ele)
                            agregado.update({str(ele): True})
                            #pdb.set_trace()
                # pdb.set_trace()

        return set(J)

    def mover(self, I, X):
        J = set()
        for i in I:
            if i.punto < len(i.der) and i.der[i.punto] == X:
                ele = Elemento(i.izq, i.der, i.punto+1, i.terminal)
                ele.set_tipo(self.terminales)
                J.add(ele)

        return J

    def obtener_conjuntos(self):
        lista = list()
        inicial = Elemento("W", "S", 0, "$")
        inicial.set_tipo(self.terminales)
        inicio = set()
        inicio.add(inicial)
        conjunto_inicio = Conjunto(inicio)
        conjunto_inicio.conjunto = self.cerradura(inicio)
        conjunto_inicio.numero = 0
        indice = 1
        lista.append(conjunto_inicio)
        for con in lista:
            for X in self.no_terminales:
                kernel = self.mover(con.conjunto, X)
                if len(kernel) != 0:
                    if not self.ya_existe(lista, kernel):
                        conjunto_aux = Conjunto(kernel)
                        conjunto_aux.conjunto = self.cerradura(kernel)
                        conjunto_aux.numero = indice
                        lista.append(conjunto_aux)
                        indice += 1

            for X in self.terminales:
                kernel = self.mover(con.conjunto, X)
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
        print('PRODUCCIONES:')
        contador_gramatica = 1
        for I in self.conjuntos:
            for A, valor in self.no_terminales.items():
                temp = self.mover(I.conjunto, A)
                num = self.ya_existe(self.conjuntos, temp)
                if num:
                    i = I.numero
                    j = valor-1
                    self.agregar_elemento(i, j, num)

            for elemento in I.conjunto:
                if elemento.tipo == self.TIPO_A:
                    temp = self.mover(I.conjunto, elemento.der[elemento.punto])
                    num = self.ya_existe(self.conjuntos, temp)
                    if num:
                        i = I.numero
                        j = len(self.no_terminales)+self.terminales.get(elemento.der[elemento.punto])-1
                        self.agregar_elemento(i, j, "d"+str(num))

                if elemento.tipo == self.TIPO_B:
                    if elemento.izq != "W":
                        llave = elemento.izq + '->' + elemento.der
                        r = 0
                        if llave in self.gramatica_id:
                            r = self.gramatica_id.get(llave)
                        else:
                            self.gramatica_id.update({llave: contador_gramatica})
                            r = contador_gramatica
                            print(str(r) + ' ' + elemento.izq + '->' + elemento.der)
                            contador_gramatica += 1
                        i = I.numero
                        j = len(self.no_terminales)+self.terminales.get(elemento.terminal)-1
                        self.agregar_elemento(i, j, "r" + str(r))
                    else:
                        i = I.numero
                        j = len(self.no_terminales)+self.terminales.get('$')-1
                        self.agregar_elemento(i, j, 'ACC')
        self.imprimir_tabla()

    def agregar_elemento(self, i, j, num):
        """Metodo que agrega un elemento a la tabla"""
        if self.tabla[i][j] == "err":
            self.tabla[i][j] = set()
        self.tabla[i][j].add(num)

    def imprimir_tabla(self):
        print("Tabla LR(1):")
        for t in self.no_terminales.keys():
            print(t, end="\t")

        for t in self.terminales.keys():
            print(t, end="\t")

        print("estado")

        for fila, edo in zip(self.tabla, range(self.num_filas)):
            for columna in fila:
                print(columna, end="\t")
            print(edo)