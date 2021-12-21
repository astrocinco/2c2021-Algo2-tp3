from grafo import *
from tp3 import *


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

	camino = camino_mas_corto(grafo,"messi","mbappe")
	print("camino mas corto entre messi y mbappe",camino)


	print("-Messi y mbappe estan unidos: ",grafo.estan_unidos("messi","mbappe"))
	print("-adyacentes de messi: ",grafo.adyacentes("messi"))
	print("borro arista entre messi y mbappe")
	grafo.borrar_arista("messi","mbappe")
	print("-adyacentes de messi: ",grafo.adyacentes("messi"))

'''
def pruebas_volumen():
	print("PRUEBAS VOLUMEN")
	grafo = Grafo()

	for i in range(0,100): #eran de 10000
		grafo.agregar_vertice(i)

	for i in range(len(grafo.obtener_vertices())):
		for j in range(90):
			grafo.agregar_arista(i,j,1)


	camino = camino_mas_corto(grafo,2,3)
	print(camino)
	#print("-adyacentes de 1: ",grafo.adyacentes(1))
'''
def pruebas_varias():
	print("PRUEBAS CON ARISTAS")
	grafo = Grafo()
	grafo.agregar_vertice("1")
	grafo.agregar_vertice("2")
	grafo.agregar_vertice("3")
	grafo.agregar_vertice("4")
	grafo.agregar_vertice("5")

	grafo.agregar_arista("1","2")
	grafo.agregar_arista("2","3")


	camino_mas_corto(grafo,"1","3")



def pruebas_input():
	orden = input("dale\n")
	print(type(orden))

	orden.split('	')
	while orden!= "fin":
		print(orden[0])
		orden = input("dale")




def pruebas():
	pruebas_vertices()
	print("")
	pruebas_aristas()
	print("")
	#pruebas_volumen()
	pruebas_varias()
	print("")
	pruebas_input()

pruebas()