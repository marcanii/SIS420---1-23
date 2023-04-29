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

    for i in range(1 ,10):
        if(board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]

    print(' ' + copyBoard[7] + '|' + copyBoard[8] + '|' + copyBoard[9])
    # print(' | |')
    print('-------')
    # print(' | |')
    print('  '+ copyBoard[4] + '|' + copyBoard[5] + '|' + copyBoard[6])
    # print(' | |')
    print('-------')
    # print(' | |')
    print('  '+ copyBoard[1] + '|' + copyBoard[2] + '|' + copyBoard[3])
    # print(' | |')
    print('-------')
# print(' | |')

def inputPlayerLetter():
	# El jugador elige con qué letra quiere jugar "X" u "O"
  # Devuelve una lista con la letra del jugador y la letra de la computadora

	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Usted quiere ser X o O?')
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
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # linea superior
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # linea del medio
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # linea de abajo
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # columna de la izquierda
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # columna del medio
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # columna da la derecha
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal principal
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal secundaria


def isSpaceFree(board, move):
    # Devuelve verdadero si el espacio solicitado está libre en el tablero
    if (board[move] == ''):
        return True
    else:
        return False


def getPlayerMove(board):
    # Recibe el movimiento del jugador
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Cual es su proximo movimiento? (1-9)')
        move = input();
        if (move not in '1 2 3 4 5 6 7 8 9'):
            print("MOVIMENTO INVALIDO! INTRODUSCA UN NUMERO ENTRE 1 Y 9!")

        if (move in '1 2 3 4 5 6 7 8 9'):
            if (not isSpaceFree(board, int(move))):
                print(
                    "ESPACIO NO DISPONIBLE! ELIJA OTRO ESPACO ENTRE 1 Y 9 O CUALQUIER NUMERO DISPONIBLE EN EL TABLERO!")

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
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def possiveisOpcoes(board):
    # Devuelve una lista de todos los espacios en el tablero que están disponibles

    opcoes = []

    for i in range(1, 10):
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
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Checa se o jogador pode vencer no proximo movimento e bloqueia
    for i in range(1, 10):
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


print('Vamos jogar jogo da velha!')

def main():
    jogar = True

    while jogar:
        # Reseta o jogo
        theBoard = [''] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirts()
        print('O ' + turn + ' joga primeiro,')
        gameisPlaying = True

        while gameisPlaying:
            if turn == 'jogador':
                # Vez do Jogador
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Woooow! Voce venceu o jogo!')
                    gameisPlaying = False

                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('O jogo terminou empatado')
                        break
                    else:
                        turn = 'computador'

            else:
                # Vez do computador
                move = getComputerMove(theBoard, playerLetter, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print("O computador venceu :(")
                    gameisPlaying = False

                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('O jogo terminou empatado')
                        break
                    else:
                        turn = 'jogador'

        letterNew = ''
        while not (letterNew == 'S' or letterNew == 'N'):
            print("Voce quer jogar novamente? Digite S(para sim) ou N(para nao)")
            letterNew = input().upper()
            if (letterNew != 'S' and letterNew != 'N'):
                print("Entrada invalida! Digite S(para sim) ou N(para nao)!")
            if (letterNew == 'N'):
                print("Foi bom jogar com voce! Ate mais!")
                jogar = False

if __name__ == '__main__':
    main()
