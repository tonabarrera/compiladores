from sintactico import reglas
from sintactico.ply.lex import lex


class AnalizadorLexico:
    def __init__(self):
        self.lexer = lex(module=reglas)

    def analizar(self, cadena):
        self.lexer.input(cadena)
        token = self.lexer.token()

        while token is not None:
            print(token)
            token = self.lexer.token()


analizador = AnalizadorLexico()
archivo = open('prueba.txt', 'r')
analizador.analizar(archivo.read())
