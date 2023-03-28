import heapq
import time
import random


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    return [row.strip().split('-') for row in string_.split('\n')]

def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       Devuelve una tupla: fila, columna'''
       
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


class ColaPrioridadLimitada(object):
    def __init__(self, limite=None, *args):
        self.limite = limite
        self.queue = list()

    def __getitem__(self, val):
        return self.queue[val]

    def __len__(self):
        return len(self.queue)

    def append(self, x):
        heapq.heappush(self.queue, x)
        if self.limite and len(self.queue) > self.limite:
            self.queue.remove(heapq.nlargest(1, self.queue)[0])

    def pop(self):
        return heapq.heappop(self.queue)

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def clear(self):
        for x in self:
            self.queue.remove(x)

    def remove(self, x):
        self.queue.remove(x)

    def sorted(self):
        return heapq.nsmallest(len(self.queue), self.queue)


class EigthPuzzleProblem(object):
  def __init__(self, estado_inicial, estado_objetivo):
    self.estado_inicial = estado_inicial
    self.estado_objetivo = estado_objetivo

  def acciones(self, estado):
    '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
    filas = string_to_list(estado)
    fila_e, columna_e = find_location(filas, 'e')

    acciones = []
    if fila_e > 0:
        acciones.append(filas[fila_e - 1][columna_e])
    if fila_e < 2:
        acciones.append(filas[fila_e + 1][columna_e])
    if columna_e > 0:
        acciones.append(filas[fila_e][columna_e - 1])
    if columna_e < 2:
        acciones.append(filas[fila_e][columna_e + 1])

    return acciones

  def resultado(self, estado, accion):
    '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
    '''
    filas = string_to_list(estado)
    fila_e, columna_e = find_location(filas, 'e')
    fila_n, columna_n = find_location(filas, accion)

    filas[fila_e][columna_e], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_e][columna_e]

    return list_to_string(filas)

  def es_objetivo(self, estado):
    '''Devuelve True si un estado es el estado_objetivo.'''
    return estado == self.estado_objetivo

  def costo(self, estado1, accion, estado2):
    '''Devuelve el costo de ejecutar una accion.
    '''
    return 1

  def heuristica(self, estado):
    '''Devuelve una estimacion de la distancia
    de un estado a otro, utilizando la distancia manhattan.

    '''
    filas = string_to_list(estado)

    distancia = 0

    for numero in '12345678e':
      fila_n, columna_n = find_location(filas, numero)
      fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

      distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)

    return distancia

  def estado_representacion(self, estado):
    """
    Devuelve un string de representacion de un estado.
    Por defecto devuelve str(estado).
    """
    return str(estado)


class NodoBusqueda(object):
    '''Nodo para el proceso de busqueda.'''

    def __init__(self, estado, padre=None, accion=None, costo=0, problema=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo
        self.problema = problema or padre.problema
        self.profundidad = profundidad

    def expandir(self, busqueda_local=False):
        '''Crear sucesores.'''
        nodos_nuevos = []
        for accion in self.problema.acciones(self.estado):
            estado_nuevo = self.problema.resultado(self.estado, accion)
            costo = self.problema.costo(self.estado, accion, estado_nuevo)
            fabrica_nodos = self.__class__
            nodos_nuevos.append(fabrica_nodos(estado=estado_nuevo,
                                         padre=None if busqueda_local else self,
                                         problema=self.problema,
                                         accion=accion,
                                         costo=self.costo + costo,
                                         profundidad=self.profundidad + 1))
        return nodos_nuevos

    def camino(self):
        '''Camino (lista de nodos y acciones) desde el nodo raiz al nodo actual.'''
        nodo = self
        camino = []
        while nodo:
            camino.append((nodo.accion, nodo.estado))
            nodo = nodo.padre
        return list(reversed(camino))

    def __eq__(self, otro):
        return isinstance(otro, NodoBusqueda) and self.estado == otro.estado

    def estado_representacion(self):
        return self.problema.estado_representacion(self.estado)

    def accion_representacion(self):
        return self.problema.accion_representacion(self.accion)

    def __repr__(self):
        return 'Node <%s>' % self.estado_representacion().replace('\n', ' ')

    def __hash__(self):
        return hash((
            self.estado,
            self.padre,
            self.accion,
            self.costo,
            self.profundidad,
        ))



class NodoBusquedaHeuristicaOrdenado(NodoBusqueda):
    def __init__(self, *args, **kwargs):
        super(NodoBusquedaHeuristicaOrdenado, self).__init__(*args, **kwargs)
        self.heuristica = self.problema.heuristica(self.estado)

    def __lt__(self, otro):
        return self.heuristica < otro.heuristica

class NodoBusquedaEstrellaOrdenado(NodoBusquedaHeuristicaOrdenado):
    def __lt__(self, otro):
        return self.heuristica + self.costo < otro.heuristica + otro.costo



def busqueda_AEstrella(problema): 
  limite_profundidad = None
  busqueda_en_grafo = False
  reemplazar_grafo_cuando_mejor = True
  frontera = ColaPrioridadLimitada()
  nodos_visitados = set()

  nodo_inicio = NodoBusquedaEstrellaOrdenado(estado=problema.estado_inicial, problema=problema)
  frontera.append(nodo_inicio)
  while frontera:
    nodo_actual = frontera.pop()
    # print("###"*20)
    # print(nodo_actual.estado)
    # print(problema.estado_objetivo)

    if problema.es_objetivo(nodo_actual.estado):
      return nodo_actual
    
    nodos_visitados.add(nodo_actual.estado)

    if limite_profundidad is None or nodo_actual.profundidad < limite_profundidad:
      nodos_expandidos = nodo_actual.expandir()

      for n in nodos_expandidos:
        if busqueda_en_grafo:
          otros_nodos = [x for x in frontera if x.estado == n.estado]
          assert len(otros_nodos) in (0, 1)
          if n.estado not in nodos_visitados and len(otros_nodos) == 0:
            frontera.append(n)
          elif reemplazar_grafo_cuando_mejor and len(otros_nodos) > 0 and n < otros_nodos[0]:
            frontera.remove(otros_nodos[0])
            frontera.append(n)
        else:
          frontera.append(n)


if __name__ == "__main__":
  estado_inicial = '''e-1-3
                      4-2-5
                      8-7-6'''
  estado_objetivo = '''1-2-3
                       4-5-6
                       7-8-e'''
  
  posiciones_objetivo = {}
  filas_objetivo = string_to_list(estado_objetivo)
  # print(string_to_list(estado_objetivo))
  for numero in '12345678e':
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)

  # print(posiciones_objetivo)
  problema = EigthPuzzleProblem(estado_inicial, estado_objetivo)
  resultado = busqueda_AEstrella(problema)

  for accion, estado in resultado.camino():
    print('Move numero', accion)
    print(estado)