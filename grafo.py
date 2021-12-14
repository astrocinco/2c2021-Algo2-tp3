import random

class _Vertice:
    def __init__(self, dato):
        self.dato = dato


class Grafo:
    def __init__(self):
        dict = {}

    def __str__(self): # Revisar si esto es así
        pass

    def agregar_vertice(self, vertice):
        if type(vertice) != _Vertice: # No se si se ecribe así
            return False # Tal vez esto debería ser Raise Error
        self.dict[vertice] = {}
        return True

    def borrar_vertice(self, vertice):
        if vertice not in self.dict:
            return False
        self.dict.pop(vertice) 
        for i in self.dict:
            del i[vertice] # Del no da error cuando intentás sacar y el elemento no está en el diccionario
        return True

    def agregar_arista(self, vertice_1, vertice_2, peso = 1):
        if not self._pertenece(vertice_1) or not self._pertenece(vertice_2):
            return False
        self.dict[vertice_1][vertice_2] = peso
        return True

    def borrar_arista(self, vertice_1, vertice_2):
        if not self.estan_unidos(vertice_1, vertice_2):
            return False
        self.dict[vertice_1].pop(vertice_2)
        return True

    def estan_unidos(self, vertice_1, vertice_2):
        if not self._pertenece(vertice_1) or not self._pertenece(vertice_2):
            return False # Tal vez esto debería ser Raise Error
        return vertice_2 in self.dict[vertice_1]

    def peso_arista(self, vertice_1, vertice_2):
        if not self.estan_unidos(vertice_1, vertice_2):
            return 0
        return self.dict[vertice_1][vertice_2]

    def obtener_vertices(self):
        return self.dict.keys()

    def vertice_aleatorio(self):
        lista = self.obtener_vertices()
        return random.choice(lista)

    def aydacentes(self, vertice):
        return self.dict[vertice].keys()

    def _pertenece(self, vertice):
        return vertice in self.dict