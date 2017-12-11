from auxiliares import Auxiliares, Tipo
from lr_uno import Conjunto as ConjuntoUno
from lr_cero import Elemento as ElementoCero
from lr_uno import LR_UNO
import pdb


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
        self.numero_dos = None

    def obtener_conjunto_cero(self):
        representacion = set()
        for elemento in self.kernel:
            representacion.add(elemento.ID_CERO)

        return representacion


class LALR(LR_UNO):
    def __init__(self, archivo):
        super(LALR, self).__init__(archivo)

    def cerradura(self, I):
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
                        ele.set_tipo(self.terminales)
                        J.append(ele)

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

    def unir_conjuntos(self):
        lista = list(self.conjuntos)
        i = 0
        nuevos_conjuntos = set()
        print('Lista ' + str(len(lista)))
        while (i < len(lista)):
            temp = lista[i]
            j = i + 1
            agregar = False
            kernel = set()
            numero = ''
            while (j < len(lista)):
                if temp.conjunto_cero == lista[j].conjunto_cero:
                    print('UNION' + str(temp.conjunto) + ' ' + str(lista[j].conjunto_cero))
                    kernel = kernel.union(lista[j].kernel)
                    numero = numero + str(lista[j].numero)
                    lista.pop(j)
                    agregar = True
                j += 1
            if agregar:
                kernel = kernel.union(temp.kernel)
                aux_conjunto = Conjunto(kernel)
                aux_conjunto.conjunto = temp.conjunto
                numero = str(temp.numero) + numero
                aux_conjunto.numero_dos = int(numero)
                aux_conjunto.numero = temp.numero
                nuevos_conjuntos.add(aux_conjunto)
                lista.pop(i)
                print('-------------------')
                i = 0
            else:
                i += 1
        for ele in lista:
            nuevos_conjuntos.add(ele)
        self.conjuntos = nuevos_conjuntos
        pdb.set_trace()

    def ya_existe(self, lista, kernel):
        aux = set()
        for elemento in kernel:
            aux.add(elemento.ID)
        for conjunto in lista:
            if conjunto.repr_kernel == aux:
                return conjunto.numero

        return False