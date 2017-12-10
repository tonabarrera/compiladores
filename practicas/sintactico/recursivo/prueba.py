import reglas
from ply.lex import lex
from sintactico import Analizador


class Prueba:
    def __init__(self):
        # Iniciamos nuestro analizador lexico
        self.lexer = lex(module=reglas)

    def analizar(self, cadena):
        entrada = ''
        # Parte del analizador lexico
        self.lexer.input(cadena)
        for token in self.lexer:
            print(token)
            entrada += token.type

        print(entrada)
        # Inicializamos el analizador sintactico
        sintactico = Analizador(entrada)
        resultado = sintactico.A()
        if sintactico.i == len(sintactico.token):
            print('Valida')
        else:
            print('No valida')

analizador = Prueba()
archivo = open('prueba.txt', 'r')
analizador.analizar(archivo.read())
