from analizadores import LR_CERO, Elemento, Estado
import pdb

lr = LR_CERO("gramatica.txt")
lr.obtener_conjuntos()
pdb.set_trace()
