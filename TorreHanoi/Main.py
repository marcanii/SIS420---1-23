from Problema import *
from Nodo import *
import time

def busqueda_AEstrella(problema, estado_inicial, estado_objetivo):
    frontera = []
    nodos_visitados = set()

    nodo_inicio = NodoBusqueda(estado=problema.estado_inicial, problema=problema)
    frontera.append(nodo_inicio)
    while frontera:
        nodo_actual = frontera.pop()

        if problema.es_objetivo(nodo_actual.estado):
            return nodo_actual

        nodos_expandidos = nodo_actual.expandir()
        nodos_visitados.add(nodo_actual.estado)

        for n in nodos_expandidos:
            otros_nodos = [x for x in frontera if x.estado == n.estado]
            if n.estado not in nodos_visitados and len(otros_nodos) == 0:
                frontera.append(n)
            elif len(otros_nodos) > 0 and n.costo < otros_nodos[0].costo:
                frontera.remove(otros_nodos[0])
                frontera.append(n)
    return None

if __name__ == "__main__":
    estado_inicial = '''
    1-0-0
    2-0-0
    3-0-0
    4-0-0
    5-0-0
    6-0-0
    7-0-0
    8-0-0
    9-0-0'''
    estado_objetivo = '''
    0-0-1
    0-0-2
    0-0-3
    0-0-4
    0-0-5
    0-0-6
    0-0-7
    0-0-8
    0-0-9'''
    print("Estado Inicial")
    print(estado_inicial)
    estado_inicial = estado_inicial[1:].replace(" ", "")
    estado_objetivo = estado_objetivo[1:].replace(" ", "")
    inicio_tiempo = time.time()
    problema = HanoiProblem(estado_inicial, estado_objetivo)
    resultado = busqueda_AEstrella(problema, estado_inicial, estado_objetivo)
    fin_tiempo = time.time()
    # Mostrando pasos a seguir para llegar a la solucion
    print("----------------------------------------")
    for accion, estado in resultado.camino():
        try:
            print('Mover:', accion[4], ' de ', accion[2:4], ' -> ', accion[0:2])
        except:
            print('Inicio')
        print(estado)
        print('-------------')
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print('Tiempo de ejecucion: ', tiempo_ejecucion, 'seg.')

    # probando repositorio laptop
    # probando repo desde compu pc