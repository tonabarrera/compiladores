import pdb


class Auxiliares:
    def __init__(self):
        self.producciones = {
            "E": ["TR"],
            "R": ["+TR", "e"],
            "T": ["FY"],
            "Y": ["*FY", "e"],
            "F": ["(E)", "i"],
        }
        self.inicial = "E"

    def es_epsilon(self, N):
        return N == 'e'

    def es_terminal(self, N):
        return N not in self.producciones

    def primero(self, N):
        conjunto = set()
        for n in N:
            conjunto_extra = self.p(n)
            conjunto.update(conjunto_extra)
            if 'e' not in conjunto_extra:
                if 'e' in conjunto:
                    conjunto.remove('e')
                break

        return conjunto

    def p(self, N):
        conjunto = set()
        if self.es_terminal(N) or self.es_epsilon(N):
            conjunto.add(N)
        else:
            producciones = self.producciones[N]
            for n in producciones:
                i = 0
                while i < len(n):
                    extra = self.primero(n[i])
                    conjunto.update(extra)
                    # pdb.set_trace()

                    if 'e' in extra:
                        i += 1
                    else:
                        break
        return conjunto

    def es_inicial(self, N):
        return self.inicial == N

    def siguiente(self, N):
        conjunto = set()
        if self.es_inicial(N):
            conjunto.add('$')
        # A -> xN
        if self.final(N):
            no_terminales = self.obtener_izquierda(N)
            for n in no_terminales:
                conjunto.update(self.siguiente(n))
        if self.medio(N):
            simbolos = self.obtener_derecha(N)
            for n in simbolos:
                primero = self.primero(n)
                if 'e' in primero:
                    no_terminales = self.obtener_producciones(N)
                    for i in no_terminales:
                        conjunto.add(self.siguiente(i))
                else:
                    conjunto.add(primero)
        return conjunto
