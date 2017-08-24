from analizador.analizador import Analizador
def main():
    analizador = Analizador('(a*|b)')
    analizador.analizar()
    analizador.postorden(analizador.arbol)

main()
