from grafo import *
import heapq

def dijkstra(grafo,vertices,padres, origen,destino):
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



def camino_mas_corto(grafo,origen,destino):
    padres = []
    dist = 0
    dijkstra(grafo,grafo.obtener_vertices(),padres,origen,destino)
    #todavia no anda

'''
    vertices = grafo.obtener_vertices()
    visitados = set()
'''



