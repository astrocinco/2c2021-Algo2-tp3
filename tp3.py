from typing import Deque
from grafo import Grafo
import heapq
import csv
from collections import deque
import logging

logging.basicConfig(level=logging.WARNING) # Si no querés que aparezcan mensajes de debug cambía "DEBUG" por "WARNING"





class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        self.tope = _Nodo(dato, self.tope)

    def desapilar(self):
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None



class Cola:
    '''Representa a una cola, con operaciones de encolar y 
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None







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



def bfs(grafo, inicio,destino, visitados, orden, padres,n,dist_n):#O(V+E) # Aux: camino_mas_corto, todos_en_rango
    logging.debug(" tp3.py - bfs()")
    padres[inicio] = None
    orden[inicio] = 0
    visitados.add(inicio)
    q = Deque()
    q.append(inicio)
    while q:
        v = q.pop()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = orden[v] + 1
                if orden[w] == n:
                    dist_n.append(w)
                logging.debug(f" tp3.py - bfs() - {w} orden {orden[w]}")
                padres[w] = v
                if w == destino:
                    return padres
                visitados.add(w)
                q.append(w)

    logging.debug(" tp3.py - FIN bfs()")

#---------------------------------------------------------------camino mas corto: anda mal

def camino_mas_corto(grafo,origen,destino): #O(V+E)
    logging.debug(" tp3.py - camino_mas_corto()")
    if not grafo.pertenece(origen) or not grafo.pertenece(destino): 
        logging.debug(" tp3.py - camino_mas_corto() - ORIGEN O DESTINO NO PERTENECEN AL GRAFO")
        return
    visitados = set()
    padres = {}
    orden = {}
    bfs(grafo,origen,destino,visitados,orden,padres,0,[])
    camino = reconstruir_camino(padres,origen,destino)
    for i in range(len(camino)-1):
        print(camino[i],"-> ",end="")
        
    print(camino[len(camino) -1])
    print("Costo: ",len(camino))

#---------------------------------------------------------------diametro: NO ANDA

def caminos_minimos(grafo,origen,actual): 
    cola = Cola()
    distancia = {}
    distancia[origen] = 0
    visitados = set()
    visitados.add(origen)
    cola.encolar(origen)
    camino = []
    camino.append(origen)
    while cola:
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancia[w] = distancia[v] + 1 
                #+1 o +peso_arista

                camino.append(w)
                cola.encolar(w)
                visitados.add(w)
    return camino

#---------------------------------------------------------------diametro: no anda

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




#---------------------------------------------------------------todos en rango: no anda

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
    

#---------------------------------------------------------------lectura 2 am: LISTO

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

    return True

#--------------------------------------------------------------conectividad: EN PROCESO

def conectividad(grafo, pagina):
    pass



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


#---------------------------------------------------------------coef por clustering: hay algo mal, da numeros muy altos, pero en general creo que funciona

#notas finales: clustering sin indicacin particular anda bien. en los particulares no da bien




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
        print("{:.3}".format(resultado))
        return
    else:
        c_general = 0.0
        vertices = grafo.obtener_vertices()
        for v in vertices:
            print(v)
            valor_v =_clustering(grafo,v)
            c_general += valor_v

        c_general = c_general/len(vertices)
        print("{:.3}".format(c_general))
        return










