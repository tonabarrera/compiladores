from sintactico.LR.lr_uno import Conjunto as ConjuntoUno
from sintactico.LR.lr_cero import Elemento as ElementoCero
from sintactico.LR.lr_uno import LR_UNO


class Elemento(ElementoCero):
    def __init__(self, izquierda, derecha, punto, terminal):
        super(Elemento, self).__init__(izquierda, derecha, punto)
        self.terminal = terminal
        self.ID_CERO = self.ID
        self.ID = self.ID + "," + self.terminal


class Conjunto(ConjuntoUno):
    def __init__(self, kernel):
        super(Conjunto, self).__init__(kernel)
        self.conjunto_cero = self.obtener_conjunto_cero()

    def obtener_conjunto_cero(self):
        representacion = set()
        for elemento in self.kernel:
            representacion.add(elemento.ID_CERO)

        return representacion


class LALR(LR_UNO):
    def __init__(self, archivo):
        super(LALR, self).__init__(archivo)

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
                    if not super(LALR, self).ya_existe(lista, kernel):
                        conjunto_aux = Conjunto(kernel)
                        conjunto_aux.conjunto = self.cerradura(kernel)
                        conjunto_aux.numero = indice
                        lista.append(conjunto_aux)
                        indice += 1

            for X in self.terminales:
                kernel = self.mover(con.conjunto, X)
                if len(kernel) != 0:
                    if not super(LALR, self).ya_existe(lista, kernel):
                        conjunto_aux = Conjunto(kernel)
                        conjunto_aux.conjunto = self.cerradura(kernel)
                        conjunto_aux.numero = indice
                        lista.append(conjunto_aux)
                        indice += 1

        self.conjuntos = set(lista)
        self.num_columnas = len(self.terminales) + len(self.no_terminales)
        self.num_filas = indice

    def unir_conjuntos(self):
        lista = list(self.conjuntos)
        i = 0
        nuevos_conjuntos = set()
        while i < len(lista):
            temp = lista[i]
            j = i + 1
            agregar = False
            kernel = set()
            otros_conjuntos = set()
            while j < len(lista):
                if temp.conjunto_cero == lista[j].conjunto_cero:
                    kernel = kernel.union(lista[j].kernel)
                    otros_conjuntos = otros_conjuntos.union(lista[j].conjunto)
                    lista.pop(j)
                    agregar = True
                j += 1
            if agregar:
                kernel = kernel.union(temp.kernel)
                aux_conjunto = Conjunto(kernel)
                otros_conjuntos = otros_conjuntos.union(temp.conjunto)
                aux_conjunto.conjunto = otros_conjuntos
                aux_conjunto.numero = None
                nuevos_conjuntos.add(aux_conjunto)
                lista.pop(i)
                i = 0
            else:
                i += 1
        numero_conjuntos = len(lista) + len(nuevos_conjuntos)
        indices = [True] * numero_conjuntos
        self.conjuntos = set()
        for ele in lista:
            if ele.numero < numero_conjuntos:
                self.conjuntos.add(ele)
                indices[ele.numero] = False
            else:
                conta = 0
                while not indices[conta]:
                    conta += 1
                ele.numero = conta
                indices[ele.numero] = False
                self.conjuntos.add(ele)
        j = 0
        lista_conjuntos = list(nuevos_conjuntos)
        while j < len(lista_conjuntos):
            conta = 0
            while not indices[conta]:
                conta += 1
            lista_conjuntos[j].numero = conta
            indices[conta] = False
            self.conjuntos.add(lista_conjuntos[j])
            j += 1
        self.num_filas = len(self.conjuntos)
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
        self.imprimir_tabla("Tabla LALR:")

    def ya_existe(self, lista, kernel):
        aux = set()
        for elemento in kernel:
            aux.add(elemento.ID_CERO)
        for conjunto in lista:
            if conjunto.conjunto_cero == aux:
                return conjunto.numero

        return False
