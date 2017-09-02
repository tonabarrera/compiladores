from automata.automatas import AFD, AFN
from automata.transformacion import Transformacion
from expresiones.analizador import Analizador


def correr_analizador():
    print("Ejecutando...")
    analizador = Analizador()
    analizador.convertir_inorden('(a|b)*abb')
    analizador.mostar_expresion_inorden()
    analizador.generar_automata()
    analizador.mostar_automata()


def correr_automata_AFN():
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
    for n in range(5):
        cadena = input("-Ingresa una cadena: ")
        print("La cadena es:")
        if automata.evaluar_cadena(cadena):
            print("Valida")
        else:
            print("No valida")


def correr_automata_AFD():
    automata = AFD()
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
    automata.agregar_transicion(0, 0, 'b')
    automata.agregar_transicion(1, 1, 'a')
    automata.agregar_transicion(2, 1, 'a')
    automata.agregar_transicion(3, 1, 'a')
    automata.agregar_transicion(3, 0, 'b')

    for n in range(5):
        cadena = input("-Ingresa una cadena: ")
        print("La cadena es:")
        if automata.evaluar_cadena(cadena):
            print("Valida")
        else:
            print("No valida")


def transformar_automata():
    automata = AFN()
    automata.agregar_alfabeto({'a', 'b'})

    automata.agregar_estado(0)
    automata.agregar_estado(1)
    automata.agregar_estado(2)
    automata.agregar_estado(3)
    automata.agregar_estado(4)
    automata.agregar_estado(5)
    automata.agregar_estado(6)
    automata.agregar_estado(7)
    automata.agregar_estado(8)
    automata.agregar_estado(9)
    automata.agregar_estado(10)

    automata.agregar_inicial(0)
    automata.agregar_finales({10})

    automata.agregar_transicion(0, 1, 'e')
    automata.agregar_transicion(1, 2, 'e')
    automata.agregar_transicion(1, 4, 'e')
    automata.agregar_transicion(0, 7, 'e')
    automata.agregar_transicion(2, 3, 'a')

    automata.agregar_transicion(4, 5, 'b')
    automata.agregar_transicion(3, 6, 'e')
    automata.agregar_transicion(5, 6, 'e')
    automata.agregar_transicion(6, 1, 'e')
    automata.agregar_transicion(6, 7, 'e')
    automata.agregar_transicion(7, 8, 'a')
    automata.agregar_transicion(8, 9, 'b')
    automata.agregar_transicion(9, 10, 'b')

    transformer = Transformacion()
    transformer.AFN = automata
    transformer.convertir_automata()
    for a in transformer.AFD.transiciones:
        print(a)


# correr_analizador()
correr_automata_AFD()
# correr_automata_AFN
# transformar_automata()
