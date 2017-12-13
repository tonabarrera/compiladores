from lr_cero import LR_CERO
from lr_uno import LR_UNO
from lalr import LALR
import pdb

archivo = input('Introduce el nombre del archivo con la gramatica plis: ')
tipo = input("""Tipos de tabla
    1) LR(0)
    2) LR(1)
    3) LALR
Selecciona alguna: """)
if int(tipo) == 1:
    analizador = LR_CERO(archivo)
    analizador.obtener_conjuntos()
elif int(tipo) == 2:
    analizador = LR_UNO(archivo)
    analizador.obtener_conjuntos()
else:
    analizador = LALR(archivo)
    analizador.obtener_conjuntos()
    analizador.unir_conjuntos()
analizador.construir_tabla()
