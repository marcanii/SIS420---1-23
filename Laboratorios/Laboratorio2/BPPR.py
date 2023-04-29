import time
import random

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

def GenerarEstInicial(sol):
    lista = []
    while len(lista) != len(sol):
        a = random.randint(0,9)
        if a in sol and a not in lista:
            cant_num_rep = sol.count(a)
            for i in range(cant_num_rep):
                lista.append(a)
    return lista

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

def busqueda_BPPR_solucion(nodo_actual, solucion, nodos_visitados):
    nodos_visitados.append(nodo_actual.get_estado())
    if nodo_actual.get_estado() == solucion:
        return nodo_actual
    else:
        # expandir nodos hijos
        estado_nodo = nodo_actual.get_estado()
        hijos = Generador_hijos(estado_nodo)
        nodo_actual.set_hijo(hijos)

        for hijo_node in nodo_actual.get_hijo():
            if not hijo_node.get_estado() in nodos_visitados:
                solu = busqueda_BPPR_solucion(hijo_node, solucion, nodos_visitados)
                if solu is not None:
                    return solu
        return None

if __name__ == "__main__":
    n = int(input("Ingrese numero de elementos en la lista: "))
    size = input("Ingrese la contraseña: ")
    estado_inicial = []
    solucion = []
    nodos_visitados = []

    for i in size:
        estado_inicial.append(0)
        solucion.append(int(i))

    print('Estado inicial: ', estado_inicial)
    print('Solucion: ', solucion)

    # generamos el estado inicial ya con valores aleatorios
    estado_inicial = GenerarEstInicial(solucion)

    nodo_inicial = Nodo(estado_inicial)

    inicio_tiempo = time.time()
    nodo_solucion = busqueda_BPPR_solucion(nodo_inicial, solucion, nodos_visitados)
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

    print('\nCamino: ')
    print(resultado)

    print('Tiempo de ejecucion: ',tiempo_ejecucion, 'seg.')
