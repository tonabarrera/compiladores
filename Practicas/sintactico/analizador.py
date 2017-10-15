class Analizador(object):
    def __init__(self, token):
        self.token = token
        self.i = 0

    def s(self):
        if self.token[self.i] == 'a':
            if not self.consumir('a'):
                return False
            if not self.s():
                return False
            if not self.consumir('b'):
                return False
            return True
        if self.token[self.i] == 'c':
            return self.consumir('c')
        else:
            return False

    def consumir(self, simbolo):
        if simbolo == self.token[self.i]:
            self.i += 1
            return True
        return False

ejem = Analizador('aabb')
print(ejem.s())
