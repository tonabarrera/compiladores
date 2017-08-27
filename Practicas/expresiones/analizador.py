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
        inicial = 0
        final = 1
        pila_transiciones = []
        for c in self.salida:
            if c == '+':
                pass
            elif c == '*':
                pass
            elif c == '|':
                print("UNION")
                s = pila_transiciones.pop()
                t = pila_transiciones.pop()
                i1 = Transicion(s[1]+1, s[0], 'e')
                i2 = Transicion(s[1]+1, t[0], 'e')
                f1 = Transicion(s[1], s[1]+2, 'e')
                f2 = Transicion(t[1], s[1]+2, 'e')
                pila_transiciones.append([s[1]+1, s[1]+2])
                self.transiciones.extend((i1, i2, f1, f2))
            elif c == '.':
                pass
            else:
                print('ESTADO')
                if pila_transiciones.__len__() > 0:
                    inicial = pila_transiciones[-1][1]+1
                    final = inicial +1
                transicion = Transicion(inicial, final, c)
                pila_transiciones.append([inicial, final])
                self.transiciones.append(transicion)

        print('Inicial: %s Final: %s' % (pila_transiciones[0][0], pila_transiciones[0][1]))