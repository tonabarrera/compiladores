from sintactico.LR.lr_cero import Elemento as ElementoCero
from sintactico.LR.lr_cero import Conjunto as ConjuntoCero

from sintactico.LR.lr_cero import LR_CERO


class Elemento(ElementoCero):
    def __init__(self, izquierda, derecha, punto, terminal):
        super(Elemento, self).__init__(izquierda, derecha, punto)
        self.terminal = terminal
        self.ID = self.ID + "," + self.terminal


class Conjunto(ConjuntoCero):
    def __init__(self, kernel):
        super(Conjunto, self).__init__(kernel)


class LR_UNO(LR_CERO):
    def __init__(self, archivo):
        super(LR_UNO, self).__init__(archivo)

    def cerradura(self, I):
        agregado = dict()
        for i in I:
            agregado.update({str(i): True})
        J = list(I)
        for A in J:
            if A.punto < len(A.der) and self.es_no_terminal(A.der[A.punto]):
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
        inicial = Elemento(self.extendido, self.inicial, 0, "$")
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

    def construir_tabla(self):
        print('PRODUCCIONES:')
        self.imprimir_gramatica()
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
                    if elemento.izq != self.extendido:
                        llave = elemento.izq + '->' + elemento.der
                        r = self.gramatica_id.get(llave)
                        i = I.numero
                        j = len(self.no_terminales)+self.terminales.get(elemento.terminal)-1
                        self.agregar_elemento(i, j, "r" + str(r))
                    else:
                        i = I.numero
                        j = len(self.no_terminales)+self.terminales.get('$')-1
                        self.agregar_elemento(i, j, 'ACC')
        self.imprimir_tabla("Tabla LR(1):")
