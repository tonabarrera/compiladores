from funciones_auxiliares import Auxiliares
from tabla import TablaLL
import pdb
gramatica = input("Nombre del archivo: ")
g = TablaLL(gramatica)
g.construir_tabla()
g.mostrar_tabla()
