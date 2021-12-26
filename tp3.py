
import csv
import logging
from grafo import Grafo
from pilacola import Pila, Cola

# MNJS DEBUGGING

MOSTRAR_MSJ = False
if MOSTRAR_MSJ == False:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=logging.DEBUG)

# FUNCIONES AUXILIARES

def lista_to_param(lista):
    str = ' '.join(lista[1:])
    return list(str.split(","))



def listar_operaciones(list_op):
     for func in list_op:
         print(func) 



def tsv_to_vert(nombre_tsv, grafo = Grafo()):
    logging.debug(" tp3.py - tsv_to_vert()")
    with open(nombre_tsv) as archivo:
        cont = csv.reader(archivo, delimiter="\t") 
        for linea in cont:
            for elem in linea:
                if elem == "":
                    continue
                grafo.agregar_vertice(elem)
                if elem != linea[0]:
                    grafo.agregar_arista(linea[0], elem)
    logging.debug(" tp3.py - FIN tsv_to_vert()")
    return grafo 

# CAMINO

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
        return False
    rearmar_camino(padres, destino)
    return True

# RANGO

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



def todos_en_rango(grafo,pagina,rango):
    visitados = set()
    orden = {}
    resultado = []
    bfs_tuneado(grafo,pagina,visitados,orden,rango,resultado)
    print(len(resultado))
    
# LECTURA

def imprimir_lectura(res_lec):
    if res_lec == None or len(res_lec) == 0:
        print("No existe forma de leer las paginas en orden")
        return
    for i in range(len(res_lec) -1, 0, -1):
        print(res_lec[i], end=", ")
    print(res_lec[0])



def grados_entrada(grafo, lista):
    g_ent = {}
    for v in lista: 
        g_ent[v] = 0
    for v in lista:
        for ady in grafo.adyacentes(v):
            if ady in lista:
                g_ent[ady] += 1
    return g_ent



def topologico_grados(grafo, lista):
    g_ent = grados_entrada(grafo, lista)
    q = Cola()
    entra = False

    for v in g_ent.keys():
        if g_ent[v] == 0:
            q.encolar(v)
            entra = True

    resultado = []
    if entra == False:
        return None

    while not q.esta_vacia():
        v = q.desencolar()
        resultado.append(v)
        for ady in grafo.adyacentes(v):
            if ady not in lista:
                continue
            g_ent[ady] -= 1
            if g_ent[ady] == 0:
                q.encolar(ady)
    if len(resultado) != len(lista):
        return None
    return resultado



def lectura(grafo, paginas_str):
    if type(paginas_str) == str:
        paginas = list(paginas_str.split(","))
        for pag in paginas:
            logging.debug(f" tp3.py - lectura() - {pag} pertenece? {grafo.pertenece(pag)}")

    res = topologico_grados(grafo, paginas)
    imprimir_lectura(res)

# NAVEGACION

def _navegacion(grafo,actual,orden):
    max_len_nav = 20
    logging.debug(" tp3.py - _navegacion()")
    if len(orden) > max_len_nav:
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

# CLUSTERING

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
