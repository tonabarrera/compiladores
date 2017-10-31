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
        print(sintactico.i)
        print(len(sintactico.token))
        if sintactico.i == len(sintactico.token):
            print('Valido')
        else:
            print('No valido')
            print(sintactico.token[sintactico.i])

analizador = AnalizadorLexico()
archivo = open('prueba.txt', 'r')
analizador.analizar(archivo.read())
