from automata.automatas import AFD, AFN
from expresiones.analizador import Analizador


def correr_analizador():
    print("Ejecutando...")
    analizador = Analizador()
    analizador.convertir_inorden('(a|b)*abb')
    analizador.mostar_expresion_inorden()
    analizador.generar_automata()
    analizador.mostar_automata()


def correr_automata():
    automata = AFN()
    automata.agregar_alfabeto({'a', 'b'})
    automata.agregar_estado(0)
    automata.agregar_estado(1)
    automata.agregar_estado(2)
    automata.agregar_estado(3)

    automata.agregar_inicial(0)
    automata.agregar_finales({3})

    automata.agregar_transicion(0, 1, 'a')
    automata.agregar_transicion(1, 2, 'b')
    automata.agregar_transicion(2, 3, 'b')
    automata.agregar_transicion(0, 0, 'a')
    automata.agregar_transicion(0, 0, 'b')

    if automata.evaluar_cadena('aaabbabbabb'):
        print("Cadena valida")
    else:
        print("Cadena no valida")


#correr_analizador()
correr_automata()
