from NodosBI import NodoBI

def busqueda_heuristica(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        nodo_estado = nodo_inicial.get_estado()
        hijo = [nodo_estado[1], nodo_estado[0], nodo_estado[2], nodo_estado[3]]
        hijo_left = NodoBI(hijo)
        hijo = [nodo_estado[0], nodo_estado[2], nodo_estado[1], nodo_estado[3]]
        hijo_central = NodoBI(hijo)
        hijo = [nodo_estado[0], nodo_estado[1], nodo_estado[3], nodo_estado[2]]
        hijo_right = NodoBI(hijo)
        nodo_inicial.set_hijo([hijo_left, hijo_central, hijo_right])

        for hijo_node in nodo_inicial.get_hijo():
            if not hijo_node.get_estado() in visitados and heuristica(nodo_inicial, hijo_node):
            #if not hijo_node.get_estado() in visitados:
                # Llamada recursiva
                solu = busqueda_heuristica(hijo_node, solucion, visitados)
                if solu is not None:
                    return solu
        return None


def heuristica(padre_node, hijo_node):
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


if __name__ == "__main__":
    # estado_inicial = [1, 2, 3, 4]
    # estado_solucion = [4, 3, 2, 1]

    estado_inicial = [4, 3, 2, 1]
    # estado_inicial  = [4, 3, 2, 1]
    estado_solucion = [1, 2, 3, 4]

    visitados_nodes = []
    nodo_inicial = NodoBI(estado_inicial)
    nodo_solucion = busqueda_heuristica(nodo_inicial, estado_solucion, visitados_nodes)

    print(nodo_solucion)

    resultado = []

    node = nodo_solucion
    while node.get_padre() is not None:
        resultado.append(node.get_estado())
        node = node.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)