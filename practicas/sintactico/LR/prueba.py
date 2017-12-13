from lr_cero import LR_CERO
#from lr_uno import LR_UNO
#from lalr import LALR
import pdb

analizador = LR_CERO("gramatica_uno.txt")
analizador.obtener_conjuntos()
# analizador.unir_conjuntos()
# pdb.set_trace()
analizador.construir_tabla()
