class _Vertice:
    def __init__(self, dato):
        self.dato = dato


class Grafo:
    def __init__(self):
        dict = {}

    def __str__(self): # Revisar si esto es así
        pass

    def agregar_vertice(self, vertice):
        self.dict[vertice] = {}

    def borrar_vertice(self, vertice):
        self.dict.pop(vertice) # IR UNO POR UNO Y SACAR DEL RESTO DE VERTICES CUALQUIER CONEXION CON ESTE
        # HACER

    def agregar_arista(self, vertice_1, vertice_2, peso = 1):
        # Y SI NO EXISTE ALGUNO DE LOS DOS VERTICES?
        self.dict[vertice_1][vertice_2] = peso

    def borrar_arista(self, vertice_1, vertice_2):
        # Revisar que vertice_2 estaba en vertice 1?
        self.dict[vertice_1].pop(vertice_2)

    def estan_unidos(self, vertice_1, vertice_2):
        pass

    def peso_arista(self, vertice_1, vertice_2):
        pass

    def obtener_vertices(self):
        pass

    def vertice_aleatorio(self):
        pass

    def aydacentes(self, vertice):
        pass
