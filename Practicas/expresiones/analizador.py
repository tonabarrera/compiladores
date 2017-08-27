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
                while pila.__len__() > 0 and pila[-1] != '(':
                    self.salida.append(pila.pop())
                try:
                    pila.pop()
                except IndexError as e:
                    raise e
            elif c == '+' or c == '*':
                self.salida.append(c)
            elif c == '|':
                while pila.__len__() > 0 and (pila[-1] == '+' or pila[-1] == '*' or pila[-1] == '.'):
                    self.salida.append(pila.pop())
                pila.append(c)
            elif c == '.':
                while pila.__len__() > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                    self.salida.append(pila.pop())
                pila.append(c)
            else:
                self.salida.append(c)

        while pila.__len__() > 0:
            self.salida.append(pila.pop())

    def generar_automata(self):
        inicial = 1
        final = 2
        pila_transiciones = []
        for c in self.salida:
            if c == '*':
                print('CERRADURA KLEENE')
                s = pila_transiciones.pop()
                i1 = Transicion(s[1]+1, s[0], 'e')
                s1 = Transicion(s[1], s[0], 'e')
                s2 = Transicion(s[1], s[1]+2, 'e')
                i2 = Transicion(s[1]+1, s[1]+2, 'e')
                pila_transiciones.append([s[1]+1, s[1]+2])
                self.transiciones.extend((i1, i2, s1, s2))
            elif c == '+':
                print('CERRADURA DE POSITIVA')
                s = pila_transiciones.pop()
                i1 = Transicion(s[1]+1, s[0], 'e')
                s1 = Transicion(s[1], s[0], 'e')
                s2 = Transicion(s[1], s[1]+2, 'e')
                pila_transiciones.append([s[1]+1, s[1]+2])
                self.transiciones.extend((i1, s1, s2))
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
                print('CONJUNCION')
                t = pila_transiciones.pop()
                s = pila_transiciones.pop()
                for aux in self.transiciones:
                    if aux.siguiente == s[1]:
                        aux.siguiente = t[0]
                pila_transiciones.append([s[0], t[1]])
            else:
                print('ESTADO')
                if pila_transiciones.__len__() > 0:
                    inicial = pila_transiciones[-1][1]+1
                    final = inicial +1
                transicion = Transicion(inicial, final, c)
                pila_transiciones.append([inicial, final])
                self.transiciones.append(transicion)

        print('Inicial: %s Final: %s' % (pila_transiciones[0][0], pila_transiciones[0][1]))