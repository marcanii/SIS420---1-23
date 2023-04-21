import random

def mostrar_tablero(tablero):
    print("+-+-+-+")
    for fila in tablero:
        print("|".join(fila))
        print("+-+-+-+")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Verificar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def turno_jugador(tablero, jugador):
    print("Turno del jugador", jugador)
    fila = int(input("Ingrese la fila donde desea colocar su marca (0-2): "))
    col = int(input("Ingrese la columna donde desea colocar su marca (0-2): "))
    if tablero[fila][col] != " ":
        print("Esa casilla ya está ocupada. Intente de nuevo.")
        turno_jugador(tablero, jugador)
    else:
        tablero[fila][col] = jugador

def turno_computadora(tablero, jugador):
    print("Turno de la computadora")
    # Estrategia básica: elegir la primera casilla vacía que encuentre
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == " ":
                tablero[fila][col] = jugador
                return

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    random.shuffle(jugadores)
    print("Comienza el juego. Jugador", jugadores[0], "va primero.")
    mostrar_tablero(tablero)
    while True:
        for jugador in jugadores:
            if all(tablero[fila][col] != " " for fila in range(3) for col in range(3)):
                print("¡Empate!")
                return
            if jugador == "X":
                turno_jugador(tablero, jugador)
            else:
                turno_computadora(tablero, jugador)
            mostrar_tablero(tablero)
            if verificar_ganador(tablero, jugador):
                print("¡Jugador", jugador, "ha ganado!")
                return


if __name__ == '__main__':
    jugar()
