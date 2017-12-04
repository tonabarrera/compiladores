from automata.automatas import Transicion
from automata.automatas import AFN

class Analizador:
    def __init__(self):
        self.salida_postfijo = list()
        self.transiciones = list()
        self.pila_transiciones = []
        self.POSITIVA = 0
        self.KLEENE = 1
        self.AFN = AFN()

    def mostar_expresion_postfijo(self):
        print(self.salida_postfijo)

    def mostar_automata(self):
        print('Inicial: %s Finales: %s' % (self.AFN.estado_inicial, self.AFN.estados_finales))
        print("Transiciones:")
        for t in self.AFN.transiciones:
            print(t)

    def convertir_postfijo(self, cadena):
        pila = []
        punto = False
        for c in cadena:
            if c == '(':
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.salida_postfijo.append(pila.pop())
                    pila.append('.')
                    punto = False
                pila.append(c)
            elif c == ')':
                punto = True
                while len(pila) > 0 and pila[-1] != '(':
                    self.salida_postfijo.append(pila.pop())
                try:
                    pila.pop()
                except IndexError as e:
                    raise e
            elif c == '+' or c == '*':
                self.salida_postfijo.append(c)
            elif c == '|':
                while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*' or pila[-1] == '.'):
                    self.salida_postfijo.append(pila.pop())
                pila.append(c)
                punto = False
            else:
                if punto:
                    while len(pila) > 0 and (pila[-1] == '+' or pila[-1] == '*'):
                        self.salida_postfijo.append(pila.pop())
                    pila.append('.')
                punto = True
                self.salida_postfijo.append(c)

        while len(pila) > 0:
            self.salida_postfijo.append(pila.pop())

    def generar_automata(self):
        inicial = 1
        final = 2
        self.AFN.alfabeto.add('e')
        for c in self.salida_postfijo:
            if c == '*':
                print('CERRADURA KLEENE')
                s = self.pila_transiciones.pop()
                self.cerradura(s, self.KLEENE)
            elif c == '+':
                print('CERRADURA DE POSITIVA')
                s = self.pila_transiciones.pop()
                self.cerradura(s, self.POSITIVA)
            elif c == '|':
                print("UNION")
                s = self.pila_transiciones.pop()
                t = self.pila_transiciones.pop()
                i1 = Transicion(s[1] + 1, s[0], 'e')
                i2 = Transicion(s[1] + 1, t[0], 'e')
                f1 = Transicion(s[1], s[1] + 2, 'e')
                f2 = Transicion(t[1], s[1] + 2, 'e')
                self.pila_transiciones.append([s[1] + 1, s[1] + 2])
                self.transiciones.extend((i1, i2, f1, f2))
            elif c == '.':
                print('CONCATENACION')
                t = self.pila_transiciones.pop()
                s = self.pila_transiciones.pop()
                for aux in self.transiciones:
                    if aux.siguiente == s[1]:
                        aux.siguiente = t[0]
                self.pila_transiciones.append([s[0], t[1]])
            else:
                print('ESTADO')
                if self.pila_transiciones.__len__() > 0:
                    inicial = self.pila_transiciones[-1][1] + 1
                    final = inicial + 1
                transicion = Transicion(inicial, final, c)
                self.pila_transiciones.append([inicial, final])
                self.transiciones.append(transicion)
                self.AFN.alfabeto.add(c)

        self.AFN.agregar_inicial(self.pila_transiciones[0][0])
        self.AFN.agregar_finales({self.pila_transiciones[0][1]})
        self.AFN.transiciones = self.transiciones

    def cerradura(self, s, tipo):
        i1 = Transicion(s[1] + 1, s[0], 'e')
        s1 = Transicion(s[1], s[0], 'e')
        s2 = Transicion(s[1], s[1] + 2, 'e')
        self.pila_transiciones.append([s[1] + 1, s[1] + 2])
        self.transiciones.extend((i1, s1, s2))

        if tipo == self.KLEENE:
            i2 = Transicion(s[1] + 1, s[1] + 2, 'e')
            self.transiciones.append(i2)
