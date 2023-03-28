import time
import random

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = []
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
        if (hijo is not None):
            self.hijo.append(hijo)
            if self.hijo is not None:
                for h in self.hijo:
                    h.padre = self

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


def busqueda_BPPR(nodo_inicial, solucion, visitado):
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        for i in range(0, len(solucion) - 1):
            indice = i

            hijo_datos = nodo_inicial.get_estado().copy()
            temp = hijo_datos[indice]
            hijo_datos[indice] = hijo_datos[indice + 1]
            hijo_datos[indice + 1] = temp
            hijo = Nodo(hijo_datos)
            nodo_inicial.set_hijo(hijo)

        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado)
                if Solution is not None:
                    return Solution
        return None


if __name__ == "__main__":
    n = int(input("Ingrese numero de elementos en la lista: "))
    size = input("Ingrese la contraseña: ")
    solucion = []

    for i in size:
        solucion.append(int(i))

    estado_inicial = [0, 0, 0, 0, 0]
    print("Estado Inicial", estado_inicial)
    print("Solucion", solucion)
    nodo_solucion = None
    visitado = []
    estado_inicial = random.sample(range(0, n), n)
    nodo_inicial = Nodo(estado_inicial)
    inicio = time.time()
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)
    fin = time.time()

    # Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Tiempo de ejecucion: ", fin - inicio)