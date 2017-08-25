from automata.automatas import Transicion


class Analizador:
    def __init__(self):
        self.salida = []
        self.transiciones = []

    def ordenar_cadena(self, cadena):
        pila = []
        for c in cadena:
            if c == '(':
                pila.append(c)
            elif c == ')':
                aux = pila.pop()
                while aux != '(':
                    self.salida.append(aux)
                    if pila.__len__() < 1:
                        break
                    aux = pila.pop()
            elif c == '+' or c == '*':
                self.salida.append(c)
            elif c == '|':
                if pila.__len__() > 0:
                    while pila[-1] == '+' or pila[-1] == '*' or pila[-1] == '.':
                        self.salida.append(pila.pop())
                pila.append(c)
            elif c == '.':
                if pila.__len__() > 0:
                    while pila[-1] == '+' or pila[-1] == '*':
                        self.salida.append(pila.pop())
                pila.append(c)
            else:
                self.salida.append(c)

        while pila.__len__() > 0:
            self.salida.append(pila.pop())

    def generar_automata(self):
        actual = 0
        pila_transiciones = []
        for c in self.salida:
            if c == '+':
                pass
            elif c == '*':
                pass
            elif c == '|':
                pass
            elif c == '.':
                pass
            else:
                transicion = Transicion(actual, actual+1, c)
                pila_transiciones.append(transicion)
                self.transiciones.append(transicion)
                actual = actual + 2