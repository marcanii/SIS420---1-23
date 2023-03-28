from NodosBI import Nodo
import random
import time
import sys
sys.setrecursionlimit(10**9)

def Generador_hijos(lista):
    m = [[i, i+1] for i in range(len(lista)-1)]
    Lista_hijos = []
    for i in m:
        listaCambiar = lista.copy()
        aux = listaCambiar[i[0]]
        listaCambiar[i[0]] = listaCambiar[i[1]]
        listaCambiar[i[1]] = aux
        Lista_hijos.append(Nodo(listaCambiar))
    return Lista_hijos

def busqueda_BPPR(nodo_actual, solucion, nodos_visitados, nodos_frontera):
    if len(nodos_frontera) == 0:
        return None
    nodo_actual = nodos_frontera.pop()
    nodos_visitados.append(nodo_actual.get_estado())
    if nodo_actual.get_estado() == solucion:
        return nodo_actual
    else:
        # expandir nodos hijos
        estado_nodo = nodo_actual.get_estado()
        hijos = Generador_hijos(estado_nodo)

        nodo_actual.set_hijo(hijos)

        for nodo_hijo in nodo_actual.get_hijo():
            if nodo_hijo.get_estado() not in nodos_visitados and nodo_hijo.get_estado() not in nodos_frontera\
                and heuristica01(nodo_actual, nodo_hijo):
                nodos_frontera.append(nodo_hijo)
                solu = busqueda_BPPR(nodo_hijo, solucion, nodos_visitados, nodos_frontera)

                if solu is not None:
                    return solu

        return None


def heuristica01(padre_node, hijo_node):
    padre_quality = 0
    hijo_quality = 0
    padre_data = padre_node.get_estado()
    hijo_data = hijo_node.get_estado()

    for n in range(1, len(padre_data)):
        if padre_data[n] > padre_data[n - 1]:
            padre_quality = padre_quality + 1
        if hijo_data[n] > hijo_data[n - 1]:
            hijo_quality = hijo_quality + 1

    if hijo_quality >= padre_quality:
        return True
    else:
        return False

def heuristica02(nodo_padre, nodo_hijo):
    solucion = sorted(nodo_padre.get_estado())
    padre = nodo_padre.get_estado()
    hijo = nodo_hijo.get_estado()
    padre_quality = 0
    hijo_quality = 0

    for i in solucion:
        b = solucion.index(i) + 1

        a_padre = padre.index(i) + 1
        c_padre = abs(a_padre - b)

        a_hijo = hijo.index(i) + 1
        c_hijo = abs(a_hijo - b)
        padre_quality += c_padre
        hijo_quality += c_hijo

    if hijo_quality <= padre_quality:
        return True
    else:
        return False

def heuristica03(nodo_padre, nodo_hijo):
    solucion = sorted(nodo_padre.get_estado())
    padre = nodo_padre.get_estado()
    hijo = nodo_hijo.get_estado()
    padre_quality = 0
    hijo_quality = 0

    for i in solucion:
        if padre.index(i) == solucion.index(i):
            padre_quality += 1
        if hijo.index(i) == solucion.index(i):
            hijo_quality += 1

    if hijo_quality >= padre_quality:
        return True
    else:
        return False

if __name__ == "__main__":
    # Heuristica 01
    # 0.00099945068359375 con 6 num
    # 0.0060808658599853516 con 8 num
    # 0.015099763870239258 con 20 num

    # Heuristica 02
    # 0.08305144309997559 con 10 num
    # 0.3032095432281494 con 11 num

    # heuristica 03
    # num
    # num
    estado_inicial = []
    solucion = []
    for i in range(15):
        solucion.append(i+1)
        estado_inicial.insert(0, i+1)

    nodos_visitados = []
    nodos_frontera = []

    print('Estado inicial: ', estado_inicial)
    print('Solucion: ', solucion)

    # generamos el estado inicial ya con valores aleatorios
    #estado_inicial = GenerarEstInicial(solucion)

    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera .append(nodo_inicial)

    inicio_tiempo = time.time()
    # funcion recursiva pero da errores de sobre desbordamiento
    nodo_solucion = busqueda_BPPR(nodo_inicial, solucion, nodos_visitados, nodos_frontera)
    fin_tiempo = time.time()

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    if nodo_actual == None:
        print('No hay solucion...')
    else:
        while nodo_actual.get_padre() is not None:
            resultado.append(nodo_actual.get_estado())
            nodo_actual = nodo_actual.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()
        tiempo_ejecucion = fin_tiempo - inicio_tiempo

        print('\nCamino: ')
        print(resultado)

        print('Tiempo de ejecucion: ',tiempo_ejecucion, 'seg.')
