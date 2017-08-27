from expresiones.analizador import Analizador


def correr():
    print("Ejecutando...")
    analizador = Analizador()
    analizador.ordenar_cadena(')')
    analizador.generar_automata()
    for t in analizador.transiciones:
        print(t)

correr()
