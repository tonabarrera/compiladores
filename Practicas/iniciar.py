from expresiones.analizador import Analizador


def correr():
    print("Ejecutando")
    analizador = Analizador()
    analizador.ordenar_cadena('a|d|c')
    analizador.generar_automata()
    for t in analizador.transiciones:
        print(t)

correr()
