from automatas import AFD, AFN
from analizador import Analizador

class Principal:
    def correr_analizador(self):
        print("Generando el automata de la expresion: (a|b)*abb ...")
        analizador = Analizador()
        # Transformamos la expresion a postfijo
        analizador.convertir_postfijo('(a|b)*abb')
        analizador.mostar_expresion_postfijo()
        # Creamos el AFN a partir de la expresion en postfijo
        analizador.generar_automata()
        analizador.mostar_automata()
        # Probamos nuestro automata con algunas cadenas
        print("Pruebas sobre el automata generado...")
        automataAFN = analizador.AFN
        for n in range(5):
            cadena = input("-Ingresa una cadena: ")
            print("La cadena es:")
            if automataAFN.evaluar_cadena(cadena):
                print("Valida")
            else:
                print("No valida")


iniciar = Principal()
iniciar.correr_analizador()
