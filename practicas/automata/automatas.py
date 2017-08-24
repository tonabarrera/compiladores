class Transicion:
    def __init__(self, actual, siguiente, caracter):
        self.actual = actual
        self.siguiente = siguiente
        self.caracter = caracter


class AFN:
    def __init__(self):
        self.alfabeto = []
        self.estados_finales = []
        self.estado_inicial = 0
        self.estados_actuales = []
        self.transiciones = []

    def agregar_transicion(self, actual, siguiente, caracter):
        self.transiciones.append(Transicion(actual, siguiente, caracter))

    def agregar_final(self, estado):
        self.estados_finales.append(estado)

    def agregar_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto
        self.alfabeto.append('e')

    def agregar_iniciar(self, estado):
        self.estado_inicial = estado

    def evaluar_cadena(self, cadena):
        self.estados_actuales = self.estados_epsilon(self.estado_inicial)
        for caracter in cadena:
            self.estados_actuales = self.estados_epsilon(self.evaluar_estado(self.estados_actuales, caracter))

        for estado in self.estados_actuales:
            if estado in self.estados_finales:
                return True
        return False

    def evaluar_estado(self, estados, c):
        aux = []
        for estado in estados:
            for transicion in self.transiciones:
                if estado == transicion.estado_actual and transicion.caracter == c:
                    aux.append(transicion.siguiente)
        return aux

    def estados_epsilon(self, estados):
        return []


class AFD(AFN):
    def agregar_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def evaluar_cadena(self, cadena):
        self.estados_actuales.append(self.estado_inicial)
        for caracter in cadena:
            if self.alfabeto.contains(caracter):
                return
            for transicion in self.transiciones:
                if transicion.actual == self.estados_actuales[0]:
                    if transicion.caracter == caracter:
                        self.estados_actuales[0] = transicion.siguiente
                        break

        return self.estados_actuales[0] in self.estados_finales
