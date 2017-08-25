from expresiones.analizador import Analizador


def correr():
    analizador = Analizador()
    analizador.ordenar_cadena('(a.c|d)*')
    analizador.generar_automata()


correr()
