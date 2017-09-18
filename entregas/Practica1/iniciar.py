from automatas import AFN, AFD

class Principal:
    def correr_automata_AFN(self):
        print("---Automata no determinista pruebas---")
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


    def correr_automata_AFD(self):
        print("---Automata determinista pruebas---")
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

iniciar = Principal()
iniciar.correr_automata_AFN()
iniciar.correr_automata_AFD()
