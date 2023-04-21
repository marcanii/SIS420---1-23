import math
from busquedas02 import ProblemaBusqueda, aestrella

MAPA = """
##############################
#E        #              #   #
#  ###    ########       #   #
#  #     A #             #   #
#     ##     ####   ######   #
#   C      ####     #        #
#            #  #   #   #### #
#     ######    #   #   #    #
#  B     ###    #            #
##############################
"""
MAPA = [list(x) for x in MAPA.split("\n") if x]
COSTOS = {
    "arriba": 1.0,
    "abajo": 1.0,
    "izquierda": 1.0,
    "derecha": 1.0,
}
class JuegoLaberinto(ProblemaBusqueda):
    def __init__(self, tablero):
        self.tablero = tablero
        self.estado_objetivo1 = (0, 0)
        self.estado_objetivo2 = (0, 0)
        self.estado_objetivo3 = (0, 0)
        for y in range(len(self.tablero)):
            for x in range(len(self.tablero[y])):
                if self.tablero[y][x].lower() == "e":
                    self.estado_inicial = (x, y)
                elif self.tablero[y][x].lower() == "a":
                    self.estado_objetivo1 = (x, y)
                elif self.tablero[y][x].lower() == "b":
                    self.estado_objetivo2 = (x, y)
                elif self.tablero[y][x].lower() == "c":
                    self.estado_objetivo3 = (x, y)

        super(JuegoLaberinto, self).__init__(estado_inicial=self.estado_inicial)
    def acciones(self, estado):
        acciones = []
        for accion in list(COSTOS.keys()):
            nuevox, nuevoy = self.resultado(estado, accion)
            if self.tablero[nuevoy][nuevox] != "#":
                acciones.append(accion)
        return acciones

    def resultado(self, estado, accion):
        x, y = estado

        if accion.count("arriba"):
            y -= 1
        if accion.count("abajo"):
            y += 1
        if accion.count("izquierda"):
            x -= 1
        if accion.count("derecha"):
            x += 1

        estado_nuevo = (x, y)
        return estado_nuevo

    def es_objetivo(self, estado):
        return estado == self.estado_objetivo1 or estado == self.estado_objetivo2 or estado == self.estado_objetivo3

    def costo(self, estado, accion, estado2):
        return COSTOS[accion]

    # def heuristica(self, estado):
    #     x, y = estado
    #     gx, gy = self.estado_objetivo1
    #     return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


def main():
    caracter = '';
    problema = JuegoLaberinto(MAPA)
    resultado = aestrella(problema, busqueda_en_grafo=True)
    camino = [x[1] for x in resultado.camino()]
    for y in range(len(MAPA)):
        for x in range(len(MAPA[y])):
            if (x, y) == problema.estado_inicial:
                print("E", end='')
            elif (x, y) == problema.estado_objetivo1:
                print("A", end='')
                caracter = 'A';
            elif (x, y) == problema.estado_objetivo2:
                print("B", end='')
                caracter = 'B';
            elif (x, y) == problema.estado_objetivo3:
                print("C", end='')
                caracter = 'C';
            elif (x, y) in camino:
                print("*", end='')
            else:
                print(MAPA[y][x], end='')
        print()

    print('El camino mas corto es hacia el punto: ',caracter)
    print('Con una distancia de ', len(camino)-1, 'puntos')

if __name__ == "__main__":
    main()

