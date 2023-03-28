import matplotlib.pyplot as plt
import numpy as np

class Casilla:
    def __init__(self, x, y, EsMuro):
        self.x = x
        self.y = y
        self.EsMuro = EsMuro
        self.Entrada = ''
        self.Up = False
        self.Right = False
        self.Down = False
        self.Left = False

class Laberinto:
    def __init__(self, StLab):
        self.Tablero = []
        self.Inicio = [None, None]
        self.Final = [None, None]
        self.Camino = []
        for x in range(len(StLab)):
            Fila = []
            for y in range(len(StLab[x])):
                Fila.append(Casilla(x, y, StLab[x][y] == '*'))
                if StLab[x][y] == 'I':
                    self.Inicio = [x,y]
                elif StLab[x][y] == 'F':
                    self.Final = [x,y]
            self.Tablero.append(Fila)
        self.Camino.append(self.Tablero[self.Inicio[0]][self.Inicio[1]])

    def Avanzar(self):
        C = self.Camino[-1]
        if not C.Up and C.Entrada != 'Up':
            Cs = self.Tablero[C.x-1][C.y]
            if not Cs.EsMuro:
                C.Up = True
                Cs.Entrada = 'Down'
                self.Camino.append(Cs)
                return
        if not C.Right and C.Entrada != 'Right':
            Cs = self.Tablero[C.x][C.y+1]
            if not Cs.EsMuro:
                C.Right = True
                Cs.Entrada = 'Left'
                self.Camino.append(Cs)
                return
        if not C.Down and C.Entrada != 'Down':
            Cs = self.Tablero[C.x+1][C.y]
            if not Cs.EsMuro:
                C.Down = True
                Cs.Entrada = 'Up'
                self.Camino.append(Cs)
                return
        if not C.Left and C.Entrada != 'Left':
            Cs = self.Tablero[C.x][C.y-1]
            if not Cs.EsMuro:
                C.Left = True
                Cs.Entrada = 'Right'
                self.Camino.append(Cs)
                return
        self.Camino.pop()

    def Finalizado(self):
        if len(self.Camino) == 0: return True
        C = self.Camino[-1]
        return C.x == self.Final[0] and C.y == self.Final[1]

    def Pintar(self):
        for x in range(len(self.Tablero)):
            for y in range(len(self.Tablero[x])):
                if self.Tablero[x][y].EsMuro:
                    plt.plot([y],[len(self.Tablero) - x - 1], linestyle='None', marker='.', markersize=8, color='black')
        plt.plot([self.Inicio[1]], [len(self.Tablero) - self.Inicio[0] - 1], linestyle='None', marker='.', markersize=14, color='blue')
        plt.plot([self.Final[1]], [len(self.Tablero) - self.Final[0] - 1], linestyle='None', marker='.', markersize=14, color='green')
        for c in self.Camino:
            plt.plot(c.y, [len(self.Tablero) - c.x -1], linestyle='None', marker='.', markersize=8, color='red')

# la matriz
maze = [
        "************************************",
        "*I                       ***********",
        "*** ****** *************************",
        "*** ****** *************************",
        "*** ****** *********       *********",
        "*** ****** ********* ***** *********",
        "*** ****** ********* ***** *********",
        "*** ****** ********* ***** *********",
        "*** ******           ***** *********",
        "*** ********************** *********",
        "***      ***************** *********",
        "*** ********************** *********",
        "*** ********************** *********",
        "*** ********************** *********",
        "*** ********************** *********",
        "***                        *********",
        "**** *******************************",
        "**** *****                **********",
        "****       **************         F*",
        "************************************",
        ]

PocoAPoco = True

L = Laberinto(maze)
if not PocoAPoco:
    while not L.Finalizado():
        L.Avanzar()
else:
    plt.ion()
    L.Pintar()
    plt.draw()
    while not L.Finalizado():
        L.Avanzar()
        plt.clf()
        L.Pintar()
        plt.draw()
        plt.pause(0.01)
    print('Ya está')
    plt.ioff()
L.Pintar()
plt.show()
