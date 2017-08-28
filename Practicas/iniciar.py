from automata.automatas import AFD, AFN
from expresiones.analizador import Analizador


def correr_analizador():
    print("Ejecutando...")
    analizador = Analizador()
    analizador.convertir_inorden('a*(b|cd)*')
    analizador.mostar_expresion_inorden()
    analizador.generar_automata()
    analizador.mostar_automata()


def correr_automata():
    automata = AFN()
    automata.agregar_alfabeto({'1', 'x'})
    automata.agregar_estado(0)
    automata.agregar_estado(1)
    automata.agregar_estado(2)
    automata.agregar_estado(3)

    automata.agregar_inicial(0)
    automata.agregar_finales({0, 3})

    automata.agregar_transicion(0, 1, '1')
    automata.agregar_transicion(1, 0, '1')
    automata.agregar_transicion(0, 2, 'e')
    automata.agregar_transicion(2, 3, 'x')

    if automata.evaluar_cadena('111x111'):
        print("Cadena valida")
    else:
        print("Cadena no valida")


# correr_analizador()
correr_automata()
