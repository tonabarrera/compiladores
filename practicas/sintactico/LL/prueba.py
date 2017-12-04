from tabla import TablaLL
# creacion de la tabla LL(1)
gramatica = input("Nombre del archivo: ")
tabla = TablaLL(gramatica)
tabla.construir_tabla()
tabla.mostrar_tabla()
