from auxiliares import Auxiliares


class TablaLL(Auxiliares):
    """Clase para la creacion y despliegue de la tabla LL(1)
    utilizando los metodos contenidos en la clase padre Auxiliares"""
    def __init__(self, archivo):
        """Se recibe el nombre del archivo y se pasa a la clase padres"""
        super(TablaLL, self).__init__(archivo)
        self.leer_archivo()
        self.num_filas = len(self.no_terminales)
        self.num_colum = len(self.terminales)
        self.tabla = [[None] * self.num_colum for i in range(self.num_filas)]

    def construir_tabla(self):
        """Implementacion del algoritmo para el
        llenado de la tabla"""
        produccion_num = 1
        for clave, valor in self.gramatica.items():
            for produccion in valor.get("producciones"):
                primeros = self.primero(produccion)
                for a in primeros:
                    if a != "e":
                        self.agregar_elemento(clave, a, produccion_num)
                if "e" in primeros:
                    siguientes = self.siguiente(clave)
                    for c in siguientes:
                        self.agregar_elemento(clave, c, produccion_num)

                produccion_num += 1

    def agregar_elemento(self, A, a, num):
        """Metodo que agrega un elemento a la tabla"""
        i = self.no_terminales.get(A)
        j = self.terminales.get(a)
        if self.tabla[i][j] is None:
            self.tabla[i][j] = set()
        self.tabla[i][j].add(num)

    def mostrar_tabla(self):
        """Metodo que muestra la tabla"""
        print("Tabla LL(1):")
        print("    ", end="")
        for t in self.terminales.keys():
            print(t, end="\t")
        print("")
        for f, n in zip(self.tabla, self.no_terminales.keys()):
            for c in f:
                print(c, end="\t")
            print(n)
