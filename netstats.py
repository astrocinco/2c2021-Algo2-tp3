# https://algoritmos-rw.github.io/algo2/tps/2021_2/tp3/
# Wiki ya parseada: https://drive.google.com/file/d/1JOxK7E0bqW3yfuj3niGpPOaWCX7vo_8Q/view
# Wiki ya parseada - REDUCIDO: https://drive.google.com/file/d/1b0fZPVE2e1z4TGFL9n4ZiqAnEMAU25rs/view

from grafo import Grafo
import tp3
import sys
import logging
logging.basicConfig(level=logging.DEBUG) # Si no querés que aparezcan mensajes de debug cambía "DEBUG" por "WARNING" # https://www.youtube.com/watch?v=-ARI4Cz-awo

INPUT_ERROR_NO_EXISTE_COMANDO = "El comando ingresado no existe. Inténtelo de nuevo"



def ciclo():
    logging.debug(" netstats.py - ciclo()")
    list_op = ["camino","rango" ,"diametro","lectura"] # Esto va acá? O podría ir como variable global?
    continuar = True # Creo que while True sería mejor
    ingreso_terminal = sys.argv
    if len(ingreso_terminal) != 2:
        raise IndexError ("Número de variables incorrecto en 'ingreso_terminal'") 
    grafo_netstats = tp3.tsv_to_vert(ingreso_terminal[1])
    if grafo_netstats == None: 
        raise Exception # En caso de fallar la lectura del archivo. -- HACER --

    while continuar:
        try:
            input_terminal = list(input().split(" "))
        except:
            continuar = False # Creo que while True sería mejor
            logging.debug(" netstats.py - Se llamó Ctrl+D en ciclo(). FIN DE PROGRAMA")
            break # este break cortaría el while True

        if input_terminal == "listar_operaciones":
            tp3.listar_operaciones(list_op)

        elif input_terminal[0] == "camino":
            if len(input_terminal) != 2:
                raise IndexError ("Número de variables incorrecto en 'camino'") 
            parametros = list(input_terminal[1].split(","))
            if len(parametros) != 2:
                raise IndexError ("Número de variables incorrecto en 'camino'") 
            tp3.camino_mas_corto(grafo_netstats, parametros[0], parametros[1])

        elif input_terminal[0] == "rango":
            tp3.todos_en_rango(grafo_netstats)

        elif input_terminal[0] == "diametro":
            tp3.diametro(grafo_netstats)

        else:
            print(INPUT_ERROR_NO_EXISTE_COMANDO)


ciclo()
