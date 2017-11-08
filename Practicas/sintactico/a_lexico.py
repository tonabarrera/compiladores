import reglas
from ply.lex import lex
from super_analizador import SuperAnalizador


class AnalizadorLexico:
    def __init__(self):
        self.lexer = lex(module=reglas)

    def analizar(self, cadena):
        entrada = ''
        self.lexer.input(cadena)
        for token in self.lexer:
            entrada += token.type

        print(entrada)

        sintactico = SuperAnalizador(entrada)
        resultado = sintactico.A()
        if sintactico.i == len(sintactico.token):
            print('Valida')
        else:
            print('No valida')

analizador = AnalizadorLexico()
archivo = open('prueba.txt', 'r')
analizador.analizar(archivo.read())
