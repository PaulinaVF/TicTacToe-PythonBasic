from random import randrange


def DisplayBoard(board):
    for i in range(3):
        print('+-------+-------+-------+\n')
        print('|       |       |       |\n')
        print('|   ', board[i][0], '   |   ', board[i][1], '   |   ', board[i][2], '   |\n', sep='')
        print('|       |       |       |\n')
    print('+-------+-------+-------+\n')


def EnterMove(board):
    move = 0
    while (int(move) < 1 or int(move) > 9):
        move = input('Enter your move: ')
    for row in board:
        if (move in row):
            x = board.index(row)
            y = row.index(move)
            return x, y
    print('Non-valid move')
    return -1, -1


def MakeListOfFreeFields(board):
    freeFi = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] != 'O' and board[i][j] != 'X'):
                freeFi.append((i, j))
    return freeFi


def VictoryFor(board, sign):
    for i in range(3):
        rowSame = 0
        colSame = 0
        for j in range(3):
            if (j == 0):
                rowSame = 1
                colSame = 1
            else:
                if (board[i][j] == board[i][j - 1]):
                    rowSame += 1
                if (board[j][i] == board[j - 1][i]):
                    colSame += 1
        if (rowSame == 3 or colSame == 3):
            return True
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or
            (board[0][2] == board[1][1] and board[1][1] == board[2][0])):
        return True
    else:
        return False


def DrawMove(board):
    pos = randrange(len(areFree))
    return areFree[pos][0], areFree[pos][1]


#
# the function draws the computer's move and updates the board
#

board = [['' for i in range(3)] for j in range(3)]
n = 1
for i in range(3):
    for j in range(3):
        board[i][j] = str(n)
        n += 1

while (True):
    areFree = MakeListOfFreeFields(board)
    if (len(areFree) == 0):
        print('Tied')
        break
    x, y = DrawMove(board)
    board[x][y] = 'X'
    DisplayBoard(board)
    if (VictoryFor(board, 'X')):
        print('Machine WON!')
        break
    areFree = MakeListOfFreeFields(board)
    if (len(areFree) == 0):
        print('Tied')
        break
    x = y = -1
    while(x == -1):
        x, y = EnterMove(board)
    board[x][y] = 'O'
    if (VictoryFor(board, 'O')):
        print('You WON!')
        break

