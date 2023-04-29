

class NodoBusqueda():
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
        nodo_actual = self
        camino = []
        while nodo_actual:
            camino.append((nodo_actual.accion, nodo_actual.estado))
            nodo_actual = nodo_actual.padre
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


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


class PalitosFosoro():
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = list_to_string(string_to_list(estado_inicial))
        self.estado_objetivo = list_to_string(string_to_list(estado_objetivo))

    def acciones(self, estado):
        '''Devuelve una lista de todos los posibles movimientos'''
        filas = string_to_list(estado)
        # Extrae todos las posiciones que se encuentran ocupadas
        u = {}
        for it, f in enumerate(filas):
            for j, a in enumerate(f):
                if a == '\\':
                    u[(it, j)] = '\\'
                elif a == '/':
                    u[(it, j)] = '/'

        # filtra las elementos que deben ser movidas
        ubicaciones = {i: j for i, j in u.items() if (i[0] != 1 and i[0] != 2) or (i[1] != 1 and i[1] != 2)}
        # A partir de las ubicaciones de los elementos que pueden ser movidos
        # se extrae los posibles movimientos de cada elemento
        acciones = []
        for u, s in ubicaciones.items():
            # Fila
            if u[0] == 0:
                if s == '\\':
                    o1 = [3, 2]
                    o2 = [2, 3]
                else:
                    o1 = [3, 1]
                    o2 = [2, 0]
            elif u[0] == 3:
                if s == '\\':
                    o1 = [0, 1]
                    o2 = [1, 0]
                else:
                    o1 = [0, 2]
                    o2 = [1, 3]
            # Columna
            if u[1] == 0:
                if s == '\\':
                    o1 = [2, 3]
                    o2 = [3, 2]
                else:
                    o1 = [1, 3]
                    o2 = [0, 2]
            elif u[1] == 3:
                if s == '\\':
                    o1 = [1, 0]
                    o2 = [0, 1]
                else:
                    o1 = [2, 0]
                    o2 = [3, 1]

            if tuple(o1) not in list(ubicaciones.keys()):
                acciones.append(o1 + list(u) + [s])

            if tuple(o2) not in list(ubicaciones.keys()):
                acciones.append(o2 + list(u) + [s])

        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        posicion = accion[0:2]
        movimiento = accion[2:4]
        filas[movimiento[0]][movimiento[1]] = '0'
        filas[posicion[0]][posicion[1]] = accion[4]
        return list_to_string(filas)


    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == self.estado_objetivo


    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion.
        '''
        return 1

def busqueda(problema, nodo_actual, visitados):
    visitados.append(nodo_actual.estado)
    #Verifica si se encontro el objetico
    if problema.es_objetivo(nodo_actual.estado):
        return nodo_actual
    #Expanden el nodo actual
    nodos_expandidos = nodo_actual.expandir()
    for nodo_hijo in nodos_expandidos:
        if not nodo_hijo.estado in visitados:
            # Llamada Recursiva
            Solution = busqueda(problema, nodo_hijo, visitados)
            if Solution is not None:
                return Solution
    return None

if __name__ == "__main__":
    estado_inicial = '''0-0-0-0
0-/-\\-0
/-\\-/-\\
0-/-\\-0'''
    estado_objetivo = '''0-\\-0-0
\\-/-\\-0
/-\\-/-0
0-/-0-0'''

    visitados = []
    problema = PalitosFosoro(estado_inicial, estado_objetivo)
    nodo_inicial = NodoBusqueda(estado=problema.estado_inicial, problema=problema)
    resultado = busqueda(problema, nodo_inicial, visitados)
    # Mostrando el camino a la solucion
    for accion, estado in resultado.camino():
        try:
            print('Mueve:', accion[4], ' de ', accion[2:4], ' a ', accion[0:2])
        except:
            print('Inicio')
        print(estado)
        print('-------------')