# S -> aSb
# S -> c


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
        elif self.token[self.i] == 'c':
            if not self.consumir('c'):
                return False
        else:
            return False
        return True

    def consumir(self, simbolo):
        if self.i >= len(self.token):
            return False
        if simbolo == self.token[self.i]:
            self.i += 1
            return True
        return False
ejem = Analizador('aaaaacbbbbbb')
if ejem.s() and ejem.i == len(ejem.token):
    print('Bien')
else:
    print('Mal')
