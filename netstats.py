"""
https://algoritmos-rw.github.io/algo2/tps/2021_2/tp3/
Wiki ya parseada: https://drive.google.com/file/d/1JOxK7E0bqW3yfuj3niGpPOaWCX7vo_8Q/view
Wiki ya parseada - REDUCIDO: https://drive.google.com/file/d/1b0fZPVE2e1z4TGFL9n4ZiqAnEMAU25rs/view
"""

from grafo import Grafo
import tp3
import sys
import logging

MOSTRAR_MSJ = False
logging.basicConfig(level=logging.WARNING) # Si no querés que aparezcan mensajes de debug cambía "DEBUG" por "WARNING" # https://www.youtube.com/watch?v=-ARI4Cz-awo
if MOSTRAR_MSJ == False:
    logging.basicConfig(level=logging.WARNING)



def ciclo():
    logging.debug(" netstats.py - ciclo()")
    # HECHAS: Camino ★✓, rango ★✓, navegacion ★✓
    # VERIFICAR: lectura ★★✓?, Conectividad ★★✓?
    # EN PROCESO: diametro ★
    list_op = ["camino", "rango", "lectura", "conectados","navegacion"] # Esto va acá? O podría ir como variable global?
    continuar = True # Creo que while True sería mejor
    ingreso_terminal = sys.argv
    cfc_conectividad = {}

    if len(ingreso_terminal) != 2: # Tal vez no funcione si se ingresa comandos por ">" en terminal
        raise IndexError ("Número de variables incorrecto en 'ingreso_terminal'") 
    grafo_netstats = tp3.tsv_to_vert(ingreso_terminal[1])

    while continuar:
        try:
            input_terminal = list(input().split(" "))
        except:
            continuar = False # Creo que while True sería mejor
            logging.debug(" netstats.py - Se llamó Ctrl+D en ciclo(). FIN DE PROGRAMA")
            break # este break cortaría el while True

        if input_terminal[0] == "listar_operaciones":
            #tp3.listar_operaciones(list_op)
            print("navegacion")
            print("camino")
            print("en_rango")
            print("lectura")
            print("conectados")

        elif input_terminal[0] == "camino":
            str_cf = ' '.join(input_terminal[1:])
            param_cam = list(str_cf.split(","))
            if len(param_cam) != 2:
                raise IndexError ("Número de variables incorrecto en 'camino'") 
            tp3.camino_mas_corto(grafo_netstats, param_cam[0], param_cam[1])

        elif input_terminal[0] == "rango":
            str_pn = ' '.join(input_terminal[1:])
            param_ran = list(str_pn.split(","))
            if len(param_ran) != 2:
                raise IndexError ("Número de variables incorrecto en 'rango'")
            tp3.todos_en_rango(grafo_netstats, param_ran[0], int(param_ran[1]))

        elif input_terminal[0] == "diametro": # -- HACER --
            tp3.diametro(grafo_netstats)

        elif input_terminal[0] == "lectura":
            if len(input_terminal) < 2:
                raise IndexError ("Número de variables incorrecto en 'lectura'") 
            str_lec = ' '.join(input_terminal[1:])
            tp3.lectura(grafo_netstats, str_lec)

        elif input_terminal[0] == "navegacion":
            str_n = ' '.join(input_terminal[1:])
            param_nav = list(str_n.split(","))
            if len(param_nav) != 1:
                raise IndexError ("Número de variables incorrecto en 'navegacion'") 
            tp3.navegacion(grafo_netstats, param_nav[0])

        elif input_terminal[0] == "conectados":
            str_c = ' '.join(input_terminal[1:])
            param_con = list(str_c.split(","))
            if len(param_con) != 1:
                raise IndexError ("Número de variables incorrecto en 'conectados'") 
            tp3.conectividad(grafo_netstats, param_con[0], cfc_conectividad)


        elif input_terminal[0] == "clustering":
            #de aca hay que conseguir solo la primera palabra, y que todo el resto sea otra
            if len(input_terminal) > 1:
                tp3.clustering(grafo_netstats,input_terminal[1])
            else:
                tp3.clustering(grafo_netstats,None)

        else:
            print("El comando ingresado no existe. Inténtelo de nuevo")


ciclo()
