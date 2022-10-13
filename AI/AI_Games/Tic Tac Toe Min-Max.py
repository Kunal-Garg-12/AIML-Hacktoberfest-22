import time

AI_1 = 'x'
AI_2 = 'o'
board = [
    ['x', '_', '_'],
    ['x', 'o', 'o'],
    ['_', '_', '_']
]
count = 1

def display(board):
    global count
    print('__________________________________________\n')
    print(str(count) + ')\n')
    count+=1
    print('  |   |   ')
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('  |   |   ')



def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False


def check_win(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == AI_1):
                return 1
            elif (b[row][0] == AI_2):
                return -1

    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == AI_1):
                return 1
            elif (b[0][col] == AI_2):
                return -1

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == AI_1):
            return 1
        elif (b[0][0] == AI_2):
            return -1

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == AI_1):
            return 1
        elif (b[0][2] == AI_2):
            return -1

    return 0


def minimax(board, depth, isMax):
    score = check_win(board)

    if (score == 1):
        return 1

    if (score == -1):
        return -1

    if (isMovesLeft(board) == False):
        return 0


    if (isMax):
        best = -10000000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = AI_1
                    best = max(best, minimax(board,depth + 1,not isMax))
                    board[i][j] = '_'
        return best

    else:
        best = 10000000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = AI_2
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board,flag):
    bestVal = -1000000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                if flag:
                    board[i][j] = AI_1
                else:
                    board[i][j] = AI_2
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove




def start_game(flag):
    bestMove = findBestMove(board,flag)

    if flag:
        #print('Flag is True')
        board[bestMove[0]][bestMove[1]]=AI_1
        display(board)
    else:
        #print('Flag is False')
        board[bestMove[0]][bestMove[1]] = AI_2
        display(board)

def play():
    print('AI VS AI Tic Tac Toe Game')
    print('Algorithm used is  MinMax')
    print('Initial Board is : ')
    display(board)
    time.sleep(1)
    player = 0
    flag = True
    while(isMovesLeft(board)==True and check_win(board)==0):
        start_game(flag)
        flag = not flag
        #print('hi')
        time.sleep(3)
    if check_win(board)==0:
        print("\nGame Tie ")
    elif check_win(board)==1:
        print('\nAI_1 WON ')
    else:
        print('\nAI_2 WON ')



play()

