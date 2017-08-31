# Cosas bien chidas como la cerradura epsilon y los movimientos que los estados de este subconjunto pueden hacer
# para pasar de un automata no deterministico a uno deterministico al puro estilo del libro de compiladores
# mañana lo hago, solo es programar el algoritmo del libro y sha


class Transformacion:
    def __init__(self):
        self.estados_deterministicos = list()
        self.AFN = None
        self.AFD = None

    def convertir_automata(self):
        estado = self.cerradura_epsilon(self.AFN.estado_inicial)
        self.estados_deterministicos.append(estado) # un nuevo estado
        pendientes = list()
        pendientes.append(estado)
        while pendientes.__len__() > 0:
            actual = pendientes.pop()
            for simbolo in self.AFN.alfabeto:
                estados = self.mover(actual, simbolo)
                na = self.cerradura_epsilon(estados)
                if na not in self.estados_deterministicos:
                    pendientes.append(na)
                    self.estados_deterministicos.append(na)
        print("break")


    # recibe un solo elemento o un conjunto de estados
    def cerradura_epsilon(self, estados):
        estados_epsilon = set()
        aux = list()
        if type(estados) is set:
            aux.extend(estados)
        else:
            aux.append(estados)
        for estado in aux:
            for t in self.AFN.transiciones:
                if t.caracter == 'e' and t.actual == estado and (t.siguiente not in aux):
                    aux.append(t.siguiente)

        estados_epsilon.update(aux)
        print("adios")
        return estados_epsilon

    def mover(self, estados, simbolo):
        estados_aux = set()
        for estado in estados:
            for transicion in self.AFN.transiciones:
                if estado == transicion.actual and transicion.caracter == simbolo:
                    estados_aux.add(transicion.siguiente)
        return estados_aux
