import numpy as np
import random

# Función para crear el tablero
def create_board():
    return np.zeros((6, 6), dtype=int)

# Función para imprimir el tablero
def print_board(board):
    print(np.flip(board, 0))

# Función para determinar si un movimiento es válido
def is_valid_move(board, col):
    return board[5][col] == 0

# Función para realizar un movimiento
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Función para comprobar si hay cuatro en línea
def get_winner(board):
    # Comprobar filas
    for row in range(6):
        for col in range(3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != 0:
                return board[row][col]

    # Comprobar columnas
    for row in range(3):
        for col in range(6):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != 0:
                return board[row][col]

    # Comprobar diagonales
    for row in range(3):
        for col in range(3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != 0:
                return board[row][col]
    for row in range(3, 6):
        for col in range(3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] != 0:
                return board[row][col]

    # Comprobar si hay empate
    if np.all(board != 0):
        return -1

    return 0

# Función para evaluar el estado actual del tablero
def evaluate(board, piece):
    # Definir las puntuaciones
    global scores
    scores = [0, 1, 10, 100, 1000]

    # Calcular puntuación para filas
    score = 0
    for row in range(6):
        row_array = [int(i) for i in list(board[row,:])]
        for col in range(3):
            window = row_array[col:col+4]
            score += scores[window.count(piece)]
    # Calcular puntuación para columnas
    for col in range(6):
        col_array = [int(i) for i in list(board[:,col])]
        for row in range(3):
            window = col_array[row:row+4]
            score += scores[window.count(piece)]
    # Calcular puntuación para diagonales
    for row in range(3):
        for col in range(3):
            window = [board[row+i][col+i] for i in range(4)]
            score += scores[window.count(piece)]
    for row in range(3):
        for col in range(3):
            window = [board[row+3-i][col+i] for i in range(4)]
            score

def find_best_move(board, piece):
    valid_moves = [col for col in range(6) if is_valid_move(board, col)]
    best_score = -10000
    best_col = random.choice(valid_moves)
    for col in valid_moves:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = minimax(temp_board, 5, False, -10000, 10000)
        if score > best_score:
            best_score = score
        best_col = col
    return best_col

#Función para obtener la siguiente fila disponible en una columna
def get_next_open_row(board, col):
    for row in range(6):
        if board[row][col] == 0:
            return row
    return -1

#Función para realizar la poda alpha-beta
def minimax(board, depth, is_maximizing_player, alpha, beta):
    # Verificar si el juego ha terminado
    winner = get_winner(board)
    if winner == COMPUTER_PLAYER:
        return 100 - depth
    elif winner == HUMAN_PLAYER:
        return -100 + depth
    elif is_board_full(board):
        return 0

    # Maximizing player
    if is_maximizing_player:
        best_score = -math.inf
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = get_new_board(board, col, COMPUTER_PLAYER)
                score = minimax(new_board, depth + 1, False, alpha, beta)
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
        return best_score

    # Minimizing player
    else:
        best_score = math.inf
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = get_new_board(board, col, HUMAN_PLAYER)
                score = minimax(new_board, depth + 1, True, alpha, beta)
                best_score = min(best_score, score)
                beta = min(beta, score)
                if alpha >= beta:
                    break
        return best_score if best_score != math.inf else -100

#Función principal del juego
def play_game():
    # Crear el tablero
    board = create_board()
    game_over = False
    turn = random.randint(1, 2)
    print_board(board)
    while not game_over:
        if turn == 1:
        # Turno del jugador
            col = int(input("Jugador 1, elige una columna (0-5): "))
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                print_board(board)
            if get_winner(board) == 1:
                print("¡Jugador 1 gana!")
                game_over = True
                turn = 2
        else:
            # Turno de la computadora
            print("Turno de la computadora...")
            col = find_best_move(board, 2)
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                print_board(board)
            if get_winner(board) == 2:
                print("¡La computadora gana!")
                game_over = True
                turn = 1


if __name__ == '__main__':
    play_game()