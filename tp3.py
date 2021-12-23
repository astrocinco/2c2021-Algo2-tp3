from typing import Deque
from grafo import Grafo
import heapq
import csv
from collections import deque
import logging
logging.basicConfig(level=logging.DEBUG) # Si no querés que aparezcan mensajes de debug cambía "DEBUG" por "WARNING"

MAX_LEN_NAVEGACION = 20

def listar_operaciones(list_op):
     for func in list_op:
         print(func) 



def tsv_to_vert(nombre_tsv, grafo = Grafo()):
    logging.debug(" tp3.py - tsv_to_vert()")
    with open(nombre_tsv) as archivo:
        cont = csv.reader(archivo, delimiter="\t") # Revisar carg mem, revisar ""
        for linea in cont:
            for elem in linea:
                grafo.agregar_vertice(elem)
                if elem != linea[0]:
                    grafo.agregar_arista(linea[0], elem)
    logging.debug(" tp3.py - FIN tsv_to_vert()")
    return grafo 


#---------------------------------------------------------------camino mas corto: LISTO

def reconstruir_camino(padres, inicio, fin): # Aux: camino_mas_corto
    logging.debug(" tp3.py - reconstruir_camino()")
    v = fin
    camino = []
    while v != inicio:
        camino.append(v)
        v = padres[v]
    camino.append(inicio)
    return camino[::-1]



def bfs(grafo, inicio,destino, visitados, orden, padres):#O(V+E) # Aux: camino_mas_corto, todos_en_rango
    logging.debug(" tp3.py - bfs()")
    padres[inicio] = None
    orden[inicio] = 0
    visitados.add(inicio)
    q = Deque()
    q.append(inicio)
    while q:
        v = q.pop()
        for w in grafo.adyacentes(v):
            if w in visitados:
                continue
            orden[w] = orden[v] + 1
            logging.debug(f" tp3.py - bfs() - {w} orden {orden[w]}")
            padres[w] = v
            if w == destino:
                return padres
            visitados.add(w)
            q.append(w)

    logging.debug(" tp3.py - FIN bfs()")



def camino_mas_corto(grafo,origen,destino): #O(V+E)
    logging.debug(" tp3.py - camino_mas_corto()")
    if not grafo.pertenece(origen) or not grafo.pertenece(destino): 
        logging.debug(" tp3.py - camino_mas_corto() - ORIGEN O DESTINO NO PERTENECEN AL GRAFO")
        return
    visitados = set()
    padres = {}
    orden = {}
    bfs(grafo,origen,destino,visitados,orden,padres)
    camino = reconstruir_camino(padres,origen,destino)
    for i in range(len(camino)-1):
        print(camino[i],"-> ",end="")
        
    print(camino[len(camino) -1])
    print("Costo: ",len(camino))

#---------------------------------------------------------------diametro: NO ANDA

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

#---------------------------------------------------------------todos en rango: LISTO

def todos_en_rango(grafo,pagina,rango):#O(V+E + V) = O(V+E)
    visitados = set()
    puestos = {}
    orden = {}
    bfs(grafo,pagina,None,visitados,orden,puestos)#O(v+e)

    cantidad = 0
    for i in orden: #O(v)
        logging.debug(f" tp3.py - todos_en_rango() - {i}")
        if orden[i] == rango:
            cantidad+=1
    print(cantidad)
    return cantidad

#---------------------------------------------------------------lectura 2 am: LISTO

def lectura(grafo, paginas_str):
    if type(paginas_str) == str:
        paginas = list(paginas_str.split(","))
        for pag in paginas:
            logging.debug(f" tp3.py - lectura() - {pag} pertenece? {grafo.pertenece(pag)}")
    else: 
        paginas = paginas_str
    orden = []

    if len(paginas) < 2:
        raise IndexError ("Numero de variables incorrecto en 'lectura'") 

    for i in range(len(paginas)-1):
        if grafo.estan_unidos(paginas[i],paginas[i+1]):
            orden.append(paginas[i])
            if i == (len(paginas)-2):
                orden.append(paginas[len(paginas)-1])
        else:
            print("No existe forma de leer las paginas en orden")
            return False
    
    for i in range(len(orden)-1):
        print(orden[len(orden)-i-1],end=", ")
    print(orden[0])
    return True

#---------------------------------------------------------------navegacion por primer link: LISTA

def _navegacion(grafo,actual,orden):
    logging.debug(" tp3.py - _navegacion()")
    if len(orden) >= MAX_LEN_NAVEGACION + 1: # No estoy seguro si está bien dejarlo como constante global. Tal vez mejor como constante adentro de _navegacion?
        return True #true o solo return?? # Mucho no importa, no hacemos nada con lo que retorne. Si pones true debería haber un false en algún lado
    orden.append(actual)
    adyacentes = grafo.adyacentes(actual)
    if len(adyacentes) > 0:
        _navegacion(grafo,adyacentes[0],orden)
    return True



def navegacion(grafo,origen):
    logging.debug(" tp3.py - navegacion()")
    navegados = []
    _navegacion(grafo,origen,navegados)

    for i in range(len(navegados)-1):
        print(navegados[i],"-> ",end="")
    print(navegados[len(navegados)-1])

    return True



#---------------------------------------------------------------comunidades: EN PROCESO

"""Por cada vértice, en el orden determinado en el punto anterior, definir: Label[Vi]=max_freq(Label[Vj],...,Label[Vk])
Donde Vj,...,VkVj,...,Vk son los vértices que tienen como adyacentes a Vi (ya que las Labels se están propagando). Para el caso de un grafo no dirigido, son los mismos adyacentes a Vi, pero en caso de un grafo dirigido se debe tener en cuenta las aristas de entrada. Se tiene en cuenta la última actualización realizada, inclusive si ya fueron procesados en esta iteración (actualización asincrónica). max_freq
max_freq es una función que devuelve la Label que aparece más frecuentemente entre todos los adyacentes a Vi. En caso de empate, es igual cuál de los máximos devolver."""

def max_freq(adyacentes):
    pass


def comunidades(grafo,pagina):
    vertices = grafo.obtener_vertices()
    label = {}
    orden = []
    for i in range(len(vertices)):
        label[vertices[i]] = i
        orden.append(vertices[i])


    for i in orden:
        adyacentes = grafo.adyacentes(i)
        label[i] = max_freq(adyacentes)


    
    
    
    return