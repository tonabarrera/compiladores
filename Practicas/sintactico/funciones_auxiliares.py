class Auxiliares:
    def primero(X):
        conjunto = set()
        if es_terminal(X):
            conjunto.add(X)
        elif produce_epsilon(X):
            conjunto.add('e')
        else:
            siguiente = X
            while True:
                extra = primero(siguiente)
                if extra.contains('e'):
                    siguiente = self.obtener_siguiente(siguiente)
                else:
                    break
            conjunto.add(extra)

    def siguiente(A):
        conjunto = set()
        if es_inicial(A):
            conjunto.add('$')
