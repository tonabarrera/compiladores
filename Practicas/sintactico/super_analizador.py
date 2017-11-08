import sys

# host to network short


class SuperAnalizador:
    def __init__(self, token):
        self.token = token
        self.i = 0

    def A(self):
        if self.i == len(self.token):
            print('No valida')
            sys.exit()
        if self.token[self.i] == 'v':
            self.consumir('v')
            self.consumir('a')
            self.consumir('z')
            self.A()
        else:
            self.I()

    def R(self):
        if self.i == len(self.token):
            print('No valida')
            sys.exit()
        if self.token[self.i] == 'a':
            self.consumir('a')
        elif self.token[self.i] == 'n':
            self.consumir('n')
        else:
            print('No valida')
            sys.exit()

    def C(self):
        if self.i == len(self.token):
            print('No valida')
            sys.exit()
        if self.token[self.i] == 'm':
            self.consumir('m')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.R()
            self.consumir('q')
        else:
            print('No valida')
            sys.exit()

    def I(self):
        if self.i == len(self.token):
            print('No valida')
            sys.exit()
        if self.token[self.i] == 'o':
            self.consumir('o')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('a')
            self.consumir('c')
            self.R()
            self.consumir('q')
            self.consumir('z')
            self.I()
        elif self.token[self.i] == 'i':
            self.consumir('i')
            self.consumir('p')
            self.C()
            self.consumir('q')
            self.I()
        elif self.token[self.i] == 'l':
            self.consumir('l')
            self.consumir('p')
            self.C()
            self.consumir('q')
            self.I()
        elif self.token[self.i] == 'f':
            self.consumir('f')
        elif self.token[self.i] == 'b':
            self.consumir('b')
            self.consumir('p')
            self.consumir('a')
            self.consumir('c')
            self.consumir('n')
            self.consumir('q')
            self.consumir('z')
            self.I()
        else:
            self.C()
            self.consumir('z')
            self.I()

    def consumir(self, simbolo):
        if self.i == len(self.token):
            print('No valida')
            sys.exit()
        if simbolo == self.token[self.i]:
            self.i += 1
        else:
            print('No valida')
            sys.exit()
