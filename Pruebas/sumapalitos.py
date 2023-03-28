
from busquedas02 import ProblemaBusqueda, aestrella

from timeit import default_timer

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


# 8. Resolver el problema de palitos de fosforo que permita:
INICIAL = """
        _     _ 
|_| _   _| = |_|
  |    |_     _|
"""

# |_ lo tomaremos como suma
OBJETIVO = """
 _      _     _ 
  | |_  _| = |_|
  |    |_     _|
"""

inicio = default_timer()

#Cambiar el string a una lista de caracteres en forma de matriz
INICIAL = [list(x) for x in INICIAL.split("\n") if x]
OBJETIVO = [list(x) for x in OBJETIVO.split("\n") if x]

#print(INICIAL)
#print(OBJETIVO)


posiciones_objetivo = {}
filas_objetivo = OBJETIVO
for i in ' ,_, , , , , , ,_, , , , , ,_, , , ,|, ,|,_, , ,_,|, ,=, ,|,_,|, , ,|, , , , ,|,_, , , , , ,_,|':
    posiciones_objetivo[i] = find_location(filas_objetivo, i)
print(posiciones_objetivo)

class JuegoPalitos(ProblemaBusqueda):

    def acciones(self, estado):

        filas = string_to_list(estado)
        fila, columna = find_location(filas, '_' or '|')

        acciones = []
        if fila > 0:
            acciones.append(filas[fila - 1][columna])
        if fila < 2:
            acciones.append(filas[fila + 1][columna])
        if columna > 0:
            acciones.append(filas[fila][columna - 1])
        if columna < 15:
            acciones.append(filas[fila][columna + 1])

        return acciones

    def resultado(self, estado, accion):
        filas = string_to_list(estado)
        fila, columna = find_location(filas, '_' or '|')
        fila_n, columna_n = find_location(filas, accion)

        filas[fila][columna], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila][columna]

        return list_to_string(filas)

    def es_objetivo(self, estado):
        # True si un estado es el estado_objetivo
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        # costo de ejecutar una accion
        return 1

    def heuristica(self, estado):
        # Aprox de la distancia de un esatdo a otro
        # distancia manhattan: define la distancia entre dos estados con la suma de las diferencias absolutas

        filas = string_to_list(estado)
        distancia = 0
        for i in ' ,_, , , , , , ,_, , , , , ,_, , , ,|, ,|,_, , ,_,|, ,=, ,|,_,|, , ,|, , , , ,|,_, , , , , ,_,|':
            fila_n, columna_n = find_location(filas, i)
            fila_n_objetivo, col_n_meta = posiciones_objetivo[i]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_meta)

        return distancia


resultado = aestrella(JuegoPalitos(INICIAL))

for accion, estado in resultado.camino():
    print(accion)
    print(estado)
fin = default_timer()
print((fin - inicio) / 60, ' Minutos')



