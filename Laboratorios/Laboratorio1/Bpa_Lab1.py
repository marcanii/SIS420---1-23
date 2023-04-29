import time

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())

def Generador_hijos(lista):
    m = [[i,i+1] for i in range(len(lista)-1)]
    Lista_hijos = []
    for i in m:
        listaCambiar = lista.copy()
        aux = listaCambiar[i[0]]
        listaCambiar[i[0]] = listaCambiar[i[1]]
        listaCambiar[i[1]] = aux
        Lista_hijos.append(Nodo(listaCambiar))
    return Lista_hijos

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            hijos = Generador_hijos(estado_nodo)
            for hijo in hijos:
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            # nodo_actual.set_hijo([hijo_1, hijo_2, hijo_3, hijo_4])
            nodo_actual.set_hijo(hijos)


if __name__ == "__main__":
    estado_inicial = []
    n = int(input('Ingrese el numero de valores de la lista: '))
    print('Ingrese ',n,' valores:')
    for i in range(n):
        x = int(input('Ingrese el valor: '))
        estado_inicial.append(x)

    #print(estado_inicial)
    #estado_inicial = [6,5, 4, 3, 2, 1,0]
    solucion = sorted(estado_inicial)
    #print(solucion)
    inicio_tiempo = time.time()
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    fin_tiempo = time.time()
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(resultado)

    print('\nEl tiempo que tardo en encontrar es: ',tiempo_ejecucion, 'segundos')