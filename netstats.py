#!/usr/bin/python3

from grafo import Grafo
import tp3
import sys
import logging

if tp3.MOSTRAR_MSJ == False:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=logging.DEBUG) 



def ciclo():
    logging.debug(" netstats.py - ciclo()") 
    list_op = ["camino", "rango", "navegacion", "clustering", "lectura"] 
    continuar = True 
    ingreso_terminal = sys.argv

    grafo_netstats = tp3.tsv_to_vert(ingreso_terminal[1])

    while continuar:
        try:
            input_terminal = list(input().split(" "))
        except:
            continuar = False
            logging.debug(" netstats.py - Se llamó Ctrl+D en ciclo(). FIN DE PROGRAMA")
            break 

        if input_terminal[0] == "listar_operaciones":
            tp3.listar_operaciones(list_op)

        elif input_terminal[0] == "camino":
            par = tp3.lista_to_param(input_terminal)
            tp3.camino_mas_corto(grafo_netstats, par[0], par[1])

        elif input_terminal[0] == "rango":
            par = tp3.lista_to_param(input_terminal)
            tp3.todos_en_rango(grafo_netstats, par[0], int(par[1]))

        elif input_terminal[0] == "lectura":
            str_lec = ' '.join(input_terminal[1:])
            tp3.lectura(grafo_netstats, str_lec)

        elif input_terminal[0] == "navegacion":
            par = tp3.lista_to_param(input_terminal)
            tp3.navegacion(grafo_netstats, par[0])

        elif input_terminal[0] == "clustering":
            str_clu = ' '.join(input_terminal[1:])
            if len(input_terminal) > 1:
                tp3.clustering(grafo_netstats,str_clu)
            else:
                tp3.clustering(grafo_netstats,None)
                
        else:
            print("El comando ingresado no existe. Inténtelo de nuevo")


ciclo()
