from analizadores import LR_CERO, Elemento
import pdb

lr = LR_CERO("gramatica.txt")
inicio = set()
elemento_inicio = Elemento("W", "E", 0)
inicio.add(elemento_inicio)
a = lr.cerradura(inicio)
lr.obtener_conjuntos(a)
pdb.set_trace()
