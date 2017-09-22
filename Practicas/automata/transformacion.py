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
        self.AFD.alfabeto = self.AFN.alfabeto
        self.AFD.alfabeto.remove('e')
        estado = self.cerradura_epsilon(self.AFN.estado_inicial)
        actual = SubConjunto(estado, self.etiqueta)
        self.lista.append(actual)
        pendientes = list()
        pendientes.append(actual)
        agregar = True
        self.etiqueta = chr(ord(self.etiqueta) + 1)
        nuevo = None
        while len(pendientes) > 0:
            actual = pendientes.pop()
            for simbolo in self.AFD.alfabeto:
                estados = self.cerradura_epsilon(self.mover(actual.estados, simbolo))
                agregar = True
                for i in self.lista:
                    if i.estados == estados:
                        agregar = False
                        nuevo  = i
                        break
                if agregar:
                    nuevo = SubConjunto(estados, self.etiqueta)
                    pendientes.append(nuevo)
                    self.lista.append(nuevo)
                    self.etiqueta = chr(ord(self.etiqueta) + 1)
                print("Transicion %s -> %s con: %s" % (actual.estados, nuevo.estados, simbolo))
                self.AFD.agregar_transicion(actual.etiqueta, nuevo.etiqueta, simbolo)
        
        for elemento in self.lista:
            if self.AFN.estado_inicial in elemento.estados:
                self.AFD.estado_inicial = elemento.etiqueta
            for final in self.AFN.estados_finales:
                if final in elemento.estados:
                    self.AFD.estados_finales.add(elemento.etiqueta)

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
