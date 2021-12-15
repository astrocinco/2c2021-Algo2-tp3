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
	print("-vertice aleatorio: ",aleatorio)

	print("borro vertice 1")
	print("-vertices:")
	grafo.borrar_vertice("1")
	
	
	vertices = grafo.obtener_vertices()
	for i in vertices:
		print(i)
	
def pruebas_aristas():
	print("PRUEBAS CON ARISTAS")
	grafo = Grafo()
	grafo.agregar_vertice("messi")
	grafo.agregar_vertice("haaland")
	grafo.agregar_vertice("mbappe")
	print("vertices: messi, haaland, mbappe")
	grafo.agregar_arista("messi","haaland",100)
	print("Uno messi y haaland con peso 100")
	print("-Messi y haaland estan unidos: ",grafo.estan_unidos("messi","haaland"))
	print("-peso entre messi y haaland: ",grafo.peso_arista("messi","haaland"))
	print("uno messi con mbappe con peso 50")
	grafo.agregar_arista("messi","mbappe",50)
	print("-Messi y mbappe estan unidos: ",grafo.estan_unidos("messi","mbappe"))
	print("-adyacentes de messi: ",grafo.adyacentes("messi"))
	print("borro arista entre messi y mbappe")
	grafo.borrar_arista("messi","mbappe")
	print("-adyacentes de messi: ",grafo.adyacentes("messi"))


def pruebas_volumen():
	print("PRUEBAS VOLUMEN")
	grafo = Grafo()

	for i in range(0,2000): #eran de 10000
		grafo.agregar_vertice(i)

	for i in range(len(grafo.obtener_vertices())):
		for j in range(1000):
			grafo.agregar_arista(i,j,j)

	#print("-adyacentes de 1: ",grafo.adyacentes(1))
	print("ta bien")


def pruebas():
	pruebas_vertices()
	print("")
	pruebas_aristas()
	print("")
	pruebas_volumen()


pruebas()