from grafo import *

def pruebas_vertices():

	print("PRUEBAS DE VERTICES")
	grafo = Grafo()
	grafo.agregar_vertice("1")
	grafo.agregar_vertice("2")
	grafo.agregar_vertice("3")

	vertices = grafo.obtener_vertices()
	for i in vertices:
		print(i)

	aleatorio = grafo.vertice_aleatorio()
	print("vertice aleatorio: ",aleatorio)



def pruebas():
	pruebas_vertices()
	print("")



pruebas()
