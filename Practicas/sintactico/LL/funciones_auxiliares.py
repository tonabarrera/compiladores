class Auxiliares:
    def primero(N):
        conjunto = set()
        if self.es_terminal(N):
            conjunto.add(N)
        else:
            producciones = self.obtener_producciones(N)
            siguiente = N
            for n in N:
                i = 0
                while True:
                    extra = primero(self.produccion(n, i))
                    conjunto.add(extra)
                    if 'e' in extra:
                        i += 1
                    else:
                        break
        return conjunto

    def siguiente(N):
        conjunto = set()
        if self.es_inicial(N):
            conjunto.add('$')
        # A -> xN
        if self.final(N):
            no_terminales = self.obtener_izquierda(N)
            for n in no_terminales:
                conjunto.add(self.siguiente(n))
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
