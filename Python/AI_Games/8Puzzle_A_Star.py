board = [['2', '8', '3'], ['1', '6', '4'], ['7', '-', '5']]
empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
final = [['1', '2', '3'], ['8', '-', '4'], ['7', '6', '5']]
path_cost = 0
queue = []
ll = []
h = {}
count = 0


def display(work):
    global count
    count = count + 1
    print(f"\n\n{count} :\n")
    print('  |   |   ')
    print(work[0][0] + ' | ' + work[0][1] + ' | ' + work[0][2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(work[1][0] + ' | ' + work[1][1] + ' | ' + work[1][2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(work[2][0] + ' | ' + work[2][1] + ' | ' + work[2][2])
    print('  |   |   ')


def check_win(work, final):
    # print("Check win Work:")
    # print(work)
    for i in range(0, 3):
        for j in range(0, 3):
            # print (f"A : {work[i][j]}  B : {final[i][j]}")
            if work[i][j] != final[i][j]:
                return 0
    return 1


def move_up(work):
    new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            new_board[i][j] = work[i][j]
    x = 0
    y = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if new_board[i][j] == '-':
                x = i
                y = j
                break
    if x - 1 >= 0:
        temp = new_board[x - 1][y]
        new_board[x - 1][y] = '-'
        new_board[x][y] = temp
        return new_board
    else:
        return 0


def move_down(work):
    new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            new_board[i][j] = work[i][j]
    x = 0
    y = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if new_board[i][j] == '-':
                x = i
                y = j
                break
    if x + 1 <= 2:
        temp = new_board[x + 1][y]
        new_board[x + 1][y] = '-'
        new_board[x][y] = temp
        return new_board
    else:
        return 0


def move_left(work):
    new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            new_board[i][j] = work[i][j]
    x = 0
    y = 0
    # print("New Board")
    # print(new_board)
    for i in range(0, 3):
        for j in range(0, 3):
            if new_board[i][j] == '-':
                x = i
                y = j
                break
    if y - 1 >= 0:
        temp = new_board[x][y - 1]
        new_board[x][y - 1] = '-'
        new_board[x][y] = temp
        return new_board
    else:
        return 0


def move_right(work):
    new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        # print("uu")
        for j in range(3):
            new_board[i][j] = work[i][j]
    x = 0
    y = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if new_board[i][j] == '-':
                x = int(i)
                y = int(j)
                break
    # print(f"I:{x}  J:{y}")
    if y + 1 <= 2:
        temp = new_board[x][y + 1]
        new_board[x][y + 1] = '-'
        new_board[x][y] = temp
        # print("pp")
        # display(new_board)
        return new_board
    else:
        return 0


def heuristic(new_board):
    global path_cost
    hn = 0
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            for p in range(3):
                for q in range(3):
                    if new_board[i][j] != '-':
                        if new_board[i][j] == final[p][q]:
                            x = p
                            y = q
                            hn = hn + abs(x - i) + abs(y - j)
    hn = hn + path_cost

    return hn


def start(board):
    global h
    global path_cost
    path_cost = path_cost + 1
    # print(check_win())
    if check_win(board, final) == 1:
        return 1
    new_board = move_right(board)
    if new_board != 0:
        display(new_board)
        queue.append(new_board)
        ll.append(heuristic(new_board))
        if check_win(new_board, final) == 1:
            return 1
    new_board = move_up(board)
    if new_board != 0:
        display(new_board)
        queue.append(new_board)
        ll.append(heuristic(new_board))
        if check_win(new_board, final) == 1:
            return 1
    new_board = move_left(board)
    if new_board != 0:
        display(new_board)
        queue.append(new_board)
        ll.append(heuristic(new_board))
        if check_win(new_board, final) == 1:
            return 1
    new_board = move_down(board)
    if new_board != 0:
        display(new_board)
        queue.append(new_board)
        ll.append(heuristic(new_board))
        if check_win(new_board, final) == 1:
            return 1
    minn = 1000000
    ct = 0
    for i in ll:
        if i <= minn:
            minn = i
            board = queue[ct]
        ct = ct + 1
    queue.clear()
    ll.clear()
    #print(f"Board Sent : {board}")
    start(board)

#print("Initial State is  :")
print("\n\n~~~~~~~ E-39 Gaurav Kedia ~~~~~")
print("~~ 8 Puzzle Problem using BFS ~~\n")
display(board)
start(board)
