#!/usr/bin/python3

from grafo import Grafo
import tp3
import sys
import logging

if tp3.MOSTRAR_MSJ == False:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=logging.DEBUG) # Si no querés que aparezcan mensajes de debug cambía "DEBUG" por "WARNING" # https://www.youtube.com/watch?v=-ARI4Cz-awo



def ciclo():
    logging.debug(" netstats.py - ciclo()")
    # BIEN: rango ★✓, navegacion ★✓, clustering ★★✓
    # HECHAS MAL: Camino ★, lectura ★★, diametro ★
    # FALTAN: Conectividad ★★, Comunidades ★★, Pagerank ★★★, Ciclo ★★★ 
    list_op = ["rango", "navegacion", "clustering", "diametro"] # Esto va acá? O podría ir como variable global?
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
            tp3.listar_operaciones(list_op)

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
            tp3.diametro_rpl(grafo_netstats)

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
            str_clu = ' '.join(input_terminal[1:])

            if len(input_terminal) > 1:
                tp3.clustering(grafo_netstats,str_clu)
            else:
                tp3.clustering(grafo_netstats,None)

        else:
            print("El comando ingresado no existe. Inténtelo de nuevo")


ciclo()
