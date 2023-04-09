import math
import random

def create_board():
    """
    Esta función crea un tablero de juego vacío para el 6 en raya.
    """
    board = [['-' for x in range(6)] for y in range(6)]
    return board

def print_board(board):
    """
    Esta función imprime el tablero de juego en la consola.
    """
    for row in board:
        print(' '.join(row))
    print()

def evaluate(board):
    """
    Evalúa el tablero para determinar la puntuación.
    Devuelve +infinito si la computadora gana, -infinito si el jugador humano gana,
    y la diferencia de fichas si no hay ganador.
    """
    winner = get_winner(board)
    if winner == 'X':
        return float('inf')
    elif winner == 'O':
        return float('-inf')
    else:
        score = 0
        # Comprobar filas
        for row in board:
            for i in range(len(row)-5):
                window = row[i:i+6]
                score += evaluate_window(window)
        # Comprobar columnas
        for j in range(len(board[0])):
            for i in range(len(board)-5):
                window = [board[i+k][j] for k in range(6)]
                score += evaluate_window(window)
        # Comprobar diagonales ascendentes
        for i in range(len(board)-5):
            for j in range(len(board[0])-5):
                window = [board[i+k][j+k] for k in range(6)]
                score += evaluate_window(window)
        # Comprobar diagonales descendentes
        for i in range(5, len(board)):
            for j in range(len(board[0])-5):
                window = [board[i-k][j+k] for k in range(6)]
                score += evaluate_window(window)
        return score

def evaluate_window(window):
    """
    Evalúa una ventana de 6 fichas.
    Devuelve 100 si la computadora tiene 5 fichas en la ventana,
    10 si la computadora tiene 4 fichas y una casilla vacía en la ventana,
    1 si la computadora tiene 3 fichas y dos casillas vacías en la ventana,
    -10 si el jugador humano tiene 4 fichas y una casilla vacía en la ventana,
    -1 si el jugador humano tiene 3 fichas y dos casillas vacías en la ventana,
    y 0 en cualquier otro caso.
    """
    if window.count('X') == 5:
        return 100
    elif window.count('X') == 4 and window.count(None) == 1:
        return 10
    elif window.count('X') == 3 and window.count(None) == 2:
        return 1
    elif window.count('O') == 4 and window.count(None) == 1:
        return -10
    elif window.count('O') == 3 and window.count(None) == 2:
        return -1
    else:
        return 0


def is_game_over(board):
    """
    Esta función comprueba si el juego ha terminado.
    """
    for row in board:
        if '-' in row:
            return False
    return True

def get_valid_moves(board):
    """
    Esta función devuelve una lista de movimientos válidos que se pueden hacer en el tablero.
    """
    valid_moves = []
    for i in range(6):
        for j in range(6):
            if board[i][j] == '-':
                valid_moves.append((i, j))
    return valid_moves

def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Esta función
    implementa el algoritmo Minimax con la poda alfa-beta para seleccionar el mejor movimiento.
    """
    # Comprobar si el juego ha terminado o si se ha alcanzado la profundidad máxima
    if is_game_over(board) or depth == 0:
        return evaluate(board)

    # Obtener los movimientos válidos para el jugador actual
    valid_moves = get_valid_moves(board)

    # Si el jugador actual es el jugador que maximiza, buscar el movimiento que maximiza la puntuación
    if maximizing_player:
        max_score = -math.inf
        for move in valid_moves:
            # Hacer el movimiento en el tablero
            board[move[0]][move[1]] = 'X'
            # Llamar a la función minimax para el jugador contrario con la profundidad reducida
            score = minimax(board, depth-1, alpha, beta, False)
            # Deshacer el movimiento en el tablero
            board[move[0]][move[1]] = '-'
            # Actualizar la puntuación máxima y la poda alfa
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    # Si el jugador actual es el jugador que minimiza, buscar el movimiento que minimiza la puntuación
    else:
        min_score = math.inf
        for move in valid_moves:
            # Hacer el movimiento en el tablero
            board[move[0]][move[1]] = 'O'
            # Llamar a la función minimax para el jugador contrario con la profundidad reducida
            score = minimax(board, depth-1, alpha, beta, True)
            # Deshacer el movimiento en el tablero
            board[move[0]][move[1]] = '-'
            # Actualizar la puntuación mínima y la poda beta
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

def get_best_move(board, depth):
    """
    Esta función devuelve el mejor movimiento que se puede hacer en el tablero utilizando el algoritmo Minimax con la poda alfa-beta.
    """
    best_move = None
    max_score = -math.inf
    for move in get_valid_moves(board):
        # Hacer el movimiento en el tablero
        board[move[0]][move[1]] = 'X'
        # Llamar a la función minimax para el jugador contrario con la profundidad reducida
        score = minimax(board, depth-1, -math.inf, math.inf, False)
        # Deshacer el movimiento en el tablero
        board[move[0]][move[1]] = '-'
        # Actualizar el mejor movimiento y la puntuación máxima
        if score > max_score:
            best_move = move
            max_score = score

    return best_move
def get_winner(board):
    """
    Determina si hay un ganador en el juego 6 en raya.
    Devuelve 'O' si gana el jugador humano, 'X' si gana la computadora,
    y None si no hay ganador todavía.
    """
    # Comprobar filas
    for row in board:
        for i in range(len(row)-5):
            if row[i:i+6] == ['O', 'O', 'O', 'O', 'O', 'O']:
                return 'O'
            elif row[i:i+6] == ['X', 'X', 'X', 'X', 'X', 'X']:
                return 'X'
    # Comprobar columnas
    for j in range(len(board[0])):
        for i in range(len(board)-5):
            if [board[i+k][j] for k in range(6)] == ['O', 'O', 'O', 'O', 'O', 'O']:
                return 'O'
            elif [board[i+k][j] for k in range(6)] == ['X', 'X', 'X', 'X', 'X', 'X']:
                return 'X'
    # Comprobar diagonales ascendentes
    for i in range(len(board)-5):
        for j in range(len(board[0])-5):
            if [board[i+k][j+k] for k in range(6)] == ['O', 'O', 'O', 'O', 'O', 'O']:
                return 'O'
            elif [board[i+k][j+k] for k in range(6)] == ['X', 'X', 'X', 'X', 'X', 'X']:
                return 'X'
    # Comprobar diagonales descendentes
    for i in range(5, len(board)):
        for j in range(len(board[0])-5):
            if [board[i-k][j+k] for k in range(6)] == ['O', 'O', 'O', 'O', 'O', 'O']:
                return 'O'
            elif [board[i-k][j+k] for k in range(6)] == ['X', 'X', 'X', 'X', 'X', 'X']:
                return 'X'
    return None

def play():
    """
    Esta función maneja el flujo del juego.
    """
    board = create_board()
    print_board(board)
    while not is_game_over(board):
        # Turno del jugador
        row = int(input("Introduce el número de fila (1-6): ")) - 1
        col = int(input("Introduce el número de columna (1-6): ")) - 1
        if board[row][col] == '-':
            board[row][col] = 'O'
        else:
            print("Esa casilla ya está ocupada. Introduce otra posición.")
            continue
        print_board(board)
        if is_game_over(board):
            break
        # Turno de la computadora
        print("Turno de la computadora...")
        depth = 4
        move = get_best_move(board, depth)
        board[move[0]][move[1]] = 'X'
        print(f"La computadora ha hecho el movimiento {move[0] + 1},{move[1] + 1}")
        print_board(board)
    winner = get_winner(board)
    if winner == 'O':
        print("¡Felicidades! Has ganado el juego.")
    elif winner == 'X':
        print("La computadora ha ganado el juego.")
    else:
        print("El juego ha terminado en empate.")


if __name__ == '__main__':
    play()