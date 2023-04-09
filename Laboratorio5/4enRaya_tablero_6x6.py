import random
#Alunos:
#Caique de Paula Figueiredo Coelho
#Lucas Queiroz

def getBoardCopy(board):
    # Hace una copia del tablero y devuélveme esta copia
    duplicateBoard = []

    for i in board:
        duplicateBoard.append(i)

    return duplicateBoard

def drawBoard(board):
    # Esta función imprime el tablero del juego.
    # El marco es una lista de 9 cadenas que representan el tablero
    copyBoard = getBoardCopy(board)

    for i in range(1 ,37):
        if(board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]

    print('  ' + copyBoard[31] + '|' + copyBoard[32] + '|' + copyBoard[33] + '|' + copyBoard[34] + '|' + copyBoard[35] + '|' + copyBoard[36])
    # print(' | |')
    print('--------------------')
    # print(' | |')
    print('  ' + copyBoard[25] + '|' + copyBoard[26] + '|' + copyBoard[27] + '|' + copyBoard[28] + '|' + copyBoard[29] + '|' + copyBoard[30])
    # print(' | |')
    print('--------------------')
    print('  ' + copyBoard[19] + '|' + copyBoard[20] + '|' + copyBoard[21] + '|' + copyBoard[22] + '|' + copyBoard[23] + '|' + copyBoard[24])
    # print(' | |')
    print('--------------------')
    # print(' | |')
    print('  ' + copyBoard[13] + '|' + copyBoard[14] + '|' + copyBoard[15] + '|' + copyBoard[16] + '|' + copyBoard[17] + '|' + copyBoard[18])
    # print(' | |')
    print('--------------------')
    # print(' | |')
    print('  0' + copyBoard[7] + '|0' + copyBoard[8] + '|0' + copyBoard[9] + '|' + copyBoard[10] + '|' + copyBoard[11] + '|' +copyBoard[12])
    # print(' | |')
    print('--------------------')
    # print(' | |')
    print('  0'+ copyBoard[1] + '|0' + copyBoard[2] + '|0' + copyBoard[3] + '|0' + copyBoard[4] + '|0' + copyBoard[5] + '|0' + copyBoard[6])
    # print(' | |')
    print('--------------------')
    # print(' | |')

def inputPlayerLetter():
	# El jugador elige con qué letra quiere jugar "X" u "O"
    # Devuelve una lista con la letra del jugador y la letra de la computadora

	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Elija X o O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("¡Solo ingresa la letra X si quieres ser X o la letra O si quieres ser O!")

	#El primer elemento de la lista es el jugador humano y el segundo es la computadora.
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirts():
	#Elige al azar al jugador que jugará primero
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'humano'

def makeMove(board, letter, move):
    # Hace el movimiento de la computadora o del jugador dependiendo de la letra en el tablero
    board[move] = letter


def isWinner(board, letter):
    # Dado un cuadrado y una letra, esta función devuelve True si la letra dada gana el juego.
    return ((board[31] == letter and board[32] == letter and board[33] == letter and board[34] == letter) or # 1 fila 1 opcion
            (board[32] == letter and board[33] == letter and board[34] == letter and board[35] == letter) or # 1 fila 2 opcion
            (board[33] == letter and board[34] == letter and board[35] == letter and board[36] == letter) or # 1 fila 3 opcion
            (board[25] == letter and board[26] == letter and board[27] == letter and board[28] == letter) or # 2 fila 1 opcion
            (board[26] == letter and board[27] == letter and board[28] == letter and board[29] == letter) or # 2 fila 2 opcion
            (board[27] == letter and board[28] == letter and board[29] == letter and board[30] == letter) or # 2 fila 3 opcion
            (board[19] == letter and board[20] == letter and board[21] == letter and board[22] == letter) or # 3 fila 1 opcion
            (board[20] == letter and board[21] == letter and board[22] == letter and board[23] == letter) or # 3 fila 2 opcion
            (board[21] == letter and board[22] == letter and board[23] == letter and board[24] == letter) or # 3 fila 3 opcion
            (board[13] == letter and board[14] == letter and board[15] == letter and board[16] == letter) or # 4 fila 1 opcion
            (board[14] == letter and board[15] == letter and board[16] == letter and board[17] == letter) or # 4 fila 2 opcion
            (board[15] == letter and board[16] == letter and board[17] == letter and board[18] == letter) or # 4 fila 3 opcion
            (board[7] == letter and board[8] == letter and board[9] == letter and board[10] == letter) or # 5 fila 1 opcion
            (board[8] == letter and board[9] == letter and board[10] == letter and board[11] == letter) or # 5 fila 2 opcion
            (board[9] == letter and board[10] == letter and board[11] == letter and board[12] == letter) or # 5 fila 3 opcion
            (board[1] == letter and board[2] == letter and board[3] == letter and board[4] == letter) or # 6 fila 1 opcion
            (board[2] == letter and board[3] == letter and board[4] == letter and board[5] == letter) or # 6 fila 2 opcion
            (board[3] == letter and board[4] == letter and board[5] == letter and board[6] == letter) or # 6 fila 3 opcion
            (board[31] == letter and board[25] == letter and board[19] == letter and board[13] == letter) or # 1 columna 1 opcion
            (board[25] == letter and board[19] == letter and board[13] == letter and board[7] == letter) or # 1 columna 2 opcion
            (board[19] == letter and board[13] == letter and board[7] == letter and board[1] == letter) or # 1 columna 3 opcion
            (board[32] == letter and board[26] == letter and board[20] == letter and board[14] == letter) or # 2 columna 1 opcion
            (board[26] == letter and board[20] == letter and board[14] == letter and board[8] == letter) or # 2 columna 2 opcion
            (board[20] == letter and board[14] == letter and board[8] == letter and board[2] == letter) or # 2 columna 3 opcion
            (board[33] == letter and board[27] == letter and board[21] == letter and board[15] == letter) or # 3 columna 1 opcion
            (board[27] == letter and board[21] == letter and board[15] == letter and board[9] == letter) or # 3 columna 2 opcion
            (board[21] == letter and board[15] == letter and board[9] == letter and board[3] == letter) or # 3 columna 3 opcion
            (board[34] == letter and board[28] == letter and board[22] == letter and board[16] == letter) or # 4 columna 1 opcion
            (board[28] == letter and board[22] == letter and board[16] == letter and board[10] == letter) or # 4 columna 2 opcion
            (board[22] == letter and board[16] == letter and board[10] == letter and board[4] == letter) or # 4 columna 3 opcion
            (board[35] == letter and board[29] == letter and board[23] == letter and board[17] == letter) or # 5 columna 1 opcion
            (board[29] == letter and board[23] == letter and board[17] == letter and board[11] == letter) or # 5 columna 2 opcion
            (board[23] == letter and board[17] == letter and board[11] == letter and board[5] == letter) or # 5 columna 3 opcion
            (board[36] == letter and board[30] == letter and board[24] == letter and board[18] == letter) or # 6 columna 1 opcion
            (board[30] == letter and board[24] == letter and board[18] == letter and board[12] == letter) or # 6 columna 2 opcion
            (board[24] == letter and board[18] == letter and board[12] == letter and board[6] == letter) or # 6 columna 3 opcion
            (board[19] == letter and board[14] == letter and board[9] == letter and board[4] == letter) or # diagonal principal 1 opcion
            (board[25] == letter and board[20] == letter and board[15] == letter and board[10] == letter) or # diagonal principal 2 opcion
            (board[20] == letter and board[15] == letter and board[10] == letter and board[5] == letter) or # diagonal principal 3 opcion
            (board[31] == letter and board[26] == letter and board[21] == letter and board[16] == letter) or # diagonal principal 4 opcion
            (board[26] == letter and board[21] == letter and board[16] == letter and board[11] == letter) or # diagonal principal 5 opcion
            (board[21] == letter and board[16] == letter and board[11] == letter and board[6] == letter) or # diagonal principal 6 opcion
            (board[32] == letter and board[27] == letter and board[22] == letter and board[17] == letter) or # diagonal principal 7 opcion
            (board[27] == letter and board[22] == letter and board[17] == letter and board[12] == letter) or # diagonal principal 8 opcion
            (board[33] == letter and board[28] == letter and board[23] == letter and board[18] == letter) or # diagonal principal 9 opcion
            (board[13] == letter and board[20] == letter and board[27] == letter and board[34] == letter) or # diagonal secundaria 1 opcion
            (board[7] == letter and board[14] == letter and board[21] == letter and board[28] == letter) or # diagonal secundaria 2 opcion
            (board[14] == letter and board[21] == letter and board[28] == letter and board[35] == letter) or # diagonal secundaria 3 opcion
            (board[1] == letter and board[8] == letter and board[15] == letter and board[22] == letter) or # diagonal secundaria 4 opcion
            (board[8] == letter and board[15] == letter and board[22] == letter and board[29] == letter) or # diagonal secundaria 5 opcion
            (board[15] == letter and board[22] == letter and board[29] == letter and board[36] == letter) or # diagonal secundaria 6 opcion
            (board[2] == letter and board[9] == letter and board[16] == letter and board[23] == letter) or # diagonal secundaria 7 opcion
            (board[9] == letter and board[16] == letter and board[23] == letter and board[30] == letter) or # diagonal secundaria 8 opcion
            (board[3] == letter and board[10] == letter and board[17] == letter and board[24] == letter) # diagonal secundaria 9 opcion
            )

def isSpaceFree(board, move):
    # Devuelve verdadero si el espacio solicitado está libre en el tablero
    if (board[move] == ''):
        return True
    else:
        return False

def getPlayerMove(board):
    # Recibe el movimiento del jugador
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'.split() or not isSpaceFree(board, int(move)):
        print('Cual es su proximo movimiento? (1-36)')
        move = input();
        if (move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'):
            print("MOVIMENTO INVALIDO! INTRODUSCA UN NUMERO ENTRE 1 Y 36!")

        if (move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'):
            if (not isSpaceFree(board, int(move))):
                print(
                    "ESPACIO NO DISPONIBLE! ELIJA OTRO ESPACO ENTRE 1 Y 36 O CUALQUIER NUMERO DISPONIBLE EN EL TABLERO!")

    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Devuelve un movimiento aleatorio válido
    # Devuelve None si no hay movimientos válidos
    possiveisMovimentos = []
    for i in movesList:
        if isSpaceFree(board, i):
            possiveisMovimentos.append(i)

    if len(possiveisMovimentos) != 0:
        return random.choice(possiveisMovimentos)
    else:
        return None

def isBoardFull(board):
    # Devuelve True si todos los espacios de tablero no están disponibles
    for i in range(1, 37):
        if isSpaceFree(board, i):
            return False
    return True

def possiveisOpcoes(board):
    # Devuelve una lista de todos los espacios en el tablero que están disponibles
    opcoes = []

    for i in range(1, 37):
        if isSpaceFree(board, i):
            opcoes.append(i)

    return opcoes

def finishGame(board, computerLetter):
    # Verifica se o jogo chegou ao final
    # Retorna -1 se o jogador ganha
    # Retorna 1 se o computador ganha
    # Retorna 0 se o jogo termina empatado
    # Retorna None se o jogo nao terminou
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if (isWinner(board, computerLetter)):
        return 1
    elif (isWinner(board, playerLetter)):
        return -1
    elif (isBoardFull(board)):
        return 0
    else:
        return None

def alphabeta(board, computerLetter, turn, alpha, beta):
    # Fazemos aqui a poda alphabeta
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if turn == computerLetter:
        nextTurn = playerLetter
    else:
        nextTurn = computerLetter

    finish = finishGame(board, computerLetter)

    if (finish != None):
        return finish

    possiveis = possiveisOpcoes(board)

    if turn == computerLetter:
        for move in possiveis:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val > alpha:
                alpha = val

            if alpha >= beta:
                return alpha
        return alpha

    else:
        for move in possiveis:
            makeMove(board, turn, move)
            val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
            makeMove(board, '', move)
            if val < beta:
                beta = val

            if alpha >= beta:
                return beta
        return beta


def getComputerMove(board, turn, computerLetter):
    # Definimos aqui qual sera o movimento do computador
    a = -2
    opcoes = []

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # if len(possiveisOpcoes(board)) == 9:
    #	return 5

    # Comecamos aqui o MiniMax
    # Primeiro chechamos se podemos ganhar no proximo movimento
    for i in range(1, 37):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Checa se o jogador pode vencer no proximo movimento e bloqueia
    for i in range(1, 37):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    possiveisOpcoesOn = possiveisOpcoes(board)

    for move in possiveisOpcoesOn:
        makeMove(board, computerLetter, move)
        val = alphabeta(board, computerLetter, playerLetter, -2, 2)
        makeMove(board, '', move)

        if val > a:
            a = val
            opcoes = [move]
        elif val == a:
            opcoes.append(move)

    return random.choice(opcoes)

def main():
    jogar = True
    while jogar:
        # Reseta o jogo
        theBoard = [''] * 37
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirts()
        print('El ' + turn + ' juega primero.')
        gameisPlaying = True

        while gameisPlaying:
            if turn == 'humano':
                # Vez do Jogador
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('¡Woooo! ¡Ganaste el juego!')
                    gameisPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('El juego terminó en empate.')
                        break
                    else:
                        turn = 'computador'

            else:
                # Vez do computador
                move = getComputerMove(theBoard, playerLetter, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print("La computadora ganó :(")
                    gameisPlaying = False

                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('El juego terminó en empate.')
                        break
                    else:
                        turn = 'humano'

        letterNew = ''
        while not (letterNew == 'S' or letterNew == 'N'):
            print("¿Quieres jugar de nuevo? Escriba S (para sí) o N (para no)")
            letterNew = input().upper()
            if (letterNew != 'S' and letterNew != 'N'):
                print("¡Entrada inválida! ¡Escriba Y (para sí) o N (para no)!")
            if (letterNew == 'N'):
                print("¡Fue bueno jugar contigo! ¡Hasta luego!")
                jogar = False

if __name__ == '__main__':
    print('¡Juguemos al cuatro en raya!')
    main()
