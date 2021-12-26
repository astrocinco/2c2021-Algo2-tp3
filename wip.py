#---------------------------------------------------------------ciclo de n articulos: EN PROCESO

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