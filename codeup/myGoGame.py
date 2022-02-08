
board = []

for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

for i in range(19):
    b = input().split()
    for j in range(19):
        board[i+1][j+1] = int(b[j])

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1,20):
        if board[j][y] == 0 : board[j][y] = 1
        else: board[j][y] = 0
        if board[x][j] == 0 : board[x][j] = 1
        else: board[x][j] = 0



for i in range(1,20):
    for j in range(1,20):
        print(board[i][j], end = " ")
    print()
