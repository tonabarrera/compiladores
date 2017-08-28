class Transicion:
    def __init__(self, actual, siguiente, caracter):
        self.actual = actual
        self.siguiente = siguiente
        self.caracter = caracter

    def __str__(self):
        return '{}->{}: {}'.format(self.actual, self.siguiente, self.caracter)


class AFN:
    def __init__(self):
        self.alfabeto = set()
        self.estados_finales = set()
        self.estado_inicial = 0
        self.estados_actuales = []
        self.transiciones = []
        self.estados = set()

    def agregar_transicion(self, actual, siguiente, caracter):
        self.transiciones.append(Transicion(actual, siguiente, caracter))

    def agregar_finales(self, estados):
        self.estados_finales = estados

    def agregar_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto
        self.alfabeto.add('e')

    def agregar_inicial(self, estado):
        self.estado_inicial = estado

    def agregar_estado(self, estado):
        if estado in self.estados:
            print("Estado repetido")
        else:
            self.estados.add(estado)

    def evaluar_cadena(self, cadena):
        self.estados_actuales = self.estados_epsilon(self.estado_inicial)
        for caracter in cadena:
            if not (caracter in self.alfabeto):
                return False
            siguientes_estados = self.obtener_siguientes(caracter)
            self.estados_actuales = []
            for e in siguientes_estados:
                self.estados_actuales.extend(self.estados_epsilon(e))

        for estado in self.estados_actuales:
            if estado in self.estados_finales:
                return True
        return False

    def obtener_siguientes(self, caracter):
        siguientes = []
        for estado in self.estados_actuales:
            for transicion in self.transiciones:
                if estado == transicion.actual and transicion.caracter == caracter:
                    siguientes.append(transicion.siguiente)
        return siguientes

    def estados_epsilon(self, estados):
        estados_epsilon = []
        if type(estados) is list:
            estados_epsilon.extend(estados)
        else:
            estados_epsilon.append(estados)
        for estado in estados_epsilon:
            for t in self.transiciones:
                if t.caracter == 'e' and t.actual == estado and (not t.siguiente in estados_epsilon):
                    estados_epsilon.append(t.siguiente)
        return estados_epsilon

class AFD(AFN):
    def agregar_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def evaluar_cadena(self, cadena):
        self.estados_actuales.append(self.estado_inicial)
        for caracter in cadena:
            if not (caracter in self.alfabeto):
                return False
            for transicion in self.transiciones:
                if transicion.actual == self.estados_actuales[0]:
                    if transicion.caracter == caracter:
                        self.estados_actuales[0] = transicion.siguiente
                        break

        return self.estados_actuales[0] in self.estados_finales
