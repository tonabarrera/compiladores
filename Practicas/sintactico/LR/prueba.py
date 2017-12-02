from analizadores import LR_CERO
import pdb

lr = LR_CERO("gramatica.txt")
lr.obtener_conjuntos()
lr.construir_tabla()
