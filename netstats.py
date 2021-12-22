# Welcome back, Python
# https://algoritmos-rw.github.io/algo2/tps/2021_2/tp3/
# Wiki ya parseada: https://drive.google.com/file/d/1JOxK7E0bqW3yfuj3niGpPOaWCX7vo_8Q/view
# Wiki ya parseada - REDUCIDO: https://drive.google.com/file/d/1b0fZPVE2e1z4TGFL9n4ZiqAnEMAU25rs/view

from grafo import Grafo
import tp3
import sys

INPUT_ERROR_NO_EXISTE_COMANDO = "El comando ingresado no existe. Inténtelo de nuevo"


"""
def esperar_comando():
    corriendo = True
    comando = input("")
    
    while corriendo:
        if comando == "listar_operaciones":
            print("camino")
            #van a haber mas

        elif comando == "asd":
            return 



def main():
    #validar_parametros()

    grafo = Grafo()

    esperar_comando()
"""



def ciclo():
    list_op = ["camino", "diametro"] # Esto va acá? O podría ir como variable global?
    ingreso_terminal = sys.argv
    if len(ingreso_terminal) != 2:
        raise Exception # Elegir mejor excepción
    grafo_netstats = tp3.tsv_to_vert(ingreso_terminal[1])
    if grafo_netstats == None: 
        raise Exception # En caso de fallar la lectura del archivo. -- HACER --

    tp3.listar_operaciones(list_op)
    while True: # No se si está bueno poner while(True)
        try: 
            input_terminal = list(input().split(" "))
        except EOFError:
            break # Terminar el ciclo cuando el input sea Control+D
        
        if input_terminal[0] == "camino":
            if len(input_terminal) != 2:
                raise Exception # Elegir mejor excepction
            parametros = list(input_terminal[1].split(","))
            if len(parametros) != 2:
                raise Exception
            tp3.camino_mas_corto(grafo_netstats, parametros[0], parametros[1])

        elif input_terminal[0] == "Funcion2":
            tp3.funcion2(grafo_netstats)

        elif input_terminal[0] == "Funcion3":
            tp3.funcion3(grafo_netstats)

        else:
            print(INPUT_ERROR_NO_EXISTE_COMANDO)
        


ciclo()