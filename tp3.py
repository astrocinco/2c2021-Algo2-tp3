from typing import Deque
from grafo import *
import heapq
import csv


def pruebas_input_terminal(input_terminal):
	with open(input_terminal[1]) as archi:
		lineas = csv.reader(archi, delimiter='\t') # Revisar que no esté cargando todo el archivo en memoria
		contador = 0
		for linea in lineas:
			#print(f"Acá el primer elemento de cada linea: {linea[0]} {contador}")
			print(f"Lista entera: {linea}\n\n")
			contador += 1
	print("Fin")



def tsv_to_vert(nombre_tsv, grafo = Grafo()):
    with open(nombre_tsv) as archivo:
        cont = csv.reader(archivo, delimiter="\t") # Revisar carg mem, revisar ""
        for linea in cont:
            for elem in linea:
                grafo.agregar_vertice(elem)
                if len(linea) != 1:
                    if elem == linea[0]:
                        continue
                    grafo.agregar_arista(linea[0], elem)
    return grafo



def dijkstra(grafo,vertices,padres, origen,destino): #O(E*Log(v))
    distancia = {}
    for v in grafo.obtener_vertices():
        distancia[v] = float('inf')
    distancia[origen] = 0
    padres[origen] = None
    heap = []
    heapq.heappush(heap,origen)

    while heap:
        v = heapq.heappop(heap)
        for w in grafo.adyacentes(v):
            if (distancia[v] + grafo.peso_arista(v,w) < distancia[w]):
                distancia[w] = distancia[v] + grafo.peso_arista(v,w)
                padres[w] = v
                heapq.heappush(heap,w)
    
    return padres,distancia[destino]



def reconstruir_camino(padres, inicio, fin):
    v = fin
    camino = []
    while v != inicio:
        camino.append(v)
        v = padres[v]
    camino.append(inicio)
    return camino[::-1]



def bfs(grafo, inicio,destino, visitados, orden, padres):#O(V+E)
    padres[inicio] = None
    orden[inicio] = 0
    visitados.add(inicio)
    q = Deque()
    q.append(inicio)
    while q:
        v = q.pop()
        for w in grafo.adyacentes(v):
            orden[w] = orden[v] + 1
            padres[w] = v
            if w == destino:
                return padres
            visitados.add(w)
            q.append(w)

    return padres



def camino_mas_corto(grafo,origen,destino): #O(V+E)
    visitados = set()
    padres = {}
    orden = {}
    bfs(grafo,origen,destino,visitados,orden,padres)
    camino = reconstruir_camino(padres,origen,destino)
    for i in range(len(camino)-1):
        print(camino[i],"-> ",end="")
        
    print(camino[i+1],end="")
    print("")
    print("Costo: ",len(camino))



def caminos_minimos(grafo,origen): #necesita cola
    cola = Deque()
    visitados = set()
    distancia = {}
    distancia[origen] = 0
    visitados.add(origen)
    cola.append(origen)

    while cola:
        v = cola.pop()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1 #+1 o +peso arista
                cola.append(w)
                visitados.add(w)
    return distancia



def diametro(grafo):
    max_min_dist = 0
    for v in grafo:
        distancias = caminos_minimos(grafo,v) # implementar caminos minimos
        for w in distancias:
            if distancias[w] > max_min_dist:
                max_min_dist = distancias[w]
    return max_min_dist



def todos_en_rango(grafo):
    #bfs
    pass
