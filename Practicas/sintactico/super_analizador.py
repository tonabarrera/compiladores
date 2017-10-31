# host to network short
class SuperAnalizador:
    def __init__(self, token):
        self.token = token
        self.i = 0

    def A(self):
        if self.token[self.i] == 'v':
            self.consumir('v')
            self.consumir('a')
            self.consumir('z')
            self.A()
        else:
            self.I()

    def I(self):
        if self.token[self.i] == 'o':
            self.consumir('o')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('a')
            self.consumir('c')
            self.consumir('n')
            self.consumir('q')
            self.consumir('z')
            self.I()
        elif self.token[self.i] == 'm':
            self.consumir('m')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('a')
            self.consumir('q')
            self.consumir('z')
            self.I()
        elif self.token[self.i] == 'i':
            self.consumir('i')
            self.consumir('p')
            self.consumir('m')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('a')
            self.consumir('q')
            self.consumir('q')
            self.I()
        elif self.token[self.i] == 'l':
            self.consumir('l')
            self.consumir('p')
            self.consumir('m')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('a')
            self.consumir('q')
            self.consumir('q')
            self.I()
        elif self.token[self.i] == 'f':
            self.consumir('f')
        else:
            return False

    def consumir(self, simbolo):
        if simbolo == self.token[self.i]:
            self.i += 1
