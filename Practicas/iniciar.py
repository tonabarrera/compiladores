from expresiones.analizador import Analizador


def correr():
    print("Ejecutando...")
    analizador = Analizador()
    analizador.convertir_inorden('a*(b|cd)*')
    print(analizador.salida_inorden)
    analizador.generar_automata()
    for t in analizador.transiciones:
        print(t)

correr()
