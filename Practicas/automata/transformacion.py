# Cosas bien chidas como la cerradura epsilon y los movimientos que los estados de este subconjunto pueden hacer
# para pasar de un automata no deterministico a uno deterministico al puro estilo del libro de compiladores
# mañana lo hago, solo es programar el algoritmo del libro y sha

class Transformacion:
    def __init__(self):
        self.estados_deterministicos = list()
        self.AFN = None
        self.AFD = None

    def convertir_automata(self):
        estado = self.cerradura_epsilon(self.AFD.estado_inicial)
        self.estados_deterministicos.append(estado)
        for simbolo in self.AFN.alfabeto:
            estados = self.mover(self.estados_deterministicos[0], simbolo)
            if not estados in self.estados_deterministicos:
                self.estados_deterministicos.append(estados)


    def cerradura_epsilon(self, estados):
        estados_epsilon = set()
        estados_epsilon.update(estados)
        for estado in estados_epsilon:
            for t in self.AFN.transiciones:
                if t.caracter == 'e' and t.actual == estado and (not t.siguiente in estados_epsilon):
                    estados_epsilon.add(t.siguiente)
        return estados_epsilon

    def mover(self, estados, simbolo):
        estadosD = set()
        for estado in estados:
            for transicion in self.AFN.transiciones:
                if estado == transicion.actual and transicion.simbolo == simbolo:
                    estadosD.add(transicion.siguiente)
        return estadosD
