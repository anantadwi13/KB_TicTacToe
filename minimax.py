# import random
globalComp, globalPlay = '', ''
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def checkPossibleMoves(board):
    possibleMoves = []
    for i in range(1,10):
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return possibleMoves
    else:
        return None

# def chooseRandomMoveFromList(board, movesList):
#     possibleMoves = []
#     for i in movesList:
#         if isSpaceFree(board, i):
#             possibleMoves.append(i)

#     if len(possibleMoves) != 0:
#         return random.choice(possibleMoves)
#     else:
#         return None

def maxVal(board,currTurn,alpha,beta):
    
    if isWinner(board, globalPlay):
        return 0
    elif isWinner(board, globalComp):
        return 100
    elif isBoardFull(board):
        return 50
    
    
    if currTurn== 'X':
        nextTurn = 'O'
    else:
        nextTurn = 'X'

    possibleMoves = checkPossibleMoves(board)
    score = -100000
    for i in possibleMoves:
        copy = getBoardCopy(board)
        makeMove(copy,currTurn,i)
        score = max(score,minVal(copy,nextTurn,alpha,beta))
        if score >= beta:
            return score
        alpha = max(alpha,score)
        
    return score

def minVal(board,currTurn,alpha,beta):
    if isWinner(board, globalPlay):
        return 0
    elif isWinner(board, globalComp):
        return 100
    elif isBoardFull(board):
        return 50
  
    if currTurn== 'X':
        nextTurn = 'O'
    else:
        nextTurn = 'X'

    possibleMoves = checkPossibleMoves(board)
    score = 100000
    for i in possibleMoves:
        copy = getBoardCopy(board)
        makeMove(copy,currTurn,i)
        score = min(score, maxVal(copy,nextTurn,alpha,beta))
        if score <= alpha:
            return score
        beta = min(beta,score)

    return score

def getComputerMove(board, computerLetter):

    if computerLetter== 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    possibleMoves = checkPossibleMoves(board)
    alpha = -100000
    beta = 100000
    score = -100000

    for i in possibleMoves:
        copy = getBoardCopy(board)
        makeMove(copy,computerLetter,i)
        s = minVal(copy,playerLetter,alpha,beta)
        if s > alpha:
            score = s
            move = i
        alpha = max(alpha,score)
    
    return move

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    globalPlay, globalComp = playerLetter, computerLetter
    turn = 'player'
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break