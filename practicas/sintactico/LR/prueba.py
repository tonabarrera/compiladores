from lalr import LALR
import pdb

analizador = LALR("gramatica_uno.txt")
analizador.obtener_conjuntos()
analizador.unir_conjuntos()
pdb.set_trace()
# analizador.construir_tabla()
