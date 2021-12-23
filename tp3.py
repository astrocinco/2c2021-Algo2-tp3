from typing import Deque
from grafo import *
import heapq
import csv
from collections import deque

def listar_operaciones(list_op):
     for func in list_op:
         print(func) # Imprimir así? o con otra cosa como stdout?

def tsv_to_vert(nombre_tsv, grafo = Grafo()):
    with open(nombre_tsv) as archivo:
        cont = csv.reader(archivo, delimiter="\t") # Revisar carg mem, revisar ""
        for linea in cont:
            for elem in linea:
                grafo.agregar_vertice(elem)
                if len(linea) != 1:
                    if elem != linea[0]:
                        grafo.agregar_arista(linea[0], elem)
    return grafo # Retornar None o algo así cuando no se pueda entrar al archivo -- HACER --



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
        
    print(camino[i+1])
    print("Costo: ",len(camino))



def caminos_minimos(grafo,origen,actual): 
    cola = Deque()
    distancia = {}
    distancia[origen] = 0
    visitados = set()
    visitados.add(origen)
    cola.append(origen)
    camino = []
    camino.append(origen)
    while cola:
        v = cola.pop()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1 
                #+1 o +peso_arista

                camino.append(w)
                cola.append(w)
                visitados.add(w)
    return camino

def diametro(grafo):#tiene que dar 1>3>6>7
    max_min_dist = 0

    mas_largo = []
    for v in grafo.obtener_vertices():
        camino = caminos_minimos(grafo, v,v)
        print(camino)
        if len(camino) > max_min_dist:
            max_min_dist = len(camino)
            mas_largo = camino

    #asi no anda, tendre que hacer dfs y verificar no tenga mas adyacentes??
    #pienso
    #igual la respuesta esta cerca, este algoritmo recorre todos los vertices


    for i in range(len(mas_largo)-1):
        print(mas_largo[i],"-> ",end="")
    print(mas_largo[i+1])
    print("Costo: ",len(mas_largo))
    return



def todos_en_rango(grafo,pagina,rango):#O(V+E + V) = O(V+E)
    visitados = set()
    puestos = {}
    orden = {}
    bfs(grafo,pagina,None,visitados,orden,puestos)#O(v+e)

    cantidad = 0
    for i in orden: #O(v)
        if orden[i] == rango:
            cantidad+=1
    return cantidad
    















def lectura(grafo, paginas):
    orden = []
    for i in range(len(paginas)-1):
        if grafo.estan_unidos(paginas[i],paginas[i+1]):
            orden.append(paginas[i])
            if i == (len(paginas)-2):
                orden.append(paginas[len(paginas)-1])
        else:
            print("No existe forma de leer las paginas en orden")
    
    for i in range(len(orden)-1):
        print(orden[len(orden)-i-1],end=", ")
    print(orden[0])
    
    return






















