# Cosas bien chidas como la cerradura epsilon y los movimientos que los estados de este subconjunto pueden hacer
# para pasar de un automata no deterministico a uno deterministico al puro estilo del libro de compiladores
# mañana lo hago, solo es programar el algoritmo del libro y sha
import pdb
from automata.automatas import AFD
class SubConjunto:
    def __init__(self, estados, etiqueta):
        self.estados = estados
        self.etiqueta = etiqueta

class Transformacion:
    def __init__(self):
        self.estados_deterministicos = list()
        self.lista = list()
        self.AFN = None
        self.AFD = AFD()
        self.etiqueta = 'A'

    def convertir_automata(self):
        self.AFD.alfabeto = {'a', 'b'}
        estado = self.cerradura_epsilon(self.AFN.estado_inicial)
        actual = SubConjunto(estado, self.etiqueta)
        self.lista.append(actual)
        #self.estados_deterministicos.append(estado) # un nuevo estado
        pendientes = list()
        pendientes.append(actual)
        agregar = False
        self.etiqueta = chr(ord(self.etiqueta)+1)

        while len(pendientes) > 0:
            actual = pendientes.pop()
            for simbolo in self.AFD.alfabeto:
                estados = self.mover(actual.estados, simbolo)
                na = self.cerradura_epsilon(estados)
                if na == actual.estados:
                    print("Entro")
                    nuevo = actual
                else:
                    nuevo = SubConjunto(na, self.etiqueta)
                for i in self.lista:
                    if len(na) > 0 and (na != i.estados):
                        agregar = True
                    else:
                        agregar = False
                        nuevo = i
                        break 
                if agregar:
                    self.lista.append(nuevo)
                    pendientes.append(nuevo)
                    self.etiqueta = chr(ord(self.etiqueta)+1)
                    agregar = False
                print("La transicion %s (%s) -> %s (%s) : %s" % (actual.estados, actual.etiqueta, nuevo.estados, nuevo.etiqueta, simbolo))
                self.AFD.agregar_transicion(actual.etiqueta, nuevo.etiqueta, simbolo)
        for ga in self.lista:
            if self.AFN.estado_inicial in ga.estados:
                self.AFD.estado_inicial = ga.etiqueta
            for final in self.AFN.estados_finales:
                if final in ga.estados:
                    self.AFD.estados_finales.add(ga.etiqueta)
        print("Estado inicial %s" % self.AFD.estado_inicial)
        print("Estados finales %s" % self.AFD.estados_finales)
        #pdb.set_trace()

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
        return estados_epsilon

    def mover(self, estados, simbolo):
        estados_aux = set()
        for estado in estados:
            for transicion in self.AFN.transiciones:
                if simbolo != 'e' and estado == transicion.actual and transicion.caracter == simbolo:
                    estados_aux.add(transicion.siguiente)
        return estados_aux
