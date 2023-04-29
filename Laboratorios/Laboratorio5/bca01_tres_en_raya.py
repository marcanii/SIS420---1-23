from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe, using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMANO = -1
COMPUTADOR = +1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def evaluate(estado):
    """
    Función de evaluación del estado de finalización del juego.
     : parametro: estado, estado actual del tablero
     : devuelve: +1 si COMPUTADOR gana; -1 si el HUMANO gana; 0 en caso de empate
    """
    if wins(estado, COMPUTADOR):
        score = +1
    elif wins(estado, HUMANO):
        score = -1
    else:
        score = 0

    return score

def wins(estado, player):
    """
    Esta funcion verifica si un jugador especifico gana. Posibilidades:
    * Tres filas    [X X X] or [O O O]
    * Tres columnas    [X X X] or [O O O]
    * Dos diagonales [X X X] or [O O O]
    :parametro estado, el estado del tablero actual
    :parametro player: un HUMANOo o un COMPUTADORutador
    :devuelve: True si un jugador gana
    """
    win_state = [
        [estado[0][0], estado[0][1], estado[0][2]],
        [estado[1][0], estado[1][1], estado[1][2]],
        [estado[2][0], estado[2][1], estado[2][2]],
        [estado[0][0], estado[1][0], estado[2][0]],
        [estado[0][1], estado[1][1], estado[2][1]],
        [estado[0][2], estado[1][2], estado[2][2]],
        [estado[0][0], estado[1][1], estado[2][2]],
        [estado[2][0], estado[1][1], estado[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(estado):
    """
    Esa funcion verifica si el HUMANO o el COMPUTADOR gana
    :parametro estado, estado del tablero actual
    :devuelve: True si el HUMANO o el COMPUTADOR gana
    """
    return wins(estado, HUMANO) or wins(estado, COMPUTADOR)


def empty_cells(estado):
    """
    Cada celda vacía se agregará a la lista de celdas
    :parametro estado, estado de tablero actual
    :devuelve, una lista de las celdas vacias
    """
    cells = []

    for x, fila in enumerate(estado):
        for y, cell in enumerate(fila):
            if cell == 0:
                cells.append([x, y])
    return cells

def valid_move(x, y):
    """
    Un movimiento es válido si la celda elegida está vacía
    :parametro x, coordenada X
    :parametro y, coordenada Y
    :devuelve: True si la posicion del tablero[x][y] esta vacia
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def set_move(x, y, player):
    """
    Establece un movimiento en el tablero, si las coordenadas son validas
    :parametro x, coordenada X
    :parametro y, coordenada Y
    :parametro player, jugador actual
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(estado, depth, player):
    """
    Funcion IA que elige la mejor movida
    AI function that choice the best move
    :parametro estado, estado actual en el tablero
    :param depth, indice del nodo en el arbol (0 <= depth < 9), pero nunca nueve.
    :param player, un HUMANO o un COMPUTADOR
    :devuelve, una lista con [la mejor fila, la mejor columna, el mejor score]
    """
    if player == COMPUTADOR:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(estado):
        score = evaluate(estado)
        return [-1, -1, score]

    for cell in empty_cells(estado):
        x, y = cell[0], cell[1]
        estado[x][y] = player
        score = minimax(estado, depth - 1, -player)
        estado[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTADOR:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(estado, c_choice, h_choice):
    """
    Print the board on console
    :param estado: current estado of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for fila in estado:
        for cell in fila:
            symbol = chars[cell]
            print(f'| {symbol} |', end = '')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    Esta funcion llama a la funcion minimax si la profundidad es < 9,
    caso contrario esta elige una coordenada aleatoria.
    :param c_choice: COMPUTADOR elije X o O
    :param h_choice: HUMANO elije X o O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Juega COMPUTADOR [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMPUTADOR)
        x, y = move[0], move[1]

    set_move(x, y, COMPUTADOR)
    time.sleep(1)

def HUMANO_turn(c_choice, h_choice):
    """
    El HUMANO juega eligiendo una movida valida.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'turno HUMANO [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use los numeros (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMANO)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if HUMANO is the first

    # HUMANO chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting COMPUTADORuter's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # HUMANO may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        HUMANO_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMANO):
        clean()
        print(f'HUMANO turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMPUTADOR):
        clean()
        print(f'COMPUTADORuter turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('EMPATES!')

    exit()


if __name__ == '__main__':
    main()


'''
win_state = [
        [estado[0][0], estado[0][1], estado[0][2], estado[0][3]], # primera fila 1 opcion
        [estado[0][1], estado[0][2], estado[0][3], estado[0][4]], # primera fila 2 opcion
        [estado[0][2], estado[0][3], estado[0][4], estado[0][5]], # primera fila 3 opcion
        [estado[1][0], estado[1][1], estado[1][2], estado[1][3]], # segunda fila 1 opcion
        [estado[1][1], estado[1][2], estado[1][3], estado[1][4]], # segunda fila 2 opcion
        [estado[1][2], estado[1][3], estado[1][4], estado[1][5]], # segunda fila 3 opcion
        [estado[2][0], estado[2][1], estado[2][2], estado[2][3]], # tercera fila 1 opcion
        [estado[2][1], estado[2][2], estado[2][3], estado[2][4]], # tercera fila 2 opcion
        [estado[2][2], estado[2][3], estado[2][4], estado[2][5]], # tercera fila 3 opcion
        [estado[3][0], estado[3][1], estado[3][2], estado[3][3]], # cuarta fila 1 opcion
        [estado[3][1], estado[3][2], estado[3][3], estado[3][4]], # cuarta fila 2 opcion
        [estado[3][2], estado[3][3], estado[3][4], estado[3][5]], # cuarta fila 3 opcion
        [estado[4][0], estado[4][1], estado[4][2], estado[4][3]], # quinta fila 1 opcion
        [estado[4][1], estado[4][2], estado[4][3], estado[4][4]], # quinta fila 2 opcion
        [estado[4][2], estado[4][3], estado[4][4], estado[4][5]], # quinta fila 3 opcion
        [estado[5][0], estado[5][1], estado[5][2], estado[5][3]], # sexta fila 1 opcion
        [estado[5][1], estado[5][2], estado[5][3], estado[5][4]],  # sexta fila 2 opcion
        [estado[5][2], estado[5][3], estado[5][4], estado[5][5]],  # sexta fila 3 opcion

        [estado[0][0], estado[1][0], estado[2][0], estado[3][0]], # primera columna 1 opcion
        [estado[1][0], estado[2][0], estado[3][0], estado[4][0]], # primera columna 2 opcion
        [estado[2][0], estado[3][0], estado[4][0], estado[5][0]], # primera columna 3 opcion
        [estado[0][1], estado[1][1], estado[2][1], estado[3][1]], # segunda columna 1 opcion
        [estado[1][1], estado[2][1], estado[3][1], estado[4][1]], # segunda columna 2 opcion
        [estado[2][1], estado[3][1], estado[4][1], estado[5][1]], # segunda columna 3 opcion
        [estado[0][2], estado[1][2], estado[2][2], estado[3][2]], # tercera columna 1 opcion
        [estado[1][2], estado[2][2], estado[3][2], estado[4][2]], # tercera columna 2 opcion
        [estado[2][2], estado[3][2], estado[4][2], estado[5][2]], # tercera columna 3 opcion
        [estado[0][3], estado[1][3], estado[2][3], estado[3][3]], # cuarta columna 1 opcion
        [estado[1][3], estado[2][3], estado[3][3], estado[4][3]], # cuarta columna 2 opcion
        [estado[2][3], estado[3][3], estado[4][3], estado[5][3]], # cuarta columna 3 opcion
        [estado[0][4], estado[1][4], estado[2][4], estado[3][4]], # quinta columna 1 opcion
        [estado[1][4], estado[2][4], estado[3][4], estado[4][4]], # quinta columna 2 opcion
        [estado[2][4], estado[3][4], estado[4][4], estado[5][4]], # quinta columna 3 opcion
        [estado[0][5], estado[1][5], estado[2][5], estado[3][5]], # sexta columna 1 opcion
        [estado[1][5], estado[2][5], estado[3][5], estado[4][5]], # sexta columna 1 opcion
        [estado[2][5], estado[3][5], estado[4][5], estado[5][5]], # sexta columna 1 opcion

        [estado[2][0], estado[3][1], estado[4][2], estado[5][3]], # diagonal \ 1 opcion
        [estado[1][0], estado[2][1], estado[3][2], estado[4][3]], # diagonal \ 2 opcion
        [estado[2][1], estado[3][2], estado[4][3], estado[5][4]], # diagonal \ 3 opcion
        [estado[0][0], estado[1][1], estado[2][2], estado[3][3]], # diagonal \ 4 opcion
        [estado[1][1], estado[2][2], estado[3][3], estado[4][4]], # diagonal \ 5 opcion
        [estado[2][2], estado[3][3], estado[4][4], estado[5][5]], # diagonal \ 6 opcion
        [estado[0][1], estado[1][2], estado[2][3], estado[3][4]], # diagonal \ 7 opcion
        [estado[1][2], estado[2][3], estado[3][4], estado[4][5]], # diagonal \ 8 opcion
        [estado[0][2], estado[1][3], estado[2][4], estado[3][5]], # diagonal \ 9 opcion

        [estado[3][0], estado[2][1], estado[1][2], estado[0][3]], # diagonal / 1 opcion
        [estado[4][0], estado[3][1], estado[2][2], estado[1][3]], # diagonal / 2 opcion
        [estado[3][1], estado[2][2], estado[1][3], estado[0][4]], # diagonal / 3 opcion
        [estado[5][0], estado[4][1], estado[3][2], estado[2][3]], # diagonal / 4 opcion
        [estado[4][1], estado[3][2], estado[2][3], estado[1][4]], # diagonal / 5 opcion
        [estado[3][2], estado[2][3], estado[1][4], estado[0][5]], # diagonal / 6 opcion
        [estado[5][1], estado[4][2], estado[3][3], estado[2][4]], # diagonal / 7 opcion
        [estado[4][2], estado[3][3], estado[2][4], estado[1][5]], # diagonal / 8 opcion
        [estado[5][2], estado[4][3], estado[3][4], estado[2][5]]  # diagonal / 9 opcion
    ]

'''