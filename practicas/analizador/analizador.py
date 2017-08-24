from analizador.arbol import Nodo

class Analizador:
    def __init__(self, cadena):
        self.cadena = cadena
        self.arbol = None
        self.pila = []
        self.pilaTransiciones = []

    def analizar(self):
        cont_id = 0
        self.arbol = Nodo()
        self.arbol.idNodo = cont_id
        nodo_actual = self.arbol
        for c in self.cadena:
            cont_id = cont_id + 1
            print(nodo_actual.idNodo)
            if c == '(':
                nodo = Nodo()
                nodo.idNodo = cont_id
                nodo_actual.izq = nodo
                self.pila.append(nodo_actual)
                nodo_actual = nodo_actual.izq
            elif c == '|' or c == '.' or c == '*' or c=='+':
                nodo_actual.valor = c
                nodo = Nodo()
                nodo.idNodo = cont_id
                nodo_actual.der = nodo
                self.pila.append(nodo_actual)
                nodo_actual = nodo_actual.der
            elif c == ')':
                if self.pila.__len__() > 0:
                    nodo_actual = self.pila.pop()
            else:
                nodo_actual.valor = c
                if self.pila.__len__() > 0:
                    nodo_actual = self.pila.pop()
                else:
                    nodo = Nodo()
                    nodo.idNodo = cont_id
                    nodo.izq = nodo_actual
                    nodo_actual = nodo

        self.arbol = nodo_actual

    def postorden(self, arbol=None):
        if arbol is None:
            return 0
        self.postorden(arbol.izq)
        self.postorden(arbol.der)
        #crearTransicion(arbol.valor)
        print("%s %s" %(arbol.valor, arbol.idNodo))

    def crearTransicion(self, valor):
        aux = pilaTransiciones.pop()