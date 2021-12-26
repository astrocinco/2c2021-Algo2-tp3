
import heapq
import csv
import logging
from os import POSIX_FADV_RANDOM, times_result
from typing import Deque
from grafo import Grafo
from pilacola import Pila, Cola
from collections import deque

MOSTRAR_MSJ = True
if MOSTRAR_MSJ == False:
    logging.basicConfig(level=logging.WARNING)
else:
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
                if elem == "":
                    continue
                grafo.agregar_vertice(elem)
                if elem != linea[0]:
                    grafo.agregar_arista(linea[0], elem)
    logging.debug(" tp3.py - FIN tsv_to_vert()")
    return grafo 


#---------------------------------------------------------------
def rearmar_camino(padres, destino):
    logging.debug(" tp3.py - rearmar_camino()")
    p = Pila()
    actual = destino
    while actual != None:
        p.apilar(actual)
        actual = padres[actual]

    largo_p = 0
    e = p.desapilar()
    print(e, end="")
    while not p.esta_vacia():
        e = p.desapilar()
        largo_p += 1
        print(" ->", e, end="")
    print("\nCosto:", largo_p)

def bfs_camino(grafo, origen, destino):
    logging.debug(" tp3.py - bfs_camino()")
    q = Cola()
    padres = {origen:None}
    visitados = set()
    visitados.add(origen)
    q.encolar(origen)

    while not q.esta_vacia():
        v = q.desencolar()
        for ady in grafo.adyacentes(v):
            if ady not in visitados:
                visitados.add(ady)
                q.encolar(ady)
                padres[ady] = v
                if ady == destino:
                    return padres
    return None

def camino_mas_corto(grafo, origen, destino):
    logging.debug(" tp3.py - camino_mas_corto()")
    padres = bfs_camino(grafo, origen, destino)
    if padres == None:
        print("No se encontro recorrido")
        return
    rearmar_camino(padres, destino)



#---------------------------------------------------------------diametro: no anda



#---------------------------------------------------------------todos en rango: LISTO

def bfs_tuneado(grafo, inicio, visitados, orden, n, res):
    orden[inicio] = 0
    visitados.add(inicio)
    q = Cola()
    q.encolar(inicio)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = orden[v] + 1
                if orden[w] > n: return
                if orden[w] == n:
                    res.append(w)
                visitados.add(w)
                q.encolar(w)
    return

def todos_en_rango(grafo,pagina,rango):#O(V+E)
    visitados = set()
    orden = {}
    resultado = []
    bfs_tuneado(grafo,pagina,visitados,orden,rango,resultado)
    print(len(resultado))
    

#---------------------------------------------------------------lectura 2 am: anda mal

def lectura(grafo, paginas_str):
    if type(paginas_str) == str:
        paginas = list(paginas_str.split(","))
        for pag in paginas:
            logging.debug(f" tp3.py - lectura() - {pag} pertenece? {grafo.pertenece(pag)}")
    else: 
        paginas = paginas_str
    orden = []

    #if len(paginas) < 2:
    #    raise IndexError ("Numero de variables incorrecto en 'lectura'") 

    for i in range(len(paginas)-1):
        if grafo.estan_unidos(paginas[i+1],paginas[i]):
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
    if len(orden) > MAX_LEN_NAVEGACION:
        return True 
    orden.append(actual)
    adyacentes = grafo.adyacentes(actual)
    if len(adyacentes) > 0:
        _navegacion(grafo,adyacentes[0],orden)
    return True



def navegacion(grafo,origen):
    if origen not in grafo.obtener_vertices():
        return
    logging.debug(" tp3.py - navegacion()")
    navegados = []
    _navegacion(grafo,origen,navegados)

    for i in range(len(navegados)-1):
        print(navegados[i],"-> ",end="")
    print(navegados[len(navegados)-1])

    return

#--------------------------------------------------------------conectividad: EN PROCESO
def imprimir_lista(s):
    pass


def vert_to_obj(grafo, padres, solu, obj):
    logging.debug(" tp3.py - vert_to_obj()")
    for elem in solu:
        actual = elem
        while actual != None:
            print(actual, end=" -> ")
            actual = padres[actual]
        #print("NUEVO ELEM")


def bfs_con(grafo, pagina, padres, sin_hijos):
    padres[pagina] = None
    logging.debug(" tp3.py - bfs_con()")
    q = Cola()
    q.encolar(pagina)
    visitados = set()
    visitados.add(pagina)
    soluciones = set()

    while not q.esta_vacia():
        v = q.desencolar()
        for ady in grafo.adyacentes(v):
            if ady not in visitados:
                q.encolar(ady)
                visitados.add(ady)
                padres[ady] = v
                if grafo.estan_unidos(ady, pagina):
                    soluciones.add(ady)

    largo = len(visitados)
    print(f"len(visitados): {largo}")
    return soluciones
                


def conectividad(grafo, pagina, padres, sin_hijos):
    logging.debug(" tp3.py - conectividad()")
    solu = bfs_con(grafo, pagina, padres, sin_hijos)
    lista_sol = vert_to_obj(grafo, padres, solu, pagina)
    imprimir_lista(solu)

#---------------------------------------------------------------comunidades: EN PROCESO

"""Por cada vértice, en el orden determinado en el punto anterior, definir: Label[Vi]=max_freq(Label[Vj],...,Label[Vk])
Donde Vj,...,VkVj,...,Vk son los vértices que tienen como adyacentes a Vi (ya que las Labels se están propagando). Para el caso de un grafo no dirigido, son los mismos adyacentes a Vi, pero en caso de un grafo dirigido se debe tener en cuenta las aristas de entrada. Se tiene en cuenta la última actualización realizada, inclusive si ya fueron procesados en esta iteración (actualización asincrónica). max_freq
max_freq es una función que devuelve la Label que aparece más frecuentemente entre todos los adyacentes a Vi. En caso de empate, es igual cuál de los máximos devolver."""

def max_freq(adyacentes,label):
    contador = {}
    for i in adyacentes:
        contador[i] = label[i]




def comunidades(grafo,pagina):
    vertices = grafo.obtener_vertices()
    label = {}
    orden = []
    for i in range(len(vertices)):
        label[vertices[i]] = i
        orden.append(vertices[i])


    for i in orden:
        adyacentes = grafo.adyacentes(i)
        label[i] = max_freq(adyacentes,orden)
    return


#---------------------------------------------------------------clustering: LISTO


def _clustering(grafo,vertice):
    adyacentes = grafo.adyacentes(vertice)
    if len(adyacentes) < 2:
        return 0
    grado_salida = len(adyacentes)
    c = 0.0
    for i in adyacentes:
        for v in adyacentes:
            if grafo.estan_unidos(i,v):  
                c += 1

    resultado = c/(grado_salida*(grado_salida-1))
    return resultado


def clustering(grafo,vertice = None):
    if vertice:
        resultado = _clustering(grafo,vertice)
        print(round(resultado,3))
        return
    else:
        c_general = 0.0
        vertices = grafo.obtener_vertices()
        for v in vertices:
            valor_v =_clustering(grafo,v)
            c_general += valor_v

        c_general = c_general/len(vertices)
        print(round(c_general,3))
        return

#---------------------------------------------------------------ciclo de n articulos: EN PROCESO

"""
# Copia ej coloreo
def valido(grafo, vertice, coloreados):
    for ady in grafo.adyacentes(vertice):
        if ady in coloreados and coloreados[ady] == coloreados[vertice]: 
            # Mira los ady del vertice buscando que dos adyacentes tengan el mismo color
            return False
    return True

def _colorear(grafo, coloreados, n, vertices, ind):
    if len(coloreados) == len(grafo.obtener_vertices()):
        # Todos los vertices han sido coloreados
        return True

    nuevo_vertice = vertices[ind]
    for i in range(n): # Probando cada color posible
        coloreados[nuevo_vertice] = i # Asignando color a vertice en cuestion
        if not valido(grafo, nuevo_vertice, coloreados):
            del coloreados[nuevo_vertice]
            continue
        if _colorear(grafo, coloreados, n, vertices, ind + 1):
            return True
        del coloreados[nuevo_vertice]

    return False

def colorear(grafo, n):
    coloreados = {}
    vertices = grafo.obtener_vertices() # Lista de todos los vertices del grafo
    # n -> numero que representa la cantidad de colores posibles
    return _colorear(grafo, coloreados, n, vertices, 0)

def no_adyacentes(grafo, n):
    return colorear(grafo, n)
"""
def imprimir_ciclo(ciclo, objetivo):
    print(objetivo, end="")
    for key in ciclo:
        print(" ->", key, end="")
    print("")
    

def valido(grafo, objetivo, actual, n, iteracion, dead_end, padre):
    if actual in dead_end:
        logging.debug(f" tp3.py - valido() {actual} es DEAD END")
        return False

    if iteracion == n:
        if actual == objetivo:
            return True
        return False

    todos_dead_end = True
    for ady in grafo.adyacentes(actual):
        if ady == padre:
            continue
        if ady not in dead_end:
            todos_dead_end = False
            break
    if todos_dead_end == True:
        dead_end.add(actual)
        logging.debug(f" tp3.py - valido() {actual} ahora es DEAD END")

    if iteracion < n:
        return True

    return False

def _ciclo(grafo, ciclo, n, objetivo, actual, lista, iter, dead_end):
    logging.debug(f" tp3.py - _ciclo() {actual}")
    if len(ciclo) == n: 
        for key in ciclo:
            pass
        if key != objetivo:
            return False
        return True

    for ady in grafo.adyacentes(actual):
        ciclo[ady] = actual
        if not valido(grafo,objetivo, ady, n, iter, dead_end, actual):
            ciclo.pop(ady, None)
            continue
        if _ciclo(grafo, ciclo, n, objetivo, ady, lista, iter+1, dead_end):
            return True
        ciclo.pop(ady, None)

    return False

def ciclo(grafo, pagina, n):
    logging.debug(" tp3.py - ciclo()")
    ciclo = {}
    dead_end = set()
    _ciclo(grafo, ciclo, n, pagina, pagina, grafo.obtener_vertices(), 0, dead_end)
    if ciclo != {}:
        imprimir_ciclo(ciclo, pagina)
    else: 
        print("No se encontro recorrido")